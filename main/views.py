from django.shortcuts import render
from django.http import HttpResponse
from main.tasks import document_length

# Create your views here.

def celery_task(request):
    url = "http://baidu.com"
    t = document_length.delay(request.GET.get("tt"))
    print t, type(t)
    return HttpResponse("tt")