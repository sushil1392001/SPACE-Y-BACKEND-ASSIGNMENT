from rest_framework import generics
from .models import Product, Customer, Billing
from .serializers import ProductSerializer, CustomerSerializer, BillingSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BillingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer


class BillingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

'''
Products: GET /api/products/, POST /api/products/, GET /api/products/<id>/, PUT /api/products/<id>/, DELETE /api/products/<id>/
Customers: GET /api/customers/, POST /api/customers/, GET /api/customers/<id>/, PUT /api/customers/<id>/, DELETE /api/customers/<id>/
Billing: GET /api/billing/, POST /api/billing/, GET /api/billing/<id>/, PUT /api/billing/<id>/, DELETE /api/billing/<id>/
'''