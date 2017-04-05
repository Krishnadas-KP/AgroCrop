from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.statewelcomepage , name='statewelcomepage'),
    url(r'^rates', views.setRates , name='setRates'),
    url(r'^update', views.RateUpdater , name='RateUpdater'),
    url(r'^confirm', views.Confirmation , name='Confirmation'),
    url(r'^transport', views.transport , name='transport'),
    url(r'^allocate', views.StockAllocate , name='StockAllocate'),
    url(r'^deleteUser', views.deleteUser , name='deleteUser'),
    url(r'^addlocal', views.addLocal , name='addLocal'),
    url(r'^additem', views.addItem , name='addItem'),
   
    
]
