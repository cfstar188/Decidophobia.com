class SearcherInterface:
    def shop_search(self, search_params, tg):
        raise NotImplementedError

    def get_shop_name(self):
        raise NotImplementedError
