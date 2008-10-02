
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from files.models import UploadedFile, UploadedImage

import os.path

def homepage(request):
	images = UploadedImage.objects.order_by("-created")[:3]
	files = UploadedFile.objects.order_by("-created")[:3]
	for fileobject in files:
		 fileobject.basename = os.path.basename(fileobject.filedata.name)
	print images
	print files
	return render_to_response("home.html", RequestContext(request, {'images': images, 'files': files}))