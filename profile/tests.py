from .forms import SignupForm, ProfileEditForm
from django.test import Client
from django.test import TestCase


class TestSignup(TestCase):
    def test_signin(self):
        form = SignupForm({
            'email': 'foo@bar.com',
            'password': '123'
        })
        self.assertTrue(form.is_valid())
        form.save()

        c = Client()
        response = c.post('/profile/signin', {
            'username': 'foo@bar.com',
            'password': '123'
        })
        self.assertEqual(response.status_code, 302)
        response = c.get('/dashboard')
        self.assertEqual(response.status_code, 200)

        response = c.get('/profile/signout')
        self.assertEqual(response.status_code, 302)
        response = c.get('/dashboard')
        self.assertEqual(response.status_code, 302)

        response = c.post('/profile/signin', {
            'username': 'foo@bar.com',
            'password': '456'
        })
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        form = SignupForm({
            'email': 'foo@bar.com',
            'password': '123'
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.email, 'foo@bar.com')
        self.assertTrue(user.check_password('123'))

        form = SignupForm({
            'email': '',
            'password': '123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

        form = SignupForm({
            'email': 'foo@bar.com',
            'password': '123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'User with this Email address already exists.')

        form = SignupForm({
            'email': 'foo@bar.com',
            'password': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'][0], 'This field is required.')

    def test_user_edit(self):
        form = SignupForm({
            'email': 'bar@baz.com',
            'password': '123'
        })
        form.is_valid()
        form.save()

        form = SignupForm({
            'email': 'foo@bar.com',
            'password': '123'
        })
        form.is_valid()
        user = form.save()

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com'
        }, instance=user)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.get_full_name(), 'foo bar')
        self.assertEqual(user.email, 'foo@bar.com')

        form = ProfileEditForm({
            'first_name': '',
            'last_name': 'bar',
            'email': 'foo@bar.com'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

        form = ProfileEditForm({
            'first_name': '',
            'last_name': '',
            'email': 'foo@bar.com'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'bar@baz.com'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'User with this Email address already exists.')

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com',
            'old_password': '456'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['old_password'][0], 'Old password is incorrect.')

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com',
            'old_password': '123'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['new_password1'][0], 'New password cannot be empty.')

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com',
            'old_password': '123',
            'new_password1': '456',
            'new_password2': '789'
        }, instance=user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['new_password1'][0], 'New passwords must match.')

        form = ProfileEditForm({
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com',
            'old_password': '123',
            'new_password1': '456',
            'new_password2': '456'
        }, instance=user)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(user.check_password('456'))
