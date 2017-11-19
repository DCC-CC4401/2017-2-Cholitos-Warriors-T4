from django.conf.urls import url

from ong.views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ONGforNaturalUser.as_view(), name='ong-logged'),
]
