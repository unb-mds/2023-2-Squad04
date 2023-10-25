from django.shortcuts import render

def licitacao(request):
    return render(request, 'licitacao.html')

def home(request):
    return render(request, 'index.html')

def equipe(request):
    return render(request, 'equipe.html')

def sobre(request):
    return render(request, 'sobre.html')
