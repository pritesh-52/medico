from django.shortcuts import render
from django.http import  HttpResponse
from  .models import Patient
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method=='POST':
        obj = Patient(name=request.POST["name"], email=request.POST["email"],phone=request.POST["phone"],
                     date=request.POST["date"],message=request.POST["message"])
        obj.save()
        messages.success(request, 'Data wil be submitted successfully')
        return render(request,'index.html')
    return render(request, 'index.html')


def employee(request):
    return  HttpResponse("Employee Page")

def about(request):
    return  HttpResponse("About us page")

