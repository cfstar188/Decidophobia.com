from searcher_interface import SearcherInterface
from concurrent.futures import ThreadPoolExecutor

class Searcher(SearcherInterface):
    def __init__(self):
        thread_pool = ThreadPoolExecutor()

    def elegant_print(item_list):
        for item in item_list:
            print("Item Name:", item.name)
            print("Item Link:", item.link)
            print("Item image link:", item.image)
            print("Item price:", item.price, item.currency)
            print("Score:", item.currency)
            print("=" * 50)


    def shop_search(self, search_params):
        return []

    if __name__ == "__main__":
        elegant_print(shop_search(item_name="laptop sleeve", num_items=20))
