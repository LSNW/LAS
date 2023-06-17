from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
import os, random, string

from .models import AVFile, LoaderReq, ServiceRecord
from .forms import SplitForm, LoaderForm
from . import handler

def home(request):
    return render(request, 'split\\home.html')

def split(request):
    if request.method == 'POST':
        form = SplitForm(request.POST, request.FILES)
        if form.is_valid():
            formData = form.cleaned_data
            audioFile = formData['avfile']
            times = formData['times']
            titles = formData['titles']
            extension = formData['fileType']
            fileName = formData['fileName']
            tag = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

            fileNameData = audioFile.name.split('.')
            fileName = ''.join(fileNameData[:-1])
            extension = fileNameData[-1]

            if (request.user.is_authenticated):
                record = ServiceRecord(filename=fileName, filetype=extension, user=request.user, timestamps=formData['timestamps'])
            else:
                record = ServiceRecord(filename=fileName, filetype=extension, timestamps=formData['timestamps'])
            record.save()

            if extension == 'wav':
                handler.trimWAV(audioFile, times, titles, tag)
            elif extension == 'mp3':
                audioFile.name = tag + ".mp3"
                saveFile = AVFile(avfile = audioFile)
                saveFile.save()
                handler.trimMP3(audioFile.name, times, titles, tag)
                saveFile.delete()
                os.remove(os.path.join('media', 'uploads', audioFile.name))

            return redirect('download', tag=tag)
            
    else:
        form = SplitForm()
    return render(request, 'split\\ss-tool.html', {'form': form})


def download(request, tag):
    return FileResponse(open(os.path.join("media", "tempzips",'SS-' + tag + '.zip'), 'rb'), filename = 'SSArchive.zip')

def loaderdl(request):
    return render(request, 'split\\loaderdl.html')

def about(request):
    return render(request, 'split\\about.html')