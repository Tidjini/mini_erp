
from django.test import TestCase

from .models import Product


class ProductTestCase(TestCase):

    def test_fields(self):

        product = Product.objects.create(
            name="Product", qte_stock=123456789123.55)

        self.assertEqual(product.name, "Product")
