from ..searcher_decorator import SearcherDecorator
from ..decorator_helper import *


class EbaySearch(SearcherDecorator):
    def __init__(self, searcher):
        super().__init__(searcher)

    def mint_auth_token(self, config_file):
        token_config = self.get_token_config(config_file)
        token_response = requests.post(token_config.get("url"),
                                       data=token_config.get("body"),
                                       headers=token_config.get("headers"))

        if token_response.status_code == 200:
            token_details = json.loads(token_response.content)

            # update the config file to reflect the request for a new token
            token_duration = timedelta(seconds=int(token_details.get("expires_in")
                                                   .strftime(config_file.get("date_format"))))
            token_config["token_expiry"] = datetime.now(UTC) + token_duration

            # set in new token into the config file
            token_config["token"] = token_details.get("access_token")
            config_file["shops"]["ebay"]["token_info"] = token_config
            with open("api_config.json", "w") as config_file:
                config_file.write(json.dumps(config_file))
            return True
        else:
            return False

    def shop_search(self, search_params):
        item_name, num_items, force_new_token = super().fillin_params(search_params)

        token = self.get_auth_token(force_new_token)
        if token == -1:
            return []
        with open("../api_config.json", 'r') as config_file:
            config_file = json.load(config_file)
        search_info = config_file.get("shops").get("ebay").get("search_info")
        search_response = requests.get(search_info.get("url"),
                                       params={"q": item_name,
                                              "limit": num_items},
                                       headers=search_info.get("headers") | {
                                          "Authorization": f'Bearer {token}'})
        if search_response.status_code == 200:
            search_dict = json.loads(search_response.content)
            if not search_dict.get("itemSummaries"):
                print("(eBay) No results found.")
                return self.searcher.shop_search()
            all_items = []
            seller_metrics = []
            for elem in search_dict.get("itemSummaries"):
                all_items.append({"item_name": elem.get("title"),
                                  "link": elem.get("itemWebUrl"),
                                  "image": elem.get("image").get("imageUrl"),
                                  "price": elem.get("price").get("value"),
                                  "currency": elem.get("price").get("currency"),
                                  "score": 100})
                seller_metrics.extend([elem.get("seller").get("feedbackScore"),
                                       elem.get("seller").get("feedbackPercentage")])
            return self.searcher.shop_search().extend(all_items)
        else:
            print("eBay search failed.")
            return self.searcher.shop_search()

    def get_shop_name(self):
        return "ebay"

    def get_token_config(self, config_file):
        return super().get_token_config(config_file)
