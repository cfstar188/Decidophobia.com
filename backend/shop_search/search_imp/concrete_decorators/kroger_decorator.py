from ..decorator_helper import *


class KrogerDecorator(SearcherDecorator):
    def __init__(self, searcher):
        super().__init__(searcher)

    async def mint_auth_token(self, auth_info):
        async with aiohttp.ClientSession() as session:
            async with session.post(auth_info.mint_url,
                                    data=auth_info.request_body,
                                    headers=auth_info.request_headers) as token_response:

                if token_response.status == 200:
                    token_details = await token_response.json()

                    # update the config file to reflect the request for a new token
                    token_duration = timedelta(seconds=int(token_details.get("expires_in")))
                    auth_info.token_expiry = datetime.now(UTC) + token_duration

                    # set in new token into the config file
                    auth_info.token = token_details.get("access_token")
                    await auth_info.asave()
                    return True
                else:
                    return False

    async def perform_search(self, search_params):
        item, num_items, force_new_token = self.get_params(search_params)

        token = await self.get_auth_token(force_new_token)
        if token == -1:
            print("(kroger) Couldn't mint new authorization token.")
            return []

        search_info = await SearchInfo.objects.aget(shop_name="kroger")
        print("Kroger request initiated")
        async with aiohttp.ClientSession() as session:
            async with session.get(search_info.base_url,
                                       params={"filter.term": item,
                                              "filter.locationId": "01400465",
                                              "filter.limit": 50},
                                       headers=search_info.request_headers | {
                                          "Authorization": f'Bearer {token}'}) as search_response:
                if search_response.status == 200:
                    search_dict = await search_response.json()
                    if not search_dict.get("data"):
                        print("(kroger) No results found.")
                        return []
                    all_items = []
                    seller_metrics = []
                    for elem in search_dict.get("data"):
                        if (elem.get("items")[0].get("price")):
                            if elem.get("items")[0].get("price").get("promo") > 0:
                                price = elem.get("items")[0].get("price").get("promo")
                            else:
                                price = elem.get("items")[0].get("price").get("regular")

                            all_items.append({"name": elem.get("description"),
                                            "shop": "Kroger",
                                            "link": f'https://www.kroger.com/p/giveus100onsprint3plz/{elem.get("productId")}',
                                            "image": elem.get("images")[0].get("sizes")[0].get("url"),
                                            "price": price,
                                            "currency": "USD",
                                            "score": 78,
                                            "metrics":{"price": price}})
                    print("Kroger request performed succesfully")
                    return all_items
                else:
                    print("Kroger search failed.")
                    return []

    def get_shop_name(self):
        return "kroger"

    def get_token_config(self, config_file):
        return super().get_token_config(config_file)
