from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'name' : 'Prakhar'}
    return render(request, "activities/index.html", context)

def detail(request, owner):
    return HttpResponse("My lucky number is %s" % owner)

def author_add(request):
    return render(request, "activities/add_author.html")
