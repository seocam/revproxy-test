from django.conf.urls import patterns, include, url
from django.contrib import admin

from proxyapp.views import TestProxyView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proxy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<path>.*)$', TestProxyView.as_view()),
)
