from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.districtwelcomepage , name='districtwelcomepage'),
    url(r'^transport', views.transport , name='transport'),
    url(r'^allocate', views.StockAllocate , name='StockAllocate'),
    
    
]
