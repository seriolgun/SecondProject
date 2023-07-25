from django.shortcuts import render
from.models import *
# Create your views here.
def index(request):
    ogrenciler=Ogrenci.objects.all()
    context={
        'ogrencilerim':ogrenciler

    }
    return render(request,'index.html',context)

def detail (request,ogrenciId):
    ogrenci=Ogrenci.objects.get(id=ogrenciId)
    context= {
        'ogrencim':ogrenci
        
    }
    print(ogrenci)
    return render(request, 'detay.html',context)