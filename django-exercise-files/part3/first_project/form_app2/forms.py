from django import forms

class DEMO_FORM2(forms.Form):
    """DEMO_FORM2 definition."""

    # TODO: Define form fields here

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    address_1 = forms.CharField( widget=forms.Textarea, required=True)
    address_2 = forms.CharField( widget=forms.Textarea, required=False)
    website = forms.URLField(required=False)
    pin = forms.IntegerField(required=False)
