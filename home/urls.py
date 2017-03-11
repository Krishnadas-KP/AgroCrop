from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.welcomepage , name='welcomepage'),
    url(r'^rlogic', views.reglogic , name='reglogic'),
    url(r'^rates', views.rates , name='rates'),
    url(r'^contact', views.model_form_upload , name='model_form_upload'),



]
