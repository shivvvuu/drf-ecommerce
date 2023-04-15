from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSeriallizer(serializers.ModelSerializer):
    brand = BrandSeriallizer()
    category = CategorySeriallizer()

    class Meta:
        model = Product
        fields = "__all__"
