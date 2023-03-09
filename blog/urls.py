from django.urls import path
from . import views

#URL CONFIGURATION
urlpatterns = [
    path('hello/', views.hello)
]