from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

def Home(request):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(request, 'app/pages/Home.html', context=data)

def info(request):
     data = {
         'Demand': Statistic.objects.get(id=1)
     }
     return render(request, 'app/app/Demand.html', context=data)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def Demand(request):
     return render (request, 'app/pages/Demand.html')
def Geography(request):
     return render (request, 'app/pages/Geography.html')
def Latest_vacancies(request):
     return render (request, 'app/pages/Latest_vacancies.html')
def Skills (request):
     return render (request, 'app/pages/Skills.html')