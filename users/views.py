from forms import UserForm, ProfileForm

from models import UserProfile

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect


@login_required
def user_profile(request):
	print request.user.is_authenticated()
	try:
		profile = request.user.get_profile()
	except:
		profile = UserProfile(user=request.user, distro_of_choice="Archlinux", irc_nickname="bavardage")
		profile.save()
	c = RequestContext(request, {})
	return render_to_response('users/profile.html', c)
@login_required
def edit_profile(request, edit_what):
	if edit_what not in ('profile', 'user'):
		raise Http404
	elif edit_what == 'user':
		formClass = UserForm
		formInstance = request.user
	else:
		formClass = ProfileForm
		formInstance = request.user.get_profile()
			
	if request.method == 'POST': # If the form has been submitted...
		form = formClass(request.POST,instance=formInstance) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			request.user.message_set.create(message='Profile Successfully Updated')
			return HttpResponseRedirect('../..')
	else:
		form = formClass(instance=formInstance)
	return render_to_response("users/profile_edit.html", RequestContext(request, {'form': form }))
