from django.urls import path
from .view.product_view import ProductListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]