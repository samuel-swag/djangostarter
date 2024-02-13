from django.db import models

# Create your models here.

# Computed objects cache computations that were already performed
# A computation that has already been performed will not be performed again 
class Computed(models.Model):  
    input = models.IntegerField()
    output = models.IntegerField()


