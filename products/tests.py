from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.auth_model import UserAuthentication
from products.products_model import ProductModel
from common import constants as ct

class ProductTests(APITestCase):

    def setUp(self):
        self.user_auth = UserAuthentication.objects.create(user_name='testuser', password='password123')
        self.client.force_authenticate(user=self.user_auth)
        
        # Sample product data
        self.product_data = {
            "product_id": "P001",
            "product_name": "Test Product",
            "product_description": "This is a test product",
            "product_price": 100,
            "product_quantity": 10,
            "product_units": "pcs"
        }

    def test_add_product(self):
        response = self.client.post(reverse('add_product'), self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(ct.MESSAGE, response.data)

    def test_add_product_already_exists(self):
        ProductModel.objects.create(**self.product_data)
        response = self.client.post(reverse('add_product'), self.product_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(ct.ERROR, response.data)

    def test_get_products_list(self):
        ProductModel.objects.create(**self.product_data)
        response = self.client.get(reverse('get_products_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data)
        self.assertEqual(len(response.data['data']), 1)

    def test_update_product(self):
        product = ProductModel.objects.create(**self.product_data)
        update_data = {
            ct.PRODUCT_NAME: "Updated Product"
        }
        response = self.client.put(reverse('product_details', args=[product.product_id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(ct.MESSAGE, response.data)

        # Verify the product was updated
        product.refresh_from_db()
        self.assertEqual(product.product_name, "Updated Product")

    def test_delete_product(self):
        product = ProductModel.objects.create(**self.product_data)
        response = self.client.delete(reverse('product_details', args=[product.product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(ct.MESSAGE, response.data)

        # Verify the product was deleted
        self.assertFalse(ProductModel.objects.filter(product_id=product.product_id).exists())

    def test_get_product_details(self):
        product = ProductModel.objects.create(**self.product_data)
        response = self.client.get(reverse('product_details', args=[product.product_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[ct.DATA][ct.PRODUCT_NAME], self.product_data[ct.PRODUCT_NAME])

    def test_get_product_details_not_found(self):
        response = self.client.get(reverse('product_details', args=['invalid_id']))  # Non-existing ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(ct.ERROR, response.data)
