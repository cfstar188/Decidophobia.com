import os

from .searcher_interface import SearcherInterface
from .decorator_helper import *

class SearcherDecorator(SearcherInterface):
    def __init__(self, searcher):
        self.searcher = searcher
        self.thread_pool = searcher.thread_pool
        self.futures = searcher.futures

    def mint_auth_token(self, config_file):
        raise NotImplementedError

    def get_auth_token(self, force_new_token=False):
        with open("shop_search/search_imp/api_config.json", 'r') as config_file:
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
        self.futures.append(self.thread_pool.submit(self.perform_search,
                                                    search_params=search_params))
        return self.searcher.shop_search(search_params)

    def perform_search(self, search_params):
        raise NotImplementedError

    def get_shop_name(self):
        raise NotImplementedError

    def get_token_config(self, config_file):
        return config_file.get("shops").get(self.get_shop_name()).get("token_info")

    def get_params(self, search_params):
        return search_params["item"], search_params["num_items"], search_params["force_new_token"]
