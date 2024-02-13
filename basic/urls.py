from django.urls import path
from . import views

urlpatterns = [
    path("compute/<int:value>", views.compute, name="compute"),
]