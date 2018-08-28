from django import forms
from model_controller.models import Staff

class StaffForm(forms.ModelForm):

    def clean_name(self):
        raise forms.ValidationError("oh yea")
    
    
    class Meta:
        model = Staff
        fields = "__all__"
