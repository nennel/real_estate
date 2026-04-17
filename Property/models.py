from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    location  = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name


