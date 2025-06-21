from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('email', 'event')

