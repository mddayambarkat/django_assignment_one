from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(rw):
    return HttpResponse("hii")


def help(request):
    dictinoary={'md':"Md dayam is a full stack webdeveloper"}
    return render(request,'help.html',context= dictinoary)
   