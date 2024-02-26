import requests
import json
from datetime import datetime, UTC, timedelta

import pytz

from django.conf import settings
import os

config_path = os.path.join(settings.BASE_DIR, '../', 'ShopSearch', 'api_config.json')

date_format = "%Y/%m/%d %H:%M:%S %z"

def mint_ebay_token(ebay_config):
    # make api call to get token, along with important details regarding it
    token_response = requests.post(ebay_config.get("url"),
                                   data=ebay_config.get("body"),
                                   headers=ebay_config.get("headers"))

    if token_response.status_code == 200:
        token_details = json.loads(token_response.content)
        # update the config file to reflect the request for a new token
        ebay_config["token_expiry"] = (datetime.now(UTC) +
                                       timedelta(seconds=int(token_details.get("expires_in")))).strftime(date_format)
        ebay_config["token"] = token_details.get("access_token")
        return True
    else:
        return False


def get_ebay_token(force_new_token=False):
    with open(config_path, 'r') as config_file:
        all_config = json.load(config_file)
        ebay_config = all_config.get("ebay").get("token_info")

    expiry_time = datetime.strptime(ebay_config.get("token_expiry"), date_format)
    current_time = datetime.now(UTC)
    if expiry_time < current_time or force_new_token:
        if mint_ebay_token(ebay_config):
            print("New access token minted")

            # rewrite config file with new token
            all_config["ebay"]["token_info"] = ebay_config
            with open("api_config.json", "w") as config_file:
                config_file.write(json.dumps(all_config))
        else:
            print("Couldn't acquire access token. Sorry!")
            return -1

    return ebay_config.get("token")

def ebay_search(item_name="Naruto", num_items=10, force_new_token = False):
    token = get_ebay_token(force_new_token)
    if token == -1:
        return []
    with open("api_config.json", 'r') as config_file:
        all_config = json.load(config_file)
    search_info = all_config.get("ebay").get("search_info")
    search_reponse = requests.get(search_info.get("url"),
                                  params={"q": item_name, "limit": num_items},
                                  headers=search_info.get("headers")|{"Authorization": f'Bearer {token}'})
    if search_reponse.status_code == 200:
        search_dict = json.loads(search_reponse.content)
        if not search_dict.get("itemSummaries"):
            print("Oh, we couldn't get any search results for this particular item... weird.")
            return []

        all_items = []
        for elem in search_dict.get("itemSummaries"):
            item = []
            item.append(elem.get("title"))
            item.append(elem.get("itemWebUrl"))
            item.append(elem.get("image").get("imageUrl"))
            item.append([elem.get("price").get("value"), elem.get("price").get("currency")])
            item.append(elem.get("seller").get("feedbackScore"))
            item.append(elem.get("seller").get("feedbackPercentage"))
            all_items.append(item)
        return all_items
    else:
        print("Sorry! I couldn't search on Ebay!!")
        return []

def shop_search(shop_name = "ebay", item_name="Naruto", num_items=10, force_new_token = False):
    return ebay_search(item_name, num_items, force_new_token)

def elegant_print(item_list):
    for item in item_list:
        print("Item Name:", item[0])
        print("Item Link:", item[1])
        print("Item image link:", item[2])
        print("Item price:", item[3][0], item[3][1])
        print("Seller Feedback Score:", item[4])
        print("Item Feedback Percentage:", item[5] + '%')
        print("="*50)


if __name__ == "__main__":
    elegant_print(shop_search(item_name="sudan", num_items=20))