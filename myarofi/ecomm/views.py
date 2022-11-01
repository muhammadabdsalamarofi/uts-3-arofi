from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    datamap = {
        'data':1000,
        'coba':"uji coba"
    }
    return render(request,'index.html',datamap)
