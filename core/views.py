from django.views.generic import ListView, DetailView, TemplateView 
from .models import *
# Create your views here.

class HomePageView(TemplateView):
	template_name ="home.html"
	
class AttractionList(ListView):
	model=Attraction
	template_name="attractions.html"
	
class HotelList(ListView):
	model=Hotel 
	template_name="hotels.html"
	
class HotelDetail(DetailView):
	model=Hotel 
	template_name="hotel.html"
	
class AttractionDetail(DetailView):
	model=Attraction
	template_name="attraction.html"
	
