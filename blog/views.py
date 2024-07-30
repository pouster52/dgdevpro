from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("Você chegou ao portão da casa")

def post_list(request):
    return render(request, 'blog/post_list.html', {})