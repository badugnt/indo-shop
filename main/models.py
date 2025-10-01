import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES =[
        ('jersey', 'Jersey'),
        ('shoes', 'Football Shoes'),
        ('ball', 'Football'),
        ('equipment', 'Training Equipment'),
        ('accessories', 'Accessories'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)              
    price = models.IntegerField()                        
    description = models.TextField()                     
    thumbnail = models.URLField()                        
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='accessories')  
    is_featured = models.BooleanField(default=False)     
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    @property
    def formatted_price(self):
        return f" {self.price:,}".replace(',', '.')

