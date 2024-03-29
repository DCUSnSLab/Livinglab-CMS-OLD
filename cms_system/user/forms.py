from .models import CustomUser
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserAdditionalSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nickname', 'user_description', 'user_auth', 'user_profile']

