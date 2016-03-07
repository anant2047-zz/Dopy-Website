from django.conf.urls import url
from services.views import *

urlpatterns = [
	url(r'^$', services,name='services'),
    url(r'^photography$', photography, name='photography'),
    url(r'^advertising$', advertising, name='advertising'),
    url(r'^weddings$', weddings, name='weddings'),
]
