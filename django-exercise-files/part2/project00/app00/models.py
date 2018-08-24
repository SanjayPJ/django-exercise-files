from django.db import models

# Create your models here.

class user_detail(models.Model):

    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)    
    address = models.CharField(max_length=500)
    website_url = models.URLField(max_length=200)

    def __str__(self):
        full_name = self.first_name + " " + self.last_name 
        return full_name
