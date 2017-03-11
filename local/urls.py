from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.localwelcomepage , name='localwelcomepage'),
    url(r'^buy', views.buyvegetables , name='buyvegetables'),
    url(r'^sell', views.sellvegetables , name='sellvegetables'),
    url(r'^rates', views.checkrates , name='checkrates'),
    url(r'^transport', views.transport, name='transport'),
    url(r'^verify', views.verification , name='verification'),
    url(r'^vsearch', views.search_users_verify , name='search_users_verify'),
    
    url(r'^amtfind', views.amtfinder , name='amtfinder'),
    url(r'^colFarmItem', views.CollectFarmerItems , name='CollectFarmerItems'),
    
]
