from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("você chegou no protao de casa")

def sala(request):
    return HttpResponse("você chegou na sala,senta no sofá")

def quarto(request):
    return HttpResponse("agora esta no quarto ,deita na cama")

def post_list(request):
    return render(request, 'blog/post_list.html', {})

