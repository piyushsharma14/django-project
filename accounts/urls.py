from django.conf.urls import url
from . import views
from django.urls import path 
from django.contrib.auth.models import auth

urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('',views.login,name="login"),
    path('logout',views.logout, name="logout"),
]