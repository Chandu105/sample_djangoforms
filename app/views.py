from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djangoforms(request):
    ENFO=NameForm()
    d={'ENFO':ENFO}

    if request.method=='POST':
        FDFO=NameForm(request.POST)
        if FDFO.is_valid():
            return HttpResponse(str(FDFO.cleaned_data))
        else:
            return HttpResponse('data is invalid')
     



    return render(request,'djangoforms.html',d)