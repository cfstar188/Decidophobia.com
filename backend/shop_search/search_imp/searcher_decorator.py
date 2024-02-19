from searcher_interface import SearcherInterface
from decorator_helper import *


class SearcherDecorator(SearcherInterface):
    def __init__(self, searcher):
        self.searcher = searcher
        self.thread_pool = searcher.thread_pool

    def mint_auth_token(self, config_file):
        raise NotImplementedError

    def get_auth_token(self, force_new_token=False):
        config_file = None
        with open("api_config.json", 'r') as config_file:
            config_file = json.load(config_file)
        token_config = self.get_token_config(config_file)

        expiry_time = datetime.strptime(token_config.get("token_expiry"),
                                        config_file.get("date_format"))
        current_time = datetime.now(UTC)

        if force_new_token or expiry_time < current_time:
            if self.mint_auth_token(config_file):
                print("New access token minted")
            else:
                print("Couldn't acquire access token. Sorry!")
                return -1

        return token_config.get("token")

    def shop_search(self, search_params):
        raise NotImplementedError

    def get_shop_name(self):
        raise NotImplementedError

    def get_token_config(self, config_file):
        return config_file.get("shops").get(self.get_shop_name()).get(
            "token_info")

    def fillin_params(self, search_params):
        # item_name = "watch", num_items = 100, force_new_token = False
        if not search_params.get("item_name"):
            search_params["item_name"] = "watch"
        elif not search_params.get("num_items"):
            search_params["num_items"] = 100
        elif not search_params.get("force_new_token"):
            search_params["force_new_token"] = False

        return search_params["item_name"], search_params["num_items"], search_params["force_new_token"]
