from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from contact.models import Contact, Profile 

# user registration form
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

# contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = '__all__'

# frofile Form 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'