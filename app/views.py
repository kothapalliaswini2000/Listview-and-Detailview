from django.shortcuts import render

from app.models import *
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.


class Home(TemplateView):
    template_name='app/Home.html'

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


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'



