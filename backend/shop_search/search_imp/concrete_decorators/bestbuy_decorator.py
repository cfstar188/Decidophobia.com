from ..decorator_helper import *

class BestbuyDecorator(SearcherDecorator):
    def __init__(self, searcher):
        super().__init__(searcher)
    async def perform_search(self, search_params):
        item, num_items, force_new_token = self.get_params(search_params)
        auth_info = await AuthInfo.objects.aget(shop_name = "bestbuy")
        token = auth_info.token

        if token is None:
            print("Supposedly static auth token has not been set")
            return []

        search_info = await SearchInfo.objects.aget(shop_name="bestbuy")

        # could be reset in the future
        online_availability = True
        if online_availability:
            online_availability = "onlineAvailability=false"
        else:
            online_availability = ''

        seperator = "&search="
        if '-' not in item:
            formatted_item = seperator.join(item.split(" "))
        else:
            formatted_item = seperator.join(item.split("-"))

        formatted_item = "search=" + formatted_item
        url_append = f'(({formatted_item})&{online_availability})'

        print("BestBuy request initiated")
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{search_info.base_url}{url_append}',
                                       params={"pageSize": num_items,
                                               "apiKey": token,
                                               "format": "json"}) as search_response:

                if search_response.status == 200:
                    search_dict = await search_response.json()
                    if not search_dict.get("products"):
                        print("(BestBuy) No results found.")
                        return []
                    all_items = []
                    seller_metrics = []
                    for elem in search_dict.get("products"):
                        if (elem.get("customerReviewCount") and elem.get("customerReviewAverage")):
                            all_items.append({"name": elem.get("name"),
                                            "shop": "BestBuy",
                                            "link": elem.get("url"),
                                            "image": elem.get("image"),
                                            "price": elem.get("salePrice"),
                                            "currency": "USD",
                                            "score": 80,
                                            "metrics": {"review_count": elem.get("customerReviewCount"),
                                                "review_average": elem.get("customerReviewAverage")}})

                    print("BestBuy request performed succesfully")

                    return all_items
                else:
                    print("BestBuy search failed.")
                    return []

    def get_shop_name(self):
        return "bestbuy"

    def get_token_config(self, config_file):
        return super().get_token_config(config_file)
