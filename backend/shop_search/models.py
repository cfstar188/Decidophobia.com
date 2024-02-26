from django.db import models


# Create your models here.
class SearchInfo(models.Model):
    shop_name = models.TextField(primary_key=True)
    base_url = models.URLField()
    request_headers = models.JSONField(null=True)


class AuthInfo(models.Model):
    shop_name = models.TextField(primary_key=True)
    token = models.TextField(null=True)
    token_expiry = models.DateTimeField(null=True)
    mint_url = models.URLField(null=True)
    request_headers = models.JSONField(null=True)
    request_body = models.JSONField(null=True)
