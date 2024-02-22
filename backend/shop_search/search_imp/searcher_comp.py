from .searcher_interface import SearcherInterface
from concurrent.futures import ThreadPoolExecutor, as_completed


class Searcher(SearcherInterface):
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=10)
        self.futures = []

    def shop_search(self, search_params):
        results = []
        for future in as_completed(self.futures):
            results = future.result()
        return results
