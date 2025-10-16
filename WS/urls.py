# Import ur urls here

from django.contrib import admin
from django.urls import path

from WS.views import HomeView, ShopView

urlpatterns = [
    path('', HomeView.as_view(), name='greetings_page'),
    path('store/', ShopView.as_view(), name='main_store_page'),
    # path('search/', SearchView.as_view(), name='search_page'),
    # path('order/', OrderView.as_view(), name='order_page'),
    # path('bike_description/', BikeView.as_view(), name='bike_description_page')
    
]
