from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms.forms import NON_FIELD_ERRORS


class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(SignupForm, self).is_valid()

        if not valid:
            return valid

        try:
            User.objects.get(username=self.cleaned_data['username'])
            self._errors['username'] = 'User with this username already exists.'
            return False
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=self.cleaned_data['email'])
            self._errors['email'] = 'User with this email already exists.'
            return False
        except User.DoesNotExist:
            pass

        return True


class SigninForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(SigninForm, self).is_valid()

        if not valid:
            return valid

        user = authenticate(**self.cleaned_data)
        if not user:
            self._errors[NON_FIELD_ERRORS] = 'The username and password were incorrect.'
            return False

        if not user.is_active:
            self._errors[NON_FIELD_ERRORS] = 'The password is valid, but the account has been disabled!'
            return False

        return user
