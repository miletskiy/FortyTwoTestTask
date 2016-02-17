
from django.conf.urls import patterns, url

from apps.hello import views

urlpatterns = patterns(
    '',
    url(r'^$', views.contacts, name='contacts'),
    url(r'^requests/', views.requests_list, name='requests'),
    url(r'^edit_applicant/', views.edit_applicant, name='edit_applicant'),
)
