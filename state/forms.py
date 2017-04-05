from django import forms

from home.models import District

instance = District.objects.all()

class LocalAddForm(forms.Form):

    LName = forms.CharField(label="Local Center Name", max_length=30 )
                                 
    District = forms.ModelChoiceField(queryset = instance, empty_label="Select District")
    
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput())