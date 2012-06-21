"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HttpTest(TestCase):
    def test_contacts(self):
        c = Client()
        response = c.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        self.assertContains(response, 'Stanislav')
        self.assertContains(response, 'Matsevich')
        self.assertContains(response, '28.02.1986')
        self.assertContains(response, 'Email: matsevich.devel@gmail.com')
        self.assertContains(response, 'Jabber: matsevich.devel@gmail.com')
        self.assertContains(response, 'Skype: matsevich.devel')