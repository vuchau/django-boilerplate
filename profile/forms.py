from django import forms
from django.contrib.auth.models import User
from django.db.models import Q


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
