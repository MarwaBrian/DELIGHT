from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User


class Caakes(models.Model):
    Image = models.ImageField(default='default.jpg', upload_to='home/marwa254/Desktop/DELIGHT/mysite/delight_Cakehouse/images')
    cake_type = models.TextField(blank=True, null=True)
    availability = models.IntegerField(blank=True, null=True)
    Best_Before = models.DateTimeField(default=timezone.now)
    in_stock = models.BooleanField('in stock')


"""     def __str__(self): 
        return self.cake_type()  
 """
class Cookies(models.Model):
    cookie_flavor = models.CharField(max_length=100)
    available_stock = models.BooleanField()