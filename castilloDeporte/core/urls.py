from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('carrito/', views.cart, name='cart'),
    path('search', views.ProductSearchListView.as_view(), name='search'),
    # path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
    # path('agregar', views.add, name='add')
]