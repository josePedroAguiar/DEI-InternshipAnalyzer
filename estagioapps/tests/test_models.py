from django.test import TestCase
from django.urls import reverse, resolve, NoReverseMatch
from estagioapps.models import *



class ModelsViews(TestCase):

    def setUp(self):
        self.internship = Company.objects.create(
            title='Internship 1',
            description='Internship 1 description',
            company='Company 1',
            location='Location 1',
            salary=1000.00
        )

        self.review = Review.objects.create(
            internship=self.internship,
            rating=5,
            review='Great company!'
        )
