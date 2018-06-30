from django.test import TestCase
from django.test import Client
import unittest

class SimpleTest(unittest.TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_200_shop(self):        
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        
    def test_404_shop(self):      
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 404)

    def test_200_cart(self):        
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_200_order_create(self):        
        response = self.client.get('/order/create/')
        self.assertEqual(response.status_code, 200)          



class SimpleTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_NO_Redirect(self):
        response = self.client.get('/cart/')
        self.assertRedirects(response, ('/cart/detail/'), status_code=302,
                         target_status_code=200, msg_prefix=('msg_prefix'),
                         fetch_redirect_response=True)

    def test_Contains(self):
        response = self.client.get('/shop/')
        self.assertContains(response, ('абв'), count=0,
                            msg_prefix='абв', html=False)
