from django.db import models

# Create your models here.

class County(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name

class Hotel(models.Model):
	name = models.CharField(max_length=30,default='hotel')
	daily_cost = models.DecimalField(max_digits=6,decimal_places=2)
	county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="hotel_location")
	address = models.CharField(max_length=30)
	image = models.ImageField(upload_to="hotels")

	def __str__(self):
		return self.name

class Attraction(models.Model):
	county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="attraction_location")
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=1000)
	image = models.ImageField(upload_to="attractions")
	hotel = models.ManyToManyField(Hotel, related_name="attraction_hotels")
	

	def __str__(self):
		return self.name

