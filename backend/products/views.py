from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# - create new object
# - get all objects (list)
class ListCreateProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# - update object
# - get single object
# - delete object
class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
