# Import ur urls here

from django.contrib import admin
from django.urls import path

from BW.views import HomeView, ShopView, AboutView, DescitptionView

urlpatterns = [
    path('', HomeView.as_view(), name='greetings_page'),
    path('store/', ShopView.as_view(), name='main_store_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('bike_page/<int:bikeid>', DescitptionView.as_view(), name='bike_page'),
    # path('search/', SearchView.as_view(), name='search_page'),
    # path('order/', OrderView.as_view(), name='order_page'),

]
