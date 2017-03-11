from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.statewelcomepage , name='statewelcomepage'),
    url(r'^rates', views.setRates , name='setRates'),
    url(r'^update', views.RateUpdater , name='RateUpdater'),
    
]
