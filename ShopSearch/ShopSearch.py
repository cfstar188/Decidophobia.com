import requests
import json
from datetime import datetime, UTC, timedelta

token_mint_body = {"ebay": {"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"}}
def shop_search(item_name, num_items):

def get_token():
    with open("api_config.json", 'r') as config_file:
        config = json.load(config_file)

    expiry_time = datetime.strptime(config.get("last_gen"), "%Y/%m/%d %H:%M:%S")
    current_time = datetime.now(UTC)
    if expiry_time < current_time:
        token = mint_token(config)
        config["token_expiry"] = datetime.now() +
        print("New access token minted")
    else:
        token = config.get("token")
def mint_token(config):
    token_response = requests.post(config.get("url"), data=token_mint_body.get("ebay"),
                               headers={"Content-Type": config.get("Content-Type"),
                                        "Authorization": config.get("token_auth")})
    token_details = json.loads(token_response.content)
    config["token_expiry"] = datetime.now() + token_details.get("expires_in")
