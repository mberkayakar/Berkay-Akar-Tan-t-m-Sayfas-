from typing import Optional
from django import template
from django.shortcuts import render
 
from .models import Yetenekler, projeler,İsDeneyimi,Summary,KisiselBilgiler,badget,ozellikler,ProfilFotografı,Egitimler
from django.template import loader
from django.http import HttpResponse, response

# Create your views here.
def mainpage(request):
    yetenekler = Yetenekler.objects.all()
    deneyim = İsDeneyimi.objects.all()
    ozet=Summary.objects.all()
    kisiselbilgiler=KisiselBilgiler.objects.all()
    projelerim=projeler.objects.all()
    rozet=badget.objects.all()
    özellikler=ozellikler.objects.all()
    profilpotografı=ProfilFotografı.objects.all()
    egitimler= Egitimler.objects.all()

    context={"yetenekler":yetenekler,"deneyim":deneyim,"ozet":ozet,
    "kisiselbilgiler":kisiselbilgiler,"projeler":projelerim,"rozet":rozet,
    "özellikler":özellikler,"profilpotografı":profilpotografı,"egitimler":egitimler}
    return render(request,"CV.html",context)