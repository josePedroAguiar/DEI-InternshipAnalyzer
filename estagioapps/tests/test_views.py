from django.test import TestCase, Client
from django.urls import reverse, resolve, NoReverseMatch
from estagioapps.views import *
import json


from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.test import TestCase
class TestViews(TestCase):
    def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='12345')
            self.client = Client()
            self.client.login(username='testuser', password='12345')

    def test_internship_detail_url(self):
            url = reverse('internship_detail', args=[1])
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'internships/internship_detail.html')

    #GET
    def test_home_url(self):
        url = reverse('home')
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'internships/home.html')

    def test_internship_list_url(self):
        url = reverse('internship_list')
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'internships/internship_list.html')

    def test_internship_detail_url(self):
        url = reverse('internship_detail', args=[1])
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 302)

    #POST
    def test_review_form_scenario_handles_no_input(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())

    def test_review_form_scenario_handles_valid_input(self):
        form = ReviewForm(data={'rating': 5, 'review': 'Great product!'})
        self.assertTrue(form.is_valid())

    def test_review_form_scenario_rejects_invalid_rating(self):
        form = ReviewForm(data={'rating': 11, 'review': 'Great product!'})
        self.assertFalse(form.is_valid())

    def test_review_form_scenario_rejects_missing_review(self):
        form = ReviewForm(data={'rating': 5})
        self.assertFalse(form.is_valid())