from django import forms
from profile.models import User
from django.db.models import Q


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
            self._errors['email'] = 'User with this email already exists.'
            return False
        except User.DoesNotExist:
            pass

        return True

    def save(self):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()


class UserEditForm(forms.ModelForm):
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
        valid = super(UserEditForm, self).is_valid()

        if not valid:
            return valid

        user = self.instance
        try:
            User.objects.get(
                ~Q(id=user.id),
                Q(email=self.cleaned_data['email'])
            )
            self._errors['email'] = 'User with this email already exists.'
            valid = False
        except User.DoesNotExist:
            pass

        validate_passwords = False
        if self.cleaned_data['old_password']:
            validate_passwords = True
            if not user.check_password(self.cleaned_data['old_password']):
                self._errors['old_password'] = 'Old password is incorrect.'
                valid = False

        if validate_passwords and valid:
            #   old password is correct
            if not self.cleaned_data['new_password1']:
                self._errors['new_password1'] = 'New password cannot be empty.'
                valid = False

        if validate_passwords and valid:
            #   new password is not empty
            if self.cleaned_data['new_password1'] != self.cleaned_data['new_password2']:
                self._errors['new_password1'] = 'New passwords must match'
                valid = False

        return valid
