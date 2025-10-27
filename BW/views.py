
from django.shortcuts import render
from django.views.generic import View

from django.core import paginator

from BW.models import Bikes



class ShopView(View):
    def get(self, request):

        #

        all_bikes = Bikes.objects.all()
        bikes_p = paginator.Paginator(all_bikes, 5)
        page_now = request.GET.get("page")
        page_bikes = bikes_p.get_page(page_now)

        return render(request, 'store.html', context={
            "all_bikes": page_bikes
        })

    def post(self, request):
        return render(request, 'store.html')
    
class HomeView(View):
    def get(self, request):
        return render(request, 'greetings.html')
    
    def post(self, request):
        return render(request, "greetings.html")

class DescitptionView(View):
    def get(self, request):
        
        


        return render(request, "bike_page.html")

    def post():
        pass    