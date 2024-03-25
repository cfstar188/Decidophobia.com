from .search_imp.searcher_comp import Searcher
from .search_imp.concrete_decorators import *
from .models import AuthInfo, SearchInfo
import asyncio

"""
(Use function 'shop_search' to perform any searches)
Makes an external request to multiple shopping sites to execute a search query.

Input:
The function 'search_engine' takes in a **dictionary** with the following keys:
All the following key-value pairs are optional. The default value for each key
will be specified.

    shops: list 
    This is the name of the shopping sites you want to search. 
    Currently, the supported sites are "ebay", "bestbuy" and "kroger" [case-insensitive].
    Additionally, a value of ["all"] searches all supported sites
    **Default**: ["all"]

    item: string 
    This is the name of the item you want to search for.
    **Default**: "watch"

    num_items: int
    This is the number of items you want returned back for EACH shop.
    **Default**: "100"

    force_new_token = False
    You shouldn't need to pass this in, ever. This is more so for testing; if 
    you need to force a new authorization token to be generated, you can set 
    this to True. If set to False, an authorization token will be generated 
    automatically, when needed.
    **Default**: False


Output:
The function returns a list of dictionaries. Each dictionary has the following key-value pairs:

    dict['shop']: string
    This is the name of the shop that was searched

    dict['name']: string
    This is the name of the item found in the search result

    dict['link']: string
    This is the link to the product on the shop's website

    dict['image']: string
    This is a link to the product image

    dict['price']: float
    This is the price of the product in USD
    
    dict['currency']: string
    This is the currency the product price is in. 
    Currently, dict['currency'] will always be USD.

    dict['score']: int
    This is our unique score that we give to items (it defaults to the brand reputation
    score currently, as given in https://theharrispoll.com/partners/media/axios-harrispoll-100/)

    dict['metrics']: dict
    This is only used by the questionnaire app. They consist of the specific metrics
    each e-commerce website uses to rate their products. As such, they differ for each
    e-commerce site.
        eBay:
        -- dict['metrics']['feedback_score']: Gives you the seller's delta review count,
        based on the number of positive reviews minus the number of negative reviews.
        -- dict['metrics']['feedback_percentage']: Gives you the seller's positive
        review percentage, based on the number of positive reviews divided by the
        total review count.


        BestBuy:
        -- dict['metrics']['review_count']: Gives you the number of product reviews.
        -- dict['metrics']['review_average']: Gives you the average product rating.

        Kroger:
        -- dict['metrics']['price']: Gives you the price of the product.

"""


eligible_shops = ["ebay", "bestbuy", "kroger"]

'''Main function that performs a search query to all supported shopping sites'''
def search_engine(search_query):
    sanitize_params(search_query)
    searcher = Searcher()
    setup_database()

    for shop in search_query["shops"]:
        match shop.lower():
            case "ebay":
                searcher = EbayDecorator(searcher)
            case "bestbuy":
                searcher = BestbuyDecorator(searcher)
            case "kroger":
                searcher = KrogerDecorator(searcher)
            case _:
                print("An unknown shop was passed in. How is this possible?")

    search_results = asyncio.run(searcher.org_tasks(search_query))
    nonempty_results = [result for result in search_results if result]
    return interweave_results(nonempty_results)


'''interweave search results between different shopping sites just for show'''
def interweave_results(search_results):
    bestbuy_results = [result for result in search_results if result["shop"].lower() == "bestbuy"]
    ebay_results = [result for result in search_results if result["shop"].lower() == "ebay"]
    kroger_results = [result for result in search_results if result["shop"].lower() == "kroger"]

    interweave = []
    for i in range(max(len(ebay_results), len(bestbuy_results), len(kroger_results))):
        if i < len(ebay_results):
            interweave.append(ebay_results[i])
        if i < len(bestbuy_results):
            interweave.append(bestbuy_results[i])
        if i < len(kroger_results):
            interweave.append(kroger_results[i])

    return interweave


async def task_results(tasks):
    async with tasks:
        print("wait for tasks")


