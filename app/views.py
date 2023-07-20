from django.shortcuts import render

# Create your views here.


def usdp(request):
    d={'data':'How Are You'}
    return render(request,'usdf.html',d)
