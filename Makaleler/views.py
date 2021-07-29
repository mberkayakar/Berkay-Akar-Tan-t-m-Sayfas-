from typing import Optional
from django import template
from django.shortcuts import render
 
from .models import Yazılar
from django.template import loader
from django.http import HttpResponse, response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def mainpage(request):
    yazılar_listesi = Yazılar.objects.all()
    paginator=Paginator(yazılar_listesi,5)
    page = request.GET.get("page")
    try:
        yazılar=paginator.page(page)
    except PageNotAnInteger:
        yazılar=paginator.page(1)
    except EmptyPage:
        yazılar=paginator.page(paginator.num_pages)
    context={"yazılar":yazılar}
    return render(request,"bloggenel.html",context)