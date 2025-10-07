from django.urls import path
from . import views

app_name="basic"

urlpatterns = [
    path("compute/<int:value>", views.compute, name="compute"),
    path("isprime/<int:value>", views.isPrime, name="isPrime"),
    
]