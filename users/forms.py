from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from .models import Profile

User = get_user_model()


class UserRegisterForm(SignupForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')

    def save(self, request):
        user = super(UserRegisterForm, self).save(request)
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.save()
        return user
    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
