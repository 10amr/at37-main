from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('Demand/', Demand, name='Demand'),
    path('Demand/', Demand,name='Demand'),
    path('Geography/', Geography,name='Geography'),
    path('Skills/', Skills,name='Skills'),
    path('Latest_vacancies/', Latest_vacancies,name='Latest_vacancies'),
]
