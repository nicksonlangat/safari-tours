from django.urls import path
from . import views
urlpatterns = [
    path('hotels',views.hotels, name="hotels"),
    path('places',views.places, name="places"),
]