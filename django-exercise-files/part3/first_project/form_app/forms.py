from django import forms

class Sample(forms.Form):
    """Sample definition."""

    # TODO: Define form fields here

    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
