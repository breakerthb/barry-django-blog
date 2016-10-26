# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from forms import UploadFileForm

from django.template import RequestContext

# Create your views here.

import os
import json
from django.conf import settings

from django.http import HttpResponseRedirect

stat = {'status':False,'data':None,'msg':None}
def upload_file(request):
  if request.method == 'POST':
     form = UploadFileForm(request.POST, request.FILES)
     if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponse(json.dumps(stat))
  else:
     form = UploadFileForm()
  return render(request, 'upload.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    img_path = os.path.join(settings.MEDIA_URL, f.name)
    destination = open(img_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    

