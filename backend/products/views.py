from rest_framework import generics, views
from .models import Product
from .serializers import MockSerializer, ProductSerializer
from rest_framework.response import Response


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


# http://127.0.0.1:8000/api/products/mock/
# {
#   "name": "asd",
#   "price": 100.23
# }
class MockAPIView(views.APIView):
    def post(self, request, *args, **kwatgs):
        serializer = MockSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            # OrderedDict([('name', 'asd'), ('year', Decimal('100.23'))])
            print(serializer.data)
            # {'name': 'asd', 'year': '100.23'}
            return Response(serializer.validated_data)
