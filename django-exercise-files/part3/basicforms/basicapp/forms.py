from django import forms

class FormName(forms.Form):
    # TODO: Define form fields here
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)
	