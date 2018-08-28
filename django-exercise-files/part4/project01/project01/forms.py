from django import forms

class Demo(forms.Form):
    """Demo definition."""

    name = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) > 0:
            raise forms.ValidationError("Gotcha manh")
        return data
    