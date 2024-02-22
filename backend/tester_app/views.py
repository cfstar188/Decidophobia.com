from django.shortcuts import render
from shop_search.search_engine import search_engine, elegant_print


# Create your views here.
def tombo_view(request, item):
    search_result = search_engine({"item": item})
    return render(request, "tomboTemplate.html", {"search_result": search_result})
