from django.forms import ModelForm

from models import UploadedFile, UploadedImage

class UploadedFileForm(ModelForm):
	class Meta:
		model = UploadedFile
		fields = ('filedata',)
		
class UploadedImageForm(ModelForm):
	class Meta:
		model = UploadedImage
		fields = ('filedata',)