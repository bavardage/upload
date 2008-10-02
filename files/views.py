from forms import UploadedFileForm, UploadedImageForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import UploadedFile, UploadedImage
import mimetypes
@login_required
def upload(request, upload_file=None, upload_image=None):
	if not (upload_file or upload_image):
		raise Http404
	elif upload_file:
		formClass = UploadedFileForm
		redir = 'file'
		is_image = False
	else:
		formClass = UploadedImageForm
		redir = 'image'
		is_image = True
		
	if request.method == 'POST': # If the form has been submitted...
		form = formClass(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			new_file = form.save(commit=False)
			new_file.user = request.user
			new_file.save()
			request.user.message_set.create(message='File uploaded successfully')
			return HttpResponseRedirect('../%s/info/%s' % (redir, new_file.id))
	else:
		form = formClass()
	return render_to_response("files/upload.html", RequestContext(request, {'form': form, 'image': is_image }))

@login_required
def fileinfo(request, info_thumb_file, fileid, image_or_file):#image_or_file, success_id):
	if image_or_file == 'image':
		model = UploadedImage
		image = True
	else:
		model = UploadedFile
		image = False
	fileobject = model.objects.get(id=fileid)
	mimetype = mimetypes.guess_type(fileobject.filedata.path)[0]
	if info_thumb_file == 'file':
		image_data = fileobject.filedata.file.read()
		return HttpResponse(image_data, mimetype=mimetype)
	elif info_thumb_file == 'info':
		return render_to_response("files/file_info.html", RequestContext(request, {'file': fileobject, 'mimetype': mimetype, 'image': image}))
	else:
		raise Http404