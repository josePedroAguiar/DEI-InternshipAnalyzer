from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #rating should be between 1 and 10
        fields = ['rating','review']  # Adjust fields as needed

        def clean_rating(self):
            rating = self.cleaned_data.get('rating')
            if rating < 1 or rating > 10:
                raise forms.ValidationError("Rating must be between 1 and 10")
            return rating