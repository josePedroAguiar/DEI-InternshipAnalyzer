from django.test import TestCase, RequestFactory
from ..forms import ReviewForm


class ReviewFormScenario(TestCase):

    def test_review_form(self):
        form = ReviewForm(data={'rating': 5, 'review': 'Great company!'})
        self.assertTrue(form.is_valid())
    def test_review_form_invalid(self):
        form = ReviewForm(data={'rating': 11, 'review': 'Great company!'})
        self.assertFalse(form.is_valid())
        form = ReviewForm(data={'rating': 5})
        self.assertFalse(form.is_valid())
        form = ReviewForm(data={'review': 'Great company!'})
        self.assertFalse(form.is_valid())
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())