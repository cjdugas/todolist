from django.db import models
import datetime
from django.utils import timezone


class List(models.Model):
    title = models.CharField(max_length=100)
    #description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    #description.admin_order_field = 'description'


class Task(models.Model):
    #maybe try to use DateField instead
    list = models.ForeignKey(List)

    task_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('due date')
    done = models.BooleanField('done?')

    def __unicode__(self):
        return self.task_text

    def due_this_week(self):
        now = timezone.now()
        return now <= self.pub_date < now + datetime.timedelta(days=7)

    due_this_week.admin_order_field = 'pub_date'  
    due_this_week.boolean = True
    due_this_week.short_description = 'Due within the next 7 days?'
