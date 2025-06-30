from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("voce chegou ao portao da casa")

def sala(request):
    return HttpResponse("voce chegou na sala,senta no sofa")

def quarto(request):
    return HttpResponse("agora esta no quarto vai varre")

def post_list(request):
    return render(request, 'blog/post_list.html', {})
