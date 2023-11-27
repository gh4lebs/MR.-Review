from django import forms
from .models import *
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# movie add form


class MovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse_lazy("index")
        self.helper.form_method = 'POST'

    class Meta:
        model = Movie
        fields = ('name', 'director', 'cast',
                  'description', 'release_date', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')
