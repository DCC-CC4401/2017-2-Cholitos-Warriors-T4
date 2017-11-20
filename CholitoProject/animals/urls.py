from django.conf.urls import url

from animals.views import AnimalRenderView, AdoptView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AnimalRenderView.as_view(), name='see-animal'),
    url(r'^adopt/$', AdoptView.as_view(), name='adopt')
]