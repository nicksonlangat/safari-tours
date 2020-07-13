from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	return render(request, "home.html")

def hotels(request):
	hotels=Hotel.objects.all()
	return render(request, "index.html",{"hotels":hotels})

def places(request):
	places=Attraction.objects.all()
	return render(request, "places.html",{"places":places})
	
