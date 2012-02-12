# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
	return render_to_response('main.html', RequestContext(request))
	
def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		raise Http404(u'Requested user not found.')
		
	bookmarks = user.bookmark_set.all()
	

	variables = RequestContext(request, {
		'username': username,
		'bookmarks': bookmarks
	})
	
	return render_to_response('bookmarks/user_page.html', variables);

	
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
	