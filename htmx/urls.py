from django.urls import path

from . import views

app_name="htmx"

urlpatterns = [
    path("demo", views.demo, name="demo"),
    path('oneimage/', views.oneimage, name='oneimage'),
    path("answer", views.answer, name="answer"),
    path("answer1", views.answer1, name="answer1"),
    
]