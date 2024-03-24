"""
URL configuration for decidophobia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import home, login, signup, logout, settings, change_password, questionnaire
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/register/', signup, name='signup'),
    # path('logout/', logout, name='logout'),
    path('settings/', settings, name='settings'),
    path('settings/change_password/', change_password, name='change_password'),
    path("", include("django_nextjs.urls")),
    path("table/", include("product_table.urls")),
    path("", include("django_nextjs.urls")),
    path('products/', include('products.urls')),
    path("search/", include("search_page.urls")),
    path('questionnaire/', questionnaire, name='questionnaire'),
    path('filter/', filter, name='filter' ),
    path('accounts/', include('users.urls')),
    path('shopping-list/', include('shopping_list.urls')),
    path('discussion_board/', include('discussionBoard.urls')),
    path('search_item/', include("tester_app.urls"))
]
