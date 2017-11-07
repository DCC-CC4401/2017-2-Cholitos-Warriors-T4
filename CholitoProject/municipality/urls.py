from django.conf.urls import url
from municipality.views import IndexView, UserDetail, StatisticsView


urlpatterns = [
    url(r'^user/$', UserDetail.as_view()),
    url(r'^$', IndexView.as_view(), name='municipality-index'),
    url(r'^statistics$', StatisticsView.as_view(), name='complaint-statistics'),
]
