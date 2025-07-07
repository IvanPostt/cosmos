from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import SpaceObj


# Create your tests here.
class MainTest(TestCase):
    def setUp(self):
        pass

    def test_case1(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        #self.assertIn('main/index.html', response.template_name)
        #self.assertEqual(response.context_data['title'], 'Home')

    def test_redirect(self):
        path = reverse('createpost')
        redirect_url = reverse('users:login') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_url)

    def test_data(self):
        a = SpaceObj.objects.all().select_related('category')
        path = reverse('index')
        response = self.client.get(path)
        self.assertQuerySetEqual(response.context_data['posts'], a[:2])

    def test_paginator(self):
        path = reverse('index')
        page = 2
        paginate_by = 5
        response = self.client.get(path + f'?page={page}')
        a = SpaceObj.objects.all().select_related('category')
        self.assertQuerySetEqual(response.context_data['posts'], a[(page-1) *paginate_by:page * paginate_by])
    def tearDown(self):
        pass