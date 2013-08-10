from django.shortcuts import render, redirect
from activities.models import AuthorInfo, Category, Activity
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from activities.forms import ActivityForm

settings.LOGIN_REDIRECT_URL = "/"
settings.LOGIN_URL = "/login"

@login_required
def index(request):
    results = Activity.objects.filter(author__username=request.user.username)
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
            return redirect(reverse('index'))
    else:
        form = ActivityForm()
    context = { 'name' : request.user.username,
                'results' : results,
                'form' : form }

    return render(request, "activities/index.html", context)

@login_required
def reports(request):
    # check for admin required
    browser_stats = {'Chrome': 52.9, 'Opera': 1.6, 'Firefox': 27.7}
    context = {'browser_stats': browser_stats}
    return render(request, "activities/reporting.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
