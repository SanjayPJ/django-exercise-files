from django import forms

class User(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField( required=False)
    url = forms.URLField(required=False)

    # def clean_name(self):
    #     data = self.cleaned_data["name"]
    #     if len(data) > 0:
    #         raise forms.ValidationError("gotcha")
    #     return data
    
    def clean(self):
        clean_val = super().clean()
        raise forms.ValidationError("ohh yea")