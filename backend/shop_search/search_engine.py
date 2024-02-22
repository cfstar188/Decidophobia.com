from .search_imp.searcher_comp import Searcher
from .search_imp.concrete_decorators import *
from .models import AuthInfo, SearchInfo


eligible_shops = ["ebay", "bestbuy"]
def search_engine(search_query):
    sanitize_params(search_query)
    searcher = Searcher()
    # setup_database()

    for shop in search_query["shops"]:
        match shop.lower():
            case "ebay":
                searcher = EbayDecorator(searcher)
            case "bestbuy":
                searcher = BestbuyDecorator(searcher)
            case _:
                print("An unknown shop was passed in. How is this possible?")

    list = searcher.shop_search(search_query)
    return list

def setup_database():
    if AuthInfo.objects.all():
        return

    ebay_auth = AuthInfo(shop_name = "ebay",
                         mint_url = "https://api.ebay.com/identity/v1/oauth2/token",
                         request_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "Basic QWhtZWRNb2gtZGVjaWRvcGgtUFJELWMxZTJiYjU2My1mNDFlNDRkMzpQUkQtMWUyYmI1NjNlZmRmLTBmMTktNDU1Yy1iMDZlLTNlNmUgDQo="},
                         request_body = {"grant_type": "client_credentials",
                                         "scope": "https://api.ebay.com/oauth/api_scope"})
    ebay_auth.save()

    ebay_search = SearchInfo(shop_name = "ebay",
                             base_url = "https://api.ebay.com/buy/browse/v1/item_summary/search",
                             request_headers = {"X-EBAY-C-MARKETPLACE-ID": "EBAY_US"})
    ebay_search.save()

    bestbuy_auth = AuthInfo(shop_name = "bestbuy",
                            token = "a6xmm2a2athgchfhkwuv8vpq")
    bestbuy_auth.save()

    bestbuy_search = SearchInfo(shop_name = "bestbuy",
                                base_url = "https://api.bestbuy.com/v1/products")
    bestbuy_search.save()

'''
This basically auto_completed the search_query for all excluded parameters
It also sanitizes the search_query by ensuring it is only made up of valid parameters.
'''
def sanitize_params(search_query):
    # item_name = "watch", num_items = 100, force_new_token = False
    if not search_query.get("item") or not isinstance(search_query.get("item"), str):
        search_query["item"] = "watch"
    if not search_query.get("num_items") or not isinstance(search_query.get("num_items"), int):
        search_query["num_items"] = 100
    if not search_query.get("force_new_token") or not isinstance(search_query.get("force_new_token"), bool):
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
            shops = eligible_shops
        else:
            for i, shop in enumerate(shops):
                if not isinstance(shop, str) or shop.lower() not in eligible_shops:
                    shops.pop(i)


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
