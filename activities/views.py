from django.shortcuts import render, redirect
from activities.models import AuthorInfo, Category, Activity
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from activities.forms import ActivityForm, ReportsDateForm
import datetime

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
    form = ReportsDateForm()
    start_date_unclean = request.GET.get("start_date", False)
    end_date_unclean = request.GET.get("end_date", False)

    if not start_date_unclean or not end_date_unclean:
        return render(request, "activities/reporting.html", {'form' : form })

    start_date = datetime.datetime.strptime(start_date_unclean, "%m/%d/%Y")
    end_date = datetime.datetime.strptime(end_date_unclean, "%m/%d/%Y")
    context = { 'form' : form }
    if start_date and end_date and (start_date < end_date):
        show_data = True
        results = {}
        results['start_date'] = start_date
        results['end_date'] = end_date
        results['objects'] = Activity.objects.filter(activity_date__gte=start_date)\
                                 .filter(activity_date__lte=end_date)
        context = { 'form' : form, 'show_data' : show_data, 'results': results }
    return render(request, "activities/reporting.html", context)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
