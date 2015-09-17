from django import forms
from django.contrib.auth.forms import AuthenticationForm
from profile.models import User


class ResetPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
    new_password1 = forms.CharField(widget=forms.PasswordInput({'required': True}), required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput({'required': True}), required=False)

    def is_valid(self):
        valid = super(ResetPasswordForm, self).is_valid()

        if not valid:
            return valid

        if self.cleaned_data['new_password1'] != self.cleaned_data['new_password2']:
            self._errors['new_password1'] = 'Passwords must match.'
            valid = False

        return valid

    def save(self):
        user = super(ResetPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data['new_password1'])
        user.save()
        return user


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'required': 'true'}))


class SigninForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'required': True})
        self.fields['password'].widget.attrs.update({'required': True})


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
            'password': forms.PasswordInput(attrs={'required': True})
        }

    def is_valid(self):
        valid = super(SignupForm, self).is_valid()

        if not valid:
            return valid

        try:
            User.objects.get(email=self.cleaned_data['email'])
            self._errors['email'] = ['User with this email already exists.']
            valid = False
        except User.DoesNotExist:
            pass

        return valid

    def save(self):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
        }
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def is_valid(self):
        valid = super(ProfileEditForm, self).is_valid()

        if not valid:
            return valid

        user = self.instance

        validate_passwords = False
        if self.cleaned_data['old_password']:
            validate_passwords = True
            if not user.check_password(self.cleaned_data['old_password']):
                self._errors['old_password'] = ['Old password is incorrect.']
                valid = False

        if validate_passwords and valid:
            #   old password is correct
            if not self.cleaned_data['new_password1']:
                self._errors['new_password1'] = ['New password cannot be empty.']
                valid = False

        if validate_passwords and valid:
            #   new password is not empty
            if self.cleaned_data['new_password1'] != self.cleaned_data['new_password2']:
                self._errors['new_password1'] = ['New passwords must match.']
                valid = False

        return valid

    def save(self):
        user = super(ProfileEditForm, self).save(commit=False)
        if self.cleaned_data['new_password1']:
            user.set_password(self.cleaned_data['new_password1'])
        user.save()
        return user
