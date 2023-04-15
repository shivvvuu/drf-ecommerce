from pytest_factoryboy import register

from .factories import BrandFactory, CategoryFactory, ProductFactory

register(CategoryFactory)

register(BrandFactory)
register(ProductFactory)
