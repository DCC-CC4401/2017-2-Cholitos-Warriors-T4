from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ComplaintView.as_view(), name='complaint-form'),
    url(r'^send', ComplaintSendView.as_view(), name='make-complaint'),
    url(r'^(?P<pk>\d+)/$', ComplaintRenderView.as_view(), name='see-complaint'),
    url(r'^act/(?P<pk>\d+)/$', ComplaintActState.as_view(), name='act-complaint'),
]
