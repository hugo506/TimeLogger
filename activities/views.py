from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    if request.user.is_authenticated():
        return render(request, "activities/index.html", {'name' : 'Prakhar'})
    return redirect('/admin/')
