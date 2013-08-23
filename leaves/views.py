from django.shortcuts import render
from leaves.models import Leave
from leaves.forms import LeaveForm
from django.contrib import messages

def index(request):
    leaves = Leave.objects.filter(author = request.user)
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
    context = { 'leaves' : leaves }
    return render(request, "leaves/index.html", context)
