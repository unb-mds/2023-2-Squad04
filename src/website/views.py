from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def equipe(request):
    return render(request, 'equipe.html')
