from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSeriallizer, CategorySeriallizer, ProductSeriallizer

# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySeriallizer)
    def list(self, requst):
        serializer = CategorySeriallizer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing brand
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSeriallizer)
    def list(self, request):
        serializer = BrandSeriallizer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing product
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSeriallizer)
    def list(self, request):
        serializer = ProductSeriallizer(self.queryset, many=True)
        return Response(serializer.data)
