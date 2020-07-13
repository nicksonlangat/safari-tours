from django.urls import path
from .views import HomePageView, HotelList, AttractionList, HotelDetail, AttractionDetail 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hotels', HotelList.as_view(), name='hotels'),
    path('attractions', AttractionList.as_view(), name='attractions'),
    path('hotel/<int:pk>/', HotelDetail.as_view(), name='hotel_detail'),
    path('attraction/<int:pk>/', AttractionDetail.as_view(), name='attraction_detail'),
]