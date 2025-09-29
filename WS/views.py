
from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')
    
    def post(self, request):
        pass
    
class ShopView(View):
    def get(self, request):
        return render(request, 'main_store.html')
    

