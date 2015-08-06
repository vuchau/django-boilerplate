from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms.forms import NON_FIELD_ERRORS


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

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
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(SigninForm, self).is_valid()

        if not valid:
            return valid

        user = authenticate(**self.cleaned_data)
        if not user:
            self._errors[NON_FIELD_ERRORS] = 'The username/email and password were incorrect.'
            valid = False

        if user and not user.is_active:
            self._errors[NON_FIELD_ERRORS] = 'The password is valid, but the account is inactive.'
            valid = False

        return user if valid else False


class UserEditForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.EmailField()

    def is_valid(self, current_user_id):
        valid = super(UserEditForm, self).is_valid()

        if not valid:
            return valid

        try:
            User.objects.get(
                ~Q(id=current_user_id),
                Q(username=self.cleaned_data['username'])
            )
            self._errors['username'] = 'User with this username already exists.'
            valid = False
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(
                ~Q(id=current_user_id),
                Q(email=self.cleaned_data['email'])
            )
            self._errors['email'] = 'User with this email already exists.'
            valid = False
        except User.DoesNotExist:
            pass

        return valid


class UserPasswordEditForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def is_valid(self, user):
        valid = super(UserPasswordEditForm, self).is_valid()

        if not valid:
            return valid

        if not user.check_password(self.cleaned_data['old_password']):
            self._errors['old_password'] = 'Current password is invalid.'
            valid = False

        if self.cleaned_data['new_password1'] != self.cleaned_data['new_password2']:
            self._errors['new_password1'] = 'New passwords don\'t match.'
            valid = False

        return valid
