from django.shortcuts import render

from app.models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
# Create your views here.

class Schoollist(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(sname='QSP') # HERE IF U WANT TO SEE ONLY SPECIFIC OBJECT ONLY
    #queryset=School.objects.all() # IF YOU WANT TO SEE ALL THE OBJECTS MEANS U CAN GO FOR ALL()
    #EXAMPLE LIKE QSP,JSP,PYSPD
    
    #ordering=['sname'] # BY USING ORDERING WE CAN INSERT OBJECTS INTO ALPHABETS OREDR
    

def wish(request,n):
    return HttpResponse(f'Hai {n} How are U')
    
class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'
