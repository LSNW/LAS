from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import os


class AVFile(models.Model):
    avfile = models.FileField(upload_to='uploads')
    timestamps = models.TextField()

    def filename(self):
        return os.path.basename(self.file.name)

class LoaderReq(models.Model):
    url = models.TextField()
    format = models.TextField()

class ServiceRecord(models.Model):
    #service = models.CharField(max_length=25)
    filename = models.CharField(max_length=250)
    filetype = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    timestamps = models.TextField(default="None")

    def __str__(self):
        return self.filename
