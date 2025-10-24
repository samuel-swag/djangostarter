from django.db import models

# Create your models here.

class Response(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    button1 = models.TextField()
    button2 = models.TextField()
    button3 = models.TextField()
    latency1 = models.FloatField(null=True, blank=True)
    latency2 = models.FloatField(null=True, blank=True)
    latency3 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return (f"Responsre at {self.timestamp}")

