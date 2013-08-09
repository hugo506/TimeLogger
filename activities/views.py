from django.shortcuts import render, redirect
from activities.models import AuthorInfo, Category, Activity
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from activities.forms import ContactForm, ActivityForm
from django.http import HttpResponseRedirect
from django.utils import timezone

settings.LOGIN_REDIRECT_URL = "/"
settings.LOGIN_URL = "/login"

@login_required
def index(request):
    results = Activity.objects.filter(author__username=request.user.username)
    context = { 'name' : request.user.username, 'results' : results}
    return render(request, "activities/index.html", context)

@login_required
def add_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = Activity(author=request.user,
                                description=form.cleaned_data["description"],
                                activity_date=form.cleaned_data["activity_date"],
                                activity_type=form.cleaned_data["activity_type"],
                                ticket_number=form.cleaned_data["ticket_number"],
                                hours_worked=form.cleaned_data["hours_worked"])
            activity.save()
            return HttpResponseRedirect('/')
    else:
        form = ActivityForm()
    return render(request, "activities/add.html", { 'form' : form })

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
