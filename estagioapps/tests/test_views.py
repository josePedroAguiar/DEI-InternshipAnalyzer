from django.test import TestCase, Client
from django.urls import reverse, resolve, NoReverseMatch
from estagioapps.views import *
import json


class TestViews(TestCase):

    #GET
    def test_home_url(self):
        url = reverse('home')
        client = Client()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

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
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'internships/internship_detail.html')

    #POST
    def test_review_form_scenario_handles_no_input(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())

    def test_review_form_scenario_handles_valid_input(self):
        form = ReviewForm(data={'review': 'Great product!', 'rating': 5})
        self.assertTrue(form.is_valid())

    def test_review_form_scenario_rejects_invalid_rating(self):
        form = ReviewForm(data={'review': 'Great product!', 'rating': 6})
        self.assertFalse(form.is_valid())

    def test_review_form_scenario_rejects_missing_review(self):
        form = ReviewForm(data={'rating': 5})
        self.assertFalse(form.is_valid())