def setup_database():
    if len(AuthInfo.objects.all()) == len(eligible_shops):
        return

    ebay_auth = AuthInfo(shop_name="ebay",
                         mint_url="https://api.ebay.com/identity/v1/oauth2/token",
                         request_headers={
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Authorization": "Basic QWhtZWRNb2gtZGVjaWRvcGgtUFJELWMxZTJiYjU2My1mNDFlNDRkMzpQUkQtMWUyYmI1NjNlZmRmLTBmMTktNDU1Yy1iMDZlLTNlNmUgDQo="},
                         request_body={"grant_type": "client_credentials",
                                       "scope": "https://api.ebay.com/oauth/api_scope"})
    ebay_auth.save()

    ebay_search = SearchInfo(shop_name="ebay",
                             base_url="https://api.ebay.com/buy/browse/v1/item_summary/search",
                             request_headers={
                                 "X-EBAY-C-MARKETPLACE-ID": "EBAY_US"})
    ebay_search.save()

    kroger_auth = AuthInfo(shop_name="kroger",
                         mint_url="https://api.kroger.com/v1/connect/oauth2/token",
                         request_headers={
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Authorization": "Basic ZGVjaWRvcGhvYmlhLThlMmI4NWY0YzIyYmI2YThjOGVkOGI3YTVhYjY5ZTgxNzkwOTAxMDg2Mjg3OTM0MTc0OTppU3hQS09QTERNaXFCbnRiS3ZwUExqVUt5LUN6QVcwVXBuRC1xTkpF"},
                         request_body={"grant_type": "client_credentials",
                                       "scope": "product.compact"})
    kroger_auth.save()

    kroger_search = SearchInfo(shop_name="kroger",
                             base_url="https://api.kroger.com/v1/products",
                             request_headers={
                                 "Accept": "application/json"})
    kroger_search.save()


    bestbuy_auth = AuthInfo(shop_name="bestbuy",
                            token="a6xmm2a2athgchfhkwuv8vpq")
    bestbuy_auth.save()

    bestbuy_search = SearchInfo(shop_name="bestbuy",
                                base_url="https://api.bestbuy.com/v1/products")
    bestbuy_search.save()


'''
This basically auto_completed the search_query for all excluded parameters
It also sanitizes the search_query by ensuring it is only made up of valid parameters.
'''
def sanitize_params(search_query):
    # item_name = "watch", num_items = 100, force_new_token = False
    if not search_query.get("item") or not isinstance(search_query.get("item"),
                                                      str):
        search_query["item"] = "watch"
    if not search_query.get("num_items") or not isinstance(
            search_query.get("num_items"), int):
        search_query["num_items"] = 100
    if not search_query.get("force_new_token") or not isinstance(
            search_query.get("force_new_token"), bool):
        search_query["force_new_token"] = False

    is_string = isinstance(search_query.get("shops"), str)
    is_list = isinstance(search_query.get("shops"), list)

    if not search_query.get("shops") or (not is_string and not is_list):
        search_query["shops"] = eligible_shops
    if is_string:
        search_query["shops"] = [search_query.get("shops")]
    if is_list:
        shops = search_query.get("shops")
        if "all" in shops:
            search_query["shops"] = eligible_shops
        else:
            for i, shop in enumerate(shops):
                if not isinstance(shop, str) or shop.lower() not in eligible_shops:
                    shops.pop(i)


'''Prints the outputted search_result elegantly in the console. You don't need
to use this function now, you can use the tester_app by:
1) Running the development server
2) Head to the link "/search_item/your-item-spaced-with-asterisks'''
def elegant_print(item_list):
    for item in item_list:
        print("Item Name:", item["name"])
        print("Shop Name:", item["shop"])
        print("Item Link:", item["link"])
        print("Item image link:", item["image"])
        print("Item price:", item["price"], item["currency"])
        print("Score:", item["score"])
        print("=" * 50)


if __name__ == "__main__":
    elegant_print(search_engine({"item": "iphone", "shops": "ebay"}))
    print("im shutting down buddy")
