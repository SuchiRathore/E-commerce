from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),
)    

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='producting')
    
    def __str__(self):
        return str(self.id)
# Create your models here.
    
class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE) 
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)   
    
