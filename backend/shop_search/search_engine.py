from .searcher_comp import Searcher
from .concrete_decorators import *
from .mo

eligible_shops = ["ebay", "bestbuy"]
def exec_search(search_query):
    sanitize_params(search_query)
    searcher = Searcher()

    for shop in search_query["shops"]:
        match shop.lower():
            case "ebay":
                searcher = EbayDecorator(searcher)
            case "bestbuy":
                searcher = BestbuyDecorator(searcher)
            case _:
                print("An unknown shop was passed in. How is this possible?")

    return searcher.shop_search(search_query)

def set_up_database():
    ebay_auth = E
'''
This basically auto_completed the search_query for all excluded parameters
It also sanitizes the search_query by ensuring it is only made up of valid parameters.
'''
def sanitize_params(search_query):
    # item_name = "watch", num_items = 100, force_new_token = False
    if not search_query.get("item_name") or not isinstance(search_query.get("item_name"), str):
        search_query["item_name"] = "watch"
    if not search_query.get("num_items") or not isinstance(search_query.get("num_items"), int):
        search_query["num_items"] = 100
    if not search_query.get("force_new_token") or not isinstance(search_query.get("force_new_token"), bool):
        search_query["force_new_token"] = False

    is_string = isinstance(search_query.get("shops"), str)
    is_list = isinstance(search_query.get("shops"), list)

    if not search_query.get("shops") or not is_string or not is_list:
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


def elegant_print(self, item_list):
    for item in item_list:
        print("Item Name:", item.name)
        print("Item Link:", item.link)
        print("Item image link:", item.image)
        print("Item price:", item.price, item.currency)
        print("Score:", item.currency)
        print("=" * 50)
