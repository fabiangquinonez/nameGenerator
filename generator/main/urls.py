from django.urls import path
from . import views


#url paths for the different pages necessary, using functions defined in views.py
urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('create-post', views.create_post, name = 'create_post'),
    path('feed', views.feed, name = 'feed'),
    path('profile', views.profile, name = "profile"),

]