from django.test import TestCase
from django.contrib.auth.models import User
from .models import Municipality, MunicipalityUser

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from naturalUser.models import NaturalUser

# Create your tests here.

class MunicipalityTests(TestCase):

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
        User.objects.create_user("dummy@gmail.com")
        User.objects.create_user("dummy2@gmail.com")
        Municipality.objects.create(name="DummyBunny", lat=-33.5903, lng=-70.5957, directions="somewhere", avatar=None)
        MunicipalityUser.objects.create(user=User.objects.get(username="dummy@gmail.com"), municipality=Municipality.objects.get(name="DummyBunny"))

    def test_Permits(self):
        user = User.objects.get(username="dummy@gmail.com")
        self.assertTrue(user.has_perm('municipality.municipality_user_access'))
        user = User.objects.get(username="dummy2@gmail.com")
        self.assertFalse(user.has_perm('municipality.municipality_user_access'))