from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.localwelcomepage , name='localwelcomepage'),
    url(r'^buy', views.buyvegetables , name='buyvegetables'),
    url(r'^sell', views.sellvegetables , name='sellvegetables'),
    url(r'^rates', views.checkrates , name='checkrates'),
    url(r'^transportOut', views.transport, name='transport'),
    url(r'^transportIn', views.transportIn, name='transportIn'),
    url(r'^verify', views.verification , name='verification'),
    url(r'^pending', views.pendingReceive , name='pendingReceive'),
    url(r'^vsearch', views.search_users_verify , name='search_users_verify'),
    
    url(r'^amtfind', views.amtfinder , name='amtfinder'),
    url(r'^polling', views.pollingData , name='pollingData'),
    url(r'^colFarmItem', views.CollectFarmerItems , name='CollectFarmerItems'),
    
]
