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
        
    def test_request_html(self):
        """
        Tests that html-page contents all stored data of request and shows 
        info about last 10 requests
        """
        c = Client()
        response = c.get(reverse('requests'), REMOTE_ADDR='123.45.67.89', 
                         SERVER_PROTOCOL='HTTP/1.0', HTTP_REFERER='http://r0/',
                         HTTP_USER_AGENT='Test: resp0')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123.45.67.89')
        self.assertContains(response, 'HTTP/1.0')
        self.assertContains(response, 'GET')
        self.assertContains(response, reverse('requests'))
        self.assertContains(response, 'http://r0/')
        self.assertContains(response, response.status_code)
        self.assertContains(response, response.tell())
        self.assertContains(response, 'Test: resp0')
        # OK. All firlds are present. 
        # Now test that a few requests are shown
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp1')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp2')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp3')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp4')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp5')
        self.assertContains(response, 'Test: resp0')
        self.assertContains(response, 'Test: resp1')
        self.assertContains(response, 'Test: resp2')
        self.assertContains(response, 'Test: resp3')
        self.assertContains(response, 'Test: resp4')
        self.assertContains(response, 'Test: resp5')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp6')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp7')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp8')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp9')
        response = c.get(reverse('requests'), HTTP_USER_AGENT='Test: resp10')
        # 'Test: resp0' must be displaced        
        self.assertNotContains(response, 'Test: resp0')
        