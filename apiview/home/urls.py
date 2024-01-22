
from django.contrib import admin
from django.urls import path,include
from home.models import *
from .views import *

urlpatterns = [
  
    path('home/',home),
    path('student',student_api),

]
