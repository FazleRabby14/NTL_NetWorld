from django.db import models

# Create your models here.
class contactInfo(models.Model):
        first_name=models.CharField(max_length=25)
        last_name=models.CharField(max_length=25)
        email=models.CharField(max_length=40)
        phone_number=models.CharField(max_length=25)
        message=models.CharField(max_length=200)
        
def __str__(self):
        return self.first_name + ' ' + self.last_name