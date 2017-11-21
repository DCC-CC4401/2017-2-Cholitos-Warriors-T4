from django.test import TestCase
from django.contrib.auth.models import User
from municipality.models import Municipality, MunicipalityUser
from .models import *
from .forms import *

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from .models import NaturalUser

# Create your tests here.

class NaturalUserTests(TestCase):

    def setUp(self):
        content_type = ContentType.objects.get_for_model(NaturalUser)
        permission = Permission.objects.create(
            codename='natural_user_access',
            name='Can Publish Posts',
            content_type=content_type,
        )

        content_type = ContentType.objects.get_for_model(MunicipalityUser)
        permission = Permission.objects.create(
            codename='municipality_user_access',
            name='Can Publish Posts',
            content_type=content_type,
        )

    def test_natural_user_permits(self):
        new_user_data = {
            'username': "david.natural@gmail.com",
            'email': "david.natural@gmail.com",
            'first_name': 'David',
            'last_name': 'Rojas',
            'password1': '1234asdf',
            'password2': '1234asdf'
        }

        form = SignUpForm(data = new_user_data)
        self.assertTrue(form.is_valid())
        new_user = form.save()
        NaturalUser.objects.create(user=new_user, avatar=False)

        user = User.objects.get(username="david.natural@gmail.com")
        self.assertTrue(user.has_perm('naturalUser.natural_user_access'))
        self.assertFalse(user.has_perm('municipality.municipality_user_access'))

    def test_natural_user_permits(self):
        new_user_data = {
            'username': "david.natural@gmail.com",
            'email': "david.natural@gmail.com",
            'first_name': 'David',
            'last_name': 'Rojas',
            'password1': '1234asdf',
            'password2': '1234asdf'
        }

        form = SignUpForm(data = new_user_data)
        self.assertTrue(form.is_valid())
        new_user = form.save()
        NaturalUser.objects.create(user=new_user, avatar=False)