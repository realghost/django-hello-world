"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from datetime import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_hello_world.requests.models import RequestInfo


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class RequestTest(TestCase):
    """Tests request module"""
    
    def test_request_middleware(self):
        """
        Tests that middleware registers requests and all stored fields are
        correct
        """ 
        c = Client()
        start = datetime.now()
        response = c.get('/not_existing_path/', REMOTE_ADDR='123.45.67.89', 
                          SERVER_PROTOCOL='HTTP/1.0', HTTP_REFERER='http://r',
                          HTTP_USER_AGENT='Test: response1')
        finish = datetime.now()
        last_request = RequestInfo.objects.latest()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(last_request.ip, '123.45.67.89')
        self.assertEqual(last_request.protocol, 'HTTP/1.0')
        self.assertEqual(last_request.method, 'GET')
        self.assertEqual(last_request.path, '/not_existing_path/')
        self.assertEqual(last_request.referer, 'http://r')
        self.assertEqual(last_request.response_status, response.status_code)
        self.assertEqual(last_request.response_tell, response.tell())
        self.assertEqual(last_request.user_agent, 'Test: response1')
        self.assertTrue(start<=last_request.datetime<=finish)
        