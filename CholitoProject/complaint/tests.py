from django.test import TestCase
from django.contrib.auth.models import User
from municipality.models import Municipality, MunicipalityUser
from .models import *
from .forms import *

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from naturalUser.models import NaturalUser

# Create your tests here.

class ComplaintsTests(TestCase):

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
        Municipality.objects.create(name="DummyBun", lat=-70.5957, lng=-33.5903, directions="somewhere else", avatar=None)
        MunicipalityUser.objects.create(user=User.objects.get(username="dummy2@gmail.com"), municipality=Municipality.objects.get(name="DummyBun"))
        AnimalType.objects.create(name='Conejo')
        AnimalType.objects.create(name='Gato')
        AnimalType.objects.create(name='Perro')

    def test_complaint_on_correct_Municipality(self):
        complaint_1_data = {
            'case':3,
            'animal_type':AnimalType.objects.get(name='Conejo').id,
            'gender':2,
            'color':'Blanco',
            'wounded':False,
            'directions':'Por ahi',
            'lat':-33.5903,
            'lng':-70.5957,
            'description':'Es hermosa',
            'municipality':Municipality.objects.get(name="DummyBunny").id
        }
        form = ComplaintForm(data=complaint_1_data)
        self.assertTrue(form.is_valid())
