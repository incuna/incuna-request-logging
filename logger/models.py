from django.db import models
from django.utils import timezone


class Log(models.Model):
    user_pk = models.PositiveIntegerField()
    registration_date = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.now)
    url = models.TextField()
    request_method = models.CharField(max_length=255)
