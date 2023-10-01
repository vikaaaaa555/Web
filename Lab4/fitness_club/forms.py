from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'Name not entered'
        self.fields['last_name'].empty_label = 'Last name not entered'
        self.fields['rating'].empty_label = "You didn't rate"
        self.fields['feedback'].empty_label = "You haven't left a review"

    def clean_feedback(self):
        feedback = self.cleaned_data['feedback']

        if len(feedback) <= 0:
            raise ValidationError('Feedback has not been entered')

        return feedback

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) <= 0:
            raise ValidationError('Name not entered')

        return name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if len(last_name) <= 0:
            raise ValidationError('Last name not entered')

        return last_name

    class Meta:
        model = Feedback
        fields = ['name',
                  'last_name',
                  'rating',
                  'feedback']
