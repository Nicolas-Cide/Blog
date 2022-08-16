from django.shortcuts import render
from appFamily.models import familiaPrinc

# Create your views here.

def home(request):

    info = familiaPrinc.objects.all()
    return render(request,'home.html',{'info':info})
