import os
import django

# Setting up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decidophobia.settings')
django.setup()

from shop_search.models import AuthInfo, SearchInfo

def insert_auth_search_info():
    # Insert eBay AuthInfo
    ebay_auth, created = AuthInfo.objects.get_or_create(
        shop_name="ebay",
        defaults={
            "mint_url": "https://api.ebay.com/identity/v1/oauth2/token",
            "request_headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic QWhtZWRNb2gtZGVjaWRvcGgtUFJELWMxZTJiYjU2My1mNDFlNDRkMzpQUkQtMWUyYmI1NjNlZmRmLTBmMTktNDU1Yy1iMDZlLTNlNmUgDQo="
            },
            "request_body": {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope"
            }
        }
    )
    print(f"eBay AuthInfo {'created' if created else 'updated'}.")

    # Insert eBay SearchInfo
    ebay_search, created = SearchInfo.objects.get_or_create(
        shop_name="ebay",
        defaults={
            "base_url": "https://api.ebay.com/buy/browse/v1/item_summary/search",
            "request_headers": {"X-EBAY-C-MARKETPLACE-ID": "EBAY_US"}
        }
    )
    print(f"eBay SearchInfo {'created' if created else 'updated'}.")

    # Insert BestBuy AuthInfo
    bestbuy_auth, created = AuthInfo.objects.get_or_create(
        shop_name="bestbuy",
        defaults={
            "token": "a6xmm2a2athgchfhkwuv8vpq"
        }
    )
    print(f"BestBuy AuthInfo {'created' if created else 'updated'}.")

    # Insert BestBuy SearchInfo
    bestbuy_search, created = SearchInfo.objects.get_or_create(
        shop_name="bestbuy",
        defaults={
            "base_url": "https://api.bestbuy.com/v1/products"
        }
    )
    print(f"BestBuy SearchInfo {'created' if created else 'updated'}.")

if __name__ == '__main__':
    insert_auth_search_info()