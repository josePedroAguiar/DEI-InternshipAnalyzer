from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    company = models.CharField(max_length=255)
    logo = models.TextField(null=True)
    description = models.TextField(null=True)
    requirements = models.TextField(null=True)
    duration = models.IntegerField()  # in weeks
    location = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def average_rating(self):
        return self.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']

    def __str__(self):
        return self.company


class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 1 to 10 scale
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.title} - {self.user.username}"

    #def rating(self, value):
    #    if not isinstance(value, int):
    #        raise ValueError("Age must be an integer")
    #    elif value < 1 or value > 10:
    #         raise ValueError("Rating must be between 1 and 10")
    #    self.rating = value

