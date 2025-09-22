# Import ur urls here

from django.contrib import admin
from django.urls import path

from WS.views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='main_page'),
    path('store/', TestView.as_view(), name='main_store_page')
]
