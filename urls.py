from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib.auth.views import login, logout

from upload.users.views import user_profile

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^$', 'views.homepage'),
	('^upload/(file)$|^upload/(image)$', 'upload.files.views.upload'),
	(r'^file/(\w+)/(\d+)$', 'upload.files.views.fileinfo', {'image_or_file': 'file'}),
	(r'^image/(\w+)/(\d+)$', 'upload.files.views.fileinfo', {'image_or_file': 'image'}),
	('^about/$', direct_to_template, {'template': 'static/about.html'}),
	('^contact/$', direct_to_template, {'template': 'static/contact_us.html'}),
	(r'^accounts/login/$',  login),
	(r'^accounts/logout/$', logout),
	(r'^accounts/profile/$', user_profile),
	(r'^accounts/profile/edit/(\w+)/$', 'upload.users.views.edit_profile'),
)