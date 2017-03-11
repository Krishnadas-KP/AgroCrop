from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.welcomepage , name='welcomepage'),
    url(r'^rlogic', views.reglogic , name='reglogic'),
    url(r'^rates', views.rates , name='rates'),
    



]
