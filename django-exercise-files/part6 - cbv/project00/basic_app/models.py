from django.db import models

# Create your models here.

class School(models.Model):
    """Model definition for School."""

    name = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        """Unicode representation of School."""
        return self.name

class Student(models.Model):

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students" ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


