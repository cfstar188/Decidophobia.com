from django.urls import path
from . import views

# URLConfigs
urlpatterns = [
    path('messages/', views.messageBoard),
    path('testReq/', views.requestTest),
    path('testo/', views.htmlAndCssTest),
]