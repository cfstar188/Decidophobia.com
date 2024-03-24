from ..decorator_helper import *


class EbayDecorator(SearcherDecorator):
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
            print("(ebay) Couldn't mint new authorization token.")
            return []

        search_info = await SearchInfo.objects.aget(shop_name="ebay")
        print("eBay request initiated")
        async with aiohttp.ClientSession() as session:
            async with session.get(search_info.base_url,
                                       params={"q": item,
                                              "limit": num_items},
                                       headers=search_info.request_headers | {
                                          "Authorization": f'Bearer {token}'}) as search_response:
                if search_response.status == 200:
                    search_dict = await search_response.json()
                    if not search_dict.get("itemSummaries"):
                        print("(eBay) No results found.")
                        return []
                    all_items = []
                    seller_metrics = []
                    for elem in search_dict.get("itemSummaries"):
                        if  (elem.get("seller").get("feedbackScore") and elem.get("seller").get("feedbackPercentage")):
                            if elem.get("image"):
                                image = elem.get("image").get("imageUrl")
                            else:
                                image = "https://demofree.sirv.com/nope-not-here.jpg"

                            all_items.append({"name": elem.get("title"),
                                            "shop": "eBay",
                                            "link": elem.get("itemWebUrl"),
                                            "image": image,
                                            "price": elem.get("price").get("value"),
                                            "currency": elem.get("price").get("currency"),
                                            "score": 72,
                                            "metrics": {"feedback_score": elem.get("seller").get("feedbackScore"),
                                                "feedback_percentage": elem.get("seller").get("feedbackPercentage")}})
                        
                    print("eBay request performed succesfully")

                    return all_items
                else:
                    print("eBay search failed.")
                    return []

    def get_shop_name(self):
        return "ebay"

    def get_token_config(self, config_file):
        return super().get_token_config(config_file)
