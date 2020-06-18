from django import forms
from .models import User_Details
class User_DetailsForm(forms.ModelForm):
    class Meta:
        model = User_Details
        fields = "__all__"