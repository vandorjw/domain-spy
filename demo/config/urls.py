"""Urls for the demo of domain-spy"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.http import HttpResponse
from django.views.static import serve
from django.views.defaults import bad_request
from django.views.defaults import server_error
from django.views.defaults import page_not_found
from django.views.defaults import permission_denied

urlpatterns = [
    url(r'^$', lambda request: HttpResponse('Hello World!'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('domainspy.urls')),
]

urlpatterns += [
    url(r'^400/$', bad_request),
    url(r'^403/$', permission_denied),
    url(r'^404/$', page_not_found),
    url(r'^500/$', server_error),
]
