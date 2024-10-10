from django.test import TestCase
from django.urls import reverse, resolve, NoReverseMatch
from estagioapps.views import *

class TestUrls(TestCase):

    def test_internship_list_url(self):
        url = reverse('internship_list')
        self.assertEqual(resolve(url).func, internship_list)

    def test_internship_detail_url(self):
        url = reverse('internship_detail', args=[1])
        self.assertEqual(resolve(url).func, internship_detail)

    def test_add_review_url(self):
        url = reverse('add_review', args=[1])
        self.assertEqual(resolve(url).func, add_review)

    def test_remove_review_url(self):
        url = reverse('remove_review', args=[1,1])
        self.assertEqual(resolve(url).func, remove_review)

    def test_edit_review_url(self):
        url = reverse('edit_review', args=[1,1])
        self.assertEqual(resolve(url).func, edit_review)

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_nonexistent_url(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('nonexistent_url')
            self.assertEqual(resolve(url).func)

    def test_internship_detail_url_with_invalid_args(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('internship_detail', args=['invalid_arg'])
            self.assertEqual(resolve(url).func, internship_detail)


# Run the test with the following command: python manage.py estagioapps