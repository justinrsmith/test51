from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect

from contests.forms import ContestEntryForm
from contests.models import Contest, ContestEntry

# Create your views here.
def contest(request):
    contest = Contest.objects.get(pk=1)
    contest_entries = ContestEntry.objects.filter(contest=contest)
    return render(request, 'contests/index.html', {
        'contest_entries': contest_entries
    })

#@login_required
def contest_entry(request):
    # If user is logged in and doing it via email log them out, temporary fix
    if request.GET.get('email', None):
        logout(request)
    if request.method == 'POST':
        contest = Contest.objects.first()
        form = ContestEntryForm(request.POST)
        # If user uses a social service
        if not request.user.is_anonymous():
            form = ContestEntryForm(
                request.POST,
                user=request.user,
                social_provider=request.user.socialaccount_set.first().provider
            )
        service_entered_with = 'email'
        if form.is_valid():
            contest_entry = form.save(commit=False)
            contest_entry.contest = contest
            if not request.user.is_anonymous():
                contest_entry.user = request.user
                contest_entry.social_provider = request.user.socialaccount_set.first().provider
                service_entered_with = contest_entry.social_provider
            contest_entry.save()
            messages.success(request, ('Your entry has been submitted'))
            return redirect('/')
        else:
            if not request.user.is_anonymous():
                 service_entered_with = request.user.socialaccount_set.first().provider.title()
            return render(request, 'contests/index.html', {
                'form': form,
                'service_entered_with': service_entered_with
            })

    form = ContestEntryForm()
    # Set default to email if they are not anonymous then they are using
    # a social service and we will set below
    service_entered_with = 'email'
    if not request.user.is_anonymous():
        service_entered_with = request.user.socialaccount_set.first().provider.title()
        form = ContestEntryForm(
            initial={
                'full_name': request.user.username,
                'email': request.user.email
            },
            user=request.user,
            social_provider=service_entered_with
        )

    return render(request, 'contests/index.html', {
        'form': form,
        'service_entered_with': service_entered_with
    })
