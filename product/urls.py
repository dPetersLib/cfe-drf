from django.urls import path
from .views import ProductDetailView, api_home, products_view

urlpatterns = [
    path('', products_view),
    path('<int:pk>/', ProductDetailView.as_view())
]
