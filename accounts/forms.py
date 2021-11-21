
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name', 'name': 'first_name', 'id': ''})
        
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name', 'name': 'last_name', 'id': ''})
        
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name', 'name': 'first_name', 'id': ''})
        
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name', 'name': 'last_name', 'id': ''})
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Address', 'name': 'Address', 'id': ''})
        
      
