from django.db import models


class Report(models.Model):
    file_name = models.CharField(max_length=10)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    last_update = models.DateField()
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()


class Update(models.Model):
    started_at = models.DateField()
    ended_at = models.DateField()
    elapsed_time = models.DurationField()
