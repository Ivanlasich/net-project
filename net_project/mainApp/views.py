from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainApp/homePage.html')
# Create your views here.
def about(request):
    return render(request, 'mainApp/documentation.html')

def contacts(request):
    return render(request, 'mainApp/contacts.html')
