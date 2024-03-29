from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from bookmarks.views import *
import os

static_content = os.path.join(os.path.dirname(__file__), 'static')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	#url(r'^polls/', include('polls.urls')),
	
	# Browsing
	url(r'^$', index),
	url(r'^bookmarks/', include('bookmarks.urls')),
	url(r'^user/(\w+)/$', user_page),
	url(r'^tag/$', tag_cloud_page),
	url(r'^tag/([^\s]+)/$', tag_page),
	url(r'^search/$', search_page),
	
	# Account Management
	url(r'^save/$', bookmark_save_page),
	
	# Admin access
    url(r'^admin/', include(admin.site.urls)),

	# Session Management
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^register/$', register_page),
	url(r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),
	
	# Static content
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static_content, 'show_indexes': True}),
    
    # Examples:
    # url(r'^$', 'jeff.views.home', name='home'),
    # url(r'^jeff/', include('jeff.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
