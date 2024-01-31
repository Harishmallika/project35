from django.shortcuts import render

# Create your views here.


def userfilter(request):
    d={'data':'How are you All'}
    return render(request,'userfilter.html',d)
