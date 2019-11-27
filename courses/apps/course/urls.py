from django.conf.urls import url
from . import views


urlpatterns=[
  url(r'^$', views.home),
  url(r'^course/add$', views.add),
  url(r'^delete/(?P<desc_id>\d+)$', views.delete),
]