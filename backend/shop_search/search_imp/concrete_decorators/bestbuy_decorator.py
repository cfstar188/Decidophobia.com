from ..decorator_helper import *

class BestbuyDecorator(SearcherDecorator):
    def __init__(self, searcher):
        super().__init__(searcher)
    def mint_auth_token(self, config_file):
        return True
    def perform_search(self, search_params):
        pass
    def get_shop_name(self):
        return "bestbuy"

    def get_token_config(self, config_file):
        return super().get_token_config(config_file)
