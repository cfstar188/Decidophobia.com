from .searcher_interface import SearcherInterface
from ..models import AuthInfo
from datetime import datetime, UTC
import asyncio

class SearcherDecorator(SearcherInterface):
    def __init__(self, searcher):
        self.searcher = searcher
        self.tasks = self.searcher.tasks


    def mint_auth_token(self, config_file):
        raise NotImplementedError

    async def get_auth_token(self, force_new_token=False):
        auth_info = await AuthInfo.objects.aget(shop_name=self.get_shop_name())
        expiry_time = auth_info.token_expiry
        if auth_info.mint_url is None:
            return None

        current_time = datetime.now(UTC)
        if force_new_token or expiry_time is None or expiry_time < current_time:
            if await self.mint_auth_token(auth_info):
                print("New access token minted")
            else:
                print("Couldn't acquire access token. Sorry!")
                return -1

        return auth_info.token

    async def org_tasks(self, search_params):
        async with asyncio.TaskGroup() as tg:
            self.searcher.shop_search(search_params, tg)
            self.tasks.append(tg.create_task(self.perform_search(search_params)))

        results = []
        for task in self.tasks:
            results.extend(task.result())

        return results

    def shop_search(self, search_params, tg=None):
        self.searcher.shop_search(search_params, tg)
        self.tasks.append(tg.create_task(self.perform_search(search_params)))

    def perform_search(self, search_params):
        raise NotImplementedError

    def get_shop_name(self):
        raise NotImplementedError

    def get_token_config(self, config_file):
        return config_file.get("shops").get(self.get_shop_name()).get("token_info")

    def get_params(self, search_params):
        return search_params["item"], search_params["num_items"], search_params["force_new_token"]
