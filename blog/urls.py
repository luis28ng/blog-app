from django.urls import path
from . import views

#URL CONFIGURATION
urlpatterns = [
    path('', views.home, name="Home Page"),
    path('signup/', views.signup, name="Sign Up"),
    path('login/', views.login, name="Login"),
]