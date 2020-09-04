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
    url(r'^mult$', papperapp.views.mult, name='mult'),
    url(r'^frac$', papperapp.views.frac, name='frac'),
    url(r'^add_exponents$', papperapp.views.add_exponents, name='add_exponents'),
    url(r'^equations$', papperapp.views.equations, name='equations'),
    #url(r'^$', papperapp.views.mult, func=testFunc, name='test'),
    #eller är det en dålig idé? Ska skillnaden mellan olika dok ligga i urlpatterns eller i views?
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
