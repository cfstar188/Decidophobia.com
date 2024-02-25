import asyncio

from .searcher_interface import SearcherInterface

class Searcher(SearcherInterface):

    def __init__(self):
        self.tasks = []
    def shop_search(self, search_params, tg):
        return

    def get_shop_name(self):
        return "base"
