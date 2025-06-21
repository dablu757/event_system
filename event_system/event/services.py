from .models import Event, Attendee
from django.core.exceptions import ValidationError

def register_attendee(event_id, name, email):
    event = Event.objects.get(id=event_id)
    if event.attendees.count() >= event.max_capacity:
        raise ValidationError("Event is at full capacity.")
    if Attendee.objects.filter(event=event, email=email).exists():
        raise ValidationError("Attendee already registered.")
    attendee = Attendee.objects.create(name=name, email=email, event=event)
    return attendee
