from django.shortcuts import render, redirect
from activities.models import AuthorInfo, Category, Activity
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from activities.forms import ActivityForm, ReportsDateForm
import datetime
from collections import defaultdict
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView

settings.LOGIN_REDIRECT_URL = "/"
settings.LOGIN_URL = "/login"


@login_required
def index(request):
    # list of activities posted by this user
    results = {}
    today = timezone.now()
    results['all'] = Activity.objects.filter(author__username=request.user.username)
    results['today'] = [item for item in results['all'] if item.activity_date == today.date()]
    results['last_seven_days'] = [item for item in results['all'] \
                                      if (item.activity_date + datetime.timedelta(days=7) > today.date() \
                                          and item.activity_date < today.date())]
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
            messages.add_message(request, messages.SUCCESS, "Activity added successfully!")
            return redirect(reverse('index'))
    else:
        form = ActivityForm()
    context = { 'name' : request.user.username,
                'results' : results,
                'form' : form ,
                'today': today.date()}

    return render(request, "activities/dashboard.html", context)

@login_required
def all_activities(request):
    results = Activity.objects.filter(author__username=request.user.username)
    paginator = Paginator(results, 8)
    page = request.GET.get('page')
    try :
        activities = paginator.page(page)
    except PageNotAnInteger:
        activities = paginator.page(1)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
    return render(request, "activities/all.html", {'activities' : activities})

class ActivityUpdate(UpdateView):
    model = Activity
    success_url = reverse_lazy('index')

class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('index')

@login_required
def reports(request):
    # check for admin required
    form = ReportsDateForm()
    start_date_unclean = request.GET.get("start_date", False)
    end_date_unclean = request.GET.get("end_date", False)
    today = timezone.now().date()

    if not start_date_unclean or not end_date_unclean:
        # when no dates... show data for the past one week
        start_date = today - datetime.timedelta(days=7)
        end_date = today
    else:
        # else read the dates from the url
        start_date = datetime.datetime.strptime(start_date_unclean, "%m/%d/%Y")
        end_date = datetime.datetime.strptime(end_date_unclean, "%m/%d/%Y")

    context = { 'form' : form }

    if start_date and end_date and (start_date < end_date):
        show_data = True

        results = {}

        # author - boolean representing onsite_team
        author_onsite_team = {obj.author: obj.onsite_team for obj in AuthorInfo.objects.all()}

        # start and end date
        results['start_date'] = start_date
        results['end_date'] = end_date

        # the list of activities for that date
        activities = Activity.objects.filter(activity_date__gte=start_date)\
                                     .filter(activity_date__lte=end_date)

        combined_work = defaultdict(int)
        combined_work_onsite = defaultdict(int)
        combined_work_offshore = defaultdict(int)
        support_activities = list()
        bau_activities = list()
        project_activities = list()
        bugs_activities = list()

        for activity in activities:
            parent = activity.activity_type.parent_category # cache this

            # for graphs
            combined_work[parent] += int(round(activity.hours_worked))
            if author_onsite_team[activity.author]:
                combined_work_onsite[parent] += int(round(activity.hours_worked))
            else:
                combined_work_offshore[parent] += int(round(activity.hours_worked))

            # for tables
            if parent == "Support":
                support_activities.append(activity)
            elif parent == "BAU":
                bau_activities.append(activity)
            elif parent == "Project":
                project_activities.append(activity)
            else:
                bugs_activities.append(activity)


        # graphs
        results['combined_work']  = dict(combined_work)
        results['combined_work_onsite']  = dict(combined_work_onsite)
        results['combined_work_offshore']  = dict(combined_work_offshore)

        # tables
        results["support_activities"] = support_activities
        results["bau_activities"] = bau_activities
        results["project_activities"] = project_activities
        results["bugs_activities"] = bugs_activities

        context = { 'form' : form, 'show_data' : show_data, 'results': results }

    return render(request, "activities/reporting.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
