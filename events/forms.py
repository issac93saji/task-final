from django import forms
from events.models import UserProfile,Contact,Comments
from django.contrib.auth.models import User

from events.models import UserProfile,Contact


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('title','profile_image')

class UserForm2(forms.Form):

    email=forms.EmailField(required=True)
    username=forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    title=forms.CharField(required=True)
    profile_pic=forms.ImageField(required=False)
    class Meta:
        fields = ('username', 'email', 'password','title','profile_pic',)


class ContactForm(forms.ModelForm):
    mail=forms.EmailField(label="E-mail id  ")
    data=forms.CharField(label="Message  ",widget=forms.Textarea(attrs={'cols': 20, 'rows': 5}))
    class Meta:
        model = Contact
        fields= ['mail','data',]