from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'), #in order to mach the HOME PAGE we leave the first '' empty
]