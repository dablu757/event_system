from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/register/', views.register_view, name='register'),
    path('events/<int:event_id>/attendees/', views.attendee_list, name='attendee_list'),
]
