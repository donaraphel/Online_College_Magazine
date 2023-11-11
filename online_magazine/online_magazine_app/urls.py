from django.urls import path
from online_magazine_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/',views.login, name = 'login'),
    path('publish/<str:user_id>/',views.publish, name = 'publish'),
    path('search/', views.search, name='search'),
    path('myarticle/<str:user_id>/',views.myarticle, name = 'myarticle'),
    path('add_like/', views.add_like, name='add_like'),
    ]

