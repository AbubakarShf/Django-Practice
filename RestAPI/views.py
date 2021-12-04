from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':"Abubakar"})
def add(request):
    res=int(request.GET['Number1'])+int(request.GET['Number2'])
    return render(request,'result.html',{'result':res})