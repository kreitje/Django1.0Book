from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bookmarks.views',
	url(r'^$', 'index'),
)