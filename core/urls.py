from django.contrib import admin
from django.urls import re_path, include
from .views import home
urlpatterns = [
    re_path('', home, name='core_home'),
]
