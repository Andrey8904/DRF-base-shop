from rest_framework import generics
from .serializers import MySerializers
from .models import Product


class MainView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = MySerializers




