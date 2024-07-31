from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def is_past_due(self):
        return self.event_date < timezone.now()

    def time_remaining(self):
        if self.is_past_due():
            return timezone.timedelta(0)
        return self.event_date - timezone.now()

    def hours_remaining(self):
        return self.time_remaining().days * 24 + self.time_remaining().seconds // 3600

    def minutes_remaining(self):
        return (self.time_remaining().seconds % 3600) // 60

    def seconds_remaining(self):
        return self.time_remaining().seconds % 60
