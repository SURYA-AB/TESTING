from os import name
from django.core.checks import messages
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
import datetime

# Create your models here.
   

class Tasklist(models.Model):

    clientname= models.CharField(max_length=100,null=True,blank=True)
    task = models.CharField(max_length=100)
    startdate = models.DateField(default=timezone.now, blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    assignee = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    fstatus = models.BooleanField(default=False)


    def __str__(self):
        return self.task + " - Task - " + str(self.fstatus)

class edit_page(models.Model):

    old_id = models.ForeignKey(Tasklist,null=True,on_delete=models.CASCADE)
    updatedate = models.DateField(blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)
    messagelogs = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='',null=True,blank=True)

    def __str__(self):
        return self.messagelogs

class doc(models.Model):
    name = models.CharField(max_length = 100,null=True)
    date = models.DateField(blank=True,null=True)
    time1 = models.CharField(max_length = 100,null=True)
    time2 = models.CharField(max_length = 100,null=True)
    client = models.CharField(max_length=1000,null=True)
    des = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name

#class files(models.Model):
#    number = models.ForeignKey(Tasklist,null=True,on_delete=models.CASCADE)
 #   file2 = models.FileField(upload_to='',null=True,blank=True)


