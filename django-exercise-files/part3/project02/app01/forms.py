from django import forms
from app00.models import User

class CreateUserFormForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"
