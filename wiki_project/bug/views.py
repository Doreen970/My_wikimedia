from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm
# a view that registers all bugs entered by the user
# a form is generated for the user to enter details about the bug
def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug-list')  # Redirect to the bug list view
    else:
        form = BugForm()
    return render(request, 'bug/register_bug.html', {'form': form})

# a view to show details of a bug
def detail(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/detail.html', {'bug': bug}) 

# a view that lists all bugs
def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug/bug_list.html', {'bugs': bugs})      

