from django import forms

class Demo(forms.Form):

    # TODO: Define form fields here

    username = forms.CharField( max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 5:
            raise forms.ValidationError("Username must be less than 6 charecters")
        else:
            return username
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) > 5:
            raise forms.ValidationError("Password must be less than 6 charecters")
        else:
            return password
    def clean(self):
        clean_d = super().clean()
        username = clean_d['username']
        password = clean_d['password']
        if username in password:
            raise forms.ValidationError("Username and Password must be different")