from django.shortcuts import render, redirect
from activities.models import AuthorInfo, Category, Activity
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

settings.LOGIN_REDIRECT_URL = "/"
settings.LOGIN_URL = "/login"

@login_required
def index(request):
    results = Activity.objects.filter(author__username=request.user.username)
    context = { 'name' : request.user.username, 'results' : results}
    return render(request, "activities/index.html", context)

@login_required
def add_activity(request):
    return render(request, "activities/add.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
