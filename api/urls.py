from math import prod
from django.urls import path
from api.views import products_view

urlpatterns = [
    path('products/', products_view),
]
