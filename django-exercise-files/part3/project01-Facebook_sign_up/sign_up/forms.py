from django import forms
import re

class SignUpPage(forms.Form):
    """SignUpPage definition."""

    # TODO: Define form fields here

    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=20, required=True)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not(re.match('[A-z]+', first_name)):
            raise forms.ValidationError("First Name must be less than 6 charecters")
        else:
            return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) > 5:
            raise forms.ValidationError("Last Name must be less than 6 charecters")
        else:
            return last_name