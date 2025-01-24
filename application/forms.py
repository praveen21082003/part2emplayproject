from django import forms
from application.models import register
from application.models import login
class registerForm(forms.ModelForm):
    name = forms.CharField(label="Full Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    age = forms.IntegerField(label="Age")
    phone = forms.CharField(label="Phone Number", max_length=15, required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", max_length=50)
    class Meta:#contains model,fields
        model = register
        fields=('name','email','age','phone','password','confirm_password')

class loginForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=50)
    class Meta:#contains models,fields
        model = login
        fields=('email','password')