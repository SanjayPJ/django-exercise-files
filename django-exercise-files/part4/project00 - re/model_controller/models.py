from django.db import models

# Create your models here.

class Staff(models.Model):
    """Model definition for Staff."""

    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    url = models.URLField( max_length=200)
    
    def __str__(self):
        """Unicode representation of Staff."""
        return self.name
