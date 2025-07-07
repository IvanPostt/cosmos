from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RegisterTestCase(TestCase):
    def test_reg(self):
        path = reverse('users:registrations')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registrations.html')
