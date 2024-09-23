from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

def about_us(request):
    return HttpResponse("About us")
def contact(request):
    return HttpResponse("Contact")
