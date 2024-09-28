from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Leo',
    })
# não é preciso informar que ele está na pasta de templates
# o django automaticamente reconhece isso

def about_us(request):
    return render(request, 'recipes/about_us.html')

def contact(request):
    return render(request, 'me-apague/temp.html')