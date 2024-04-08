from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView
from .views import CustomerListCreateAPIView, CustomerDetailAPIView
from .views import BillingListCreateAPIView, BillingDetailAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('billing/', BillingListCreateAPIView.as_view(), name='billing-list-create'),
    path('billing/<int:pk>/', BillingDetailAPIView.as_view(), name='billing-detail'),
]

# from django.urls import path
# from .views import (
#     ProductListCreateAPIView,
#     ProductDetailAPIView,
#     CustomerListCreateAPIView,
#     CustomerDetailAPIView,
#     BillingListCreateAPIView,
#     BillingDetailAPIView,
# )
#
# urlpatterns = [
#     # Product URLs
#     path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
#
#     # Customer URLs
#     path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list'),
#     path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
#
#     # Billing URLs
#     path('billing/', BillingListCreateAPIView.as_view(), name='billing-list'),
#     path('billing/<int:pk>/', BillingDetailAPIView.as_view(), name='billing-detail'),
# ]
#
