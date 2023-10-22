"""
Definition of urls for mattepapper.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import papperapp.views
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
	#example stuff:
    url(r'^$', papperapp.views.home, name='home'),
    url(r'^mul_decimal$', papperapp.views.mul_decimal, name='mul_decimal'),
    url(r'^div_decimal$', papperapp.views.div_decimal, name='div_decimal'),
    url(r'^add_exponent$', papperapp.views.add_exponent, name='add_exponent'),
    url(r'^equation$', papperapp.views.equation, name='equation'),
    #url(r'^$', papperapp.views.mult, func=testFunc, name='test'),
    #eller är det en dålig idé? Ska skillnaden mellan olika dok ligga i urlpatterns eller i views?
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
