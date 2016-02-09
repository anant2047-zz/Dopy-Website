from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings

from .forms import UploadFileForm
from .models import UploadFile

def gallerylist(request):
    list_items=[]
    for i in UploadFile.objects.all():
    	list_items.append(i.event_name)
    list_items.sort(reverse=True)
    context={
    "items":list_items,
    }

    return render(request,'gallerylist.html',context)