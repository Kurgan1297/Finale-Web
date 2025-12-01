
from django.shortcuts import render
from django.views.generic import View

from django.core import paginator

from BW.models import Bikes
from BW.forms import FilterForm


class ShopView(View):
    def get(self, request):

        form = FilterForm()

        bike_type = self.request.GET.get("bike_type", None)

        if bike_type is None:
            all_bikes = Bikes.objects.all()
        else:
            all_bikes = Bikes.objects.filter(bike_type=bike_type)

        bikes_p = paginator.Paginator(all_bikes, 9)
        page_now = request.GET.get("page")
        page_bikes = bikes_p.get_page(page_now)

        return render(request, 'store.html', context={
            "all_bikes": page_bikes,
            "filter_form": form
        })

    def post(self, request):
        return render(request, 'store.html')
    
class HomeView(View):
    def get(self, request):
        return render(request, 'greetings.html')
    
    def post(self, request):
        return render(request, "greetings.html")


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
    def post(self, request):
        return render(request, "about.html")
    

class DescitptionView(View):
    def get(self, request, bikeid):

        bike_info = Bikes.objects.filter(id=bikeid).last()
        print(bike_info)        

        return render(request, "bike_page.html", context={"bike_info":bike_info})

    def post(self, request):
        # bike_name = request.POST.get("bike_name")
        # bike_name = request.POST.get("bike_name")

        pass