from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Leo',
    })
# não é preciso informar que ele está na pasta de templates
# o django automaticamente reconhece isso

def about_us(request):
    return render(request, 'recipes/about_us.html')