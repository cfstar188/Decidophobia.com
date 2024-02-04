import requests
import json
from datetime import datetime, UTC, timedelta

import pytz

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
    with open("api_config.json", 'r') as config_file:
        all_config = json.load(config_file)
        ebay_config = all_config.get("ebay")

    expiry_time = datetime.strptime(ebay_config.get("token_expiry"), date_format)
    current_time = datetime.now(UTC)
    if expiry_time < current_time or force_new_token:
        if mint_ebay_token(ebay_config):
            print("New access token minted")

            # rewrite config file with new token
            all_config["ebay"] = ebay_config
            with open("api_config.json", "w") as config_file:
                config_file.write(json.dumps(all_config))
        else:
            print("Couldn't acquire access token. Sorry!")
            return -1

    return ebay_config.get("token")


def shop_search(shop_name = "ebay", item_name="Naruto", num_items="10", force_new_token = False):
    token = get_ebay_token(force_new_token)
    if token == -1: return []



if __name__ == "__main__":
    shop_search(force_new_token=True)
