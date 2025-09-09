from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)              
    price = models.IntegerField()                        
    description = models.TextField()                     
    thumbnail = models.URLField()                        
    category = models.CharField(max_length=50)           
    is_featured = models.BooleanField(default=False)     
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

