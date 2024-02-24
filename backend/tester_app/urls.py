from django.urls import re_path
from .views import tombo_view

urlpatterns = [
    re_path(r"^(?P<item>[\w-]*)/$", tombo_view, name="da_tombo_url")
]
