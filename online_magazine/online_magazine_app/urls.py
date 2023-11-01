from django.urls import path
from online_magazine_app import views

urlpatterns = [
    path('', views.hello_everyone, name='hello_everyone'),
]

