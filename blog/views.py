from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("Vocẽ chegou ao portao da casa")

def sala(request):
    return HttpResponse("Vocẽ chegou na sala,sneta no sofa")

def quarto(request):
    return HttpResponse("agora está no quarto,pode se deitar")

def opendoorsom(request):
    return HttpResponse("show Armandinho,12,13 opendoor")

def post_list(request):
    return render(request, 'blog/post_list.html', {})