from searcher_interface import SearcherInterface
from concurrent.futures import ThreadPoolExecutor

class Searcher(SearcherInterface):
    def __init__(self):
        thread_pool = ThreadPoolExecutor()

    def shop_search(self, search_params):
        return []
