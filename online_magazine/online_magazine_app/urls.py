from django.urls import path
from online_magazine_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/',views.login, name = 'login')
]

