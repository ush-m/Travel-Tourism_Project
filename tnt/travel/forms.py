from django import forms
from travel.models import user

class UserForm(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"