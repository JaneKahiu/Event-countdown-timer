from django.shortcuts import render # Create your views here.
from .models import Event
from django.utils import timezone

def countdown_timer(request):
    events = Event.objects.filter(event_date__gte=timezone.now())
    event_data = []
    for event in events:
        time_remaining = event.event_date - timezone.now()
        hours = time_remaining.days * 24 + time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        
        event_data.append({
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        })

    return render(request, 'timer.html', {'events': event_data})
