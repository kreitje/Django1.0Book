from django.conf.urls.defaults import patterns, include, url
from bookmarks.views import *
import os

static_content = os.path.join(os.path.dirname(__file__), 'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	#url(r'^polls/', include('polls.urls')),
	url(r'^$', index),
	url(r'^bookmarks/', include('bookmarks.urls')),
	url(r'^user/(\w+)/$', user_page),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static_content}),
    
    # Examples:
    # url(r'^$', 'jeff.views.home', name='home'),
    # url(r'^jeff/', include('jeff.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
