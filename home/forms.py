
from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control col-sm-6', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
                               
                               

                               
class RegForm(forms.Form):
    
    Aadhaar = forms.CharField(label="Aadhaar", max_length=12,
                                 widget=forms.TextInput(attrs={'name': 'Aadhaar'}))
    Name = forms.CharField(label = "Name" , widget=forms.TextInput(attrs = {'name' : 'Name'}))
    Address = forms.CharField(label = "Address" , widget=forms.Textarea(attrs = {'name' : 'Address'}))
    mobNum = forms.CharField(label = "Mobile Number" ,max_length=10, widget = forms.TextInput(attrs = {'name' : 'mobNum'}))
    ACnum = forms.CharField(label = "Account Number" ,max_length=16,widget = forms.TextInput(attrs = {'name' : 'ACnum'}))
    Bank = forms.CharField(label = "Bank Name" ,max_length=16,widget = forms.TextInput(attrs = {'name' : 'Bank'}))
    IFSC = forms.CharField(label = "IFS Code" ,max_length=16,widget = forms.TextInput(attrs = {'name' : 'IFSC'}))
    
 




