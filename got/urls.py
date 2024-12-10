from django.urls import path
from got.views import *


urlpatterns = [
    path('blue/',blue,name='blue'),
]