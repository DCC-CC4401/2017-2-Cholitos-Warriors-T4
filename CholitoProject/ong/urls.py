from django.conf.urls import url

from ong.views import *
app_name = 'ong'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ONGforNaturalUser.as_view(), name='ong-logged'),
]
