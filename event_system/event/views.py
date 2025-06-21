from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Event, Attendee
from .services import register_attendee
from django.core.paginator import Paginator
from django.contrib import messages

from django.shortcuts import render

def home(request):
    return render(request, 'events/home.html')


def event_list(request):
    events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

def register_view(request, event_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        try:
            register_attendee(event_id, name, email)
            messages.success(request, "Successfully registered.")
        except Exception as e:
            messages.error(request, str(e))
    return redirect('attendee_list', event_id=event_id)

def attendee_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendees = event.attendees.all()
    paginator = Paginator(attendees, 5)
    page = request.GET.get('page')
    attendees_paginated = paginator.get_page(page)
    return render(request, 'events/attendee_list.html', {
        'event': event,
        'attendees': attendees_paginated
    })
