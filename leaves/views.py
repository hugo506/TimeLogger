from django.shortcuts import render
from leaves.models import Leave
from leaves.forms import LeaveForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    results = Leave.objects.filter(author = request.user)
    paginator = Paginator(results, 8)
    page = request.GET.get('page')
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = Leave(author=request.user,
                         description = form.cleaned_data["description"],
                         start_date = form.cleaned_data['start_date'],
                         end_date = form.cleaned_data['end_date'])
            leave.save()
            messages.add_message(request, messages.SUCCESS, "Leave added successfully")
        else:
            form = LeaveForm()
    try:
        leaves = paginator.page(page)
    except PageNotAnInteger:
        leaves = paginator.page(1)
    except EmptyPage:
        leaves = paginator.page(paginator.num_pages)
    context = { 'leaves' : leaves }
    return render(request, "leaves/index.html", context)
