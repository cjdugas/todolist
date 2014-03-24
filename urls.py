from django.conf.urls import patterns, url

from core import views


urlpatterns = patterns('',
  #ex: /lists/
  url(r'^$', views.IndexView.as_view(), name='index'),
  #ex: /lists/2
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
