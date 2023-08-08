from django.db import models
import datetime



class Tasks(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

