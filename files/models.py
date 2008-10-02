from django.db import models
from django.contrib.auth.models import User

class UploadedObject(models.Model):
	user = models.ForeignKey(User)
	created = models.DateField(auto_now_add=True)
	
	class Meta:
		abstract = True
	def __unicode__(self):
		return "file created %s by %s" % (self.created, self.user)

class UploadedImage(UploadedObject):
	filedata = models.ImageField(upload_to='%d/%m/%Y')

class UploadedFile(UploadedObject):
	filedata = models.FileField(upload_to='%d/%m/%Y')