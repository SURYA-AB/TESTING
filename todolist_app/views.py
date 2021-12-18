from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist,edit_page,doc
from todolist_app.forms import TaskForm,TaskForm2
from django.contrib import messages
from taskmate2.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
#import xlwt
from django.contrib.auth.models import User
import csv
import requests
import urllib
from urllib.request import urlopen
from todolist_app.functions import handle_uploaded_file  
from django.core.files.storage import FileSystemStorage
# Create your views here.

def todolist(request):
     if request.user.is_authenticated:
          if request.method == 'POST' and 'action' in request.POST:

            data = request.POST.copy()
            form = TaskForm(request.POST or None)
            if form.is_valid():
                    newdata = form.save()
                            #messages.success(request,(newdata.pk))
            #Client_name = newdata.pk.get("Clientname")
            task = Tasklist.objects.get(pk=newdata.pk)
            Client =  task.clientname
            Work = task.task
            Assignee = task.assignee

            
            if Assignee ==  ('Ramajayam'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
               # Print (Assignee)

            elif Assignee ==  ('Arul Murugan'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9962138673&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
               # Print Assignee
            elif Assignee ==  ('Akash'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Pavithra'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9600190835&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Bharath'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=8138986331&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Kalai'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=7338758831&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            else:
                print ("sms not sent")

            messages.success(request,("New Task Added Successfully!" ))
            return redirect('email1', (newdata.pk))
            return  redirect('todolist')

          else:
                countarulpending = Tasklist.objects.filter(assignee = 'Arul Murugan').filter(status = 'Pending').count()
                countarulwip = Tasklist.objects.filter(assignee = 'Arul Murugan').filter(status = 'Work in Progress').count()
                countrampending = Tasklist.objects.filter(assignee = 'Ramajayam').filter(status = 'Pending').count()
                countramwip = Tasklist.objects.filter(assignee = 'Ramajayam').filter(status = 'Work in Progress').count()
                countramapp = Tasklist.objects.filter(status = 'Finished').filter(fstatus = 0).count()

                countpavithrapending = Tasklist.objects.filter(assignee = 'Pavithra').filter(status = 'Pending').count()
                countpavithrawip = Tasklist.objects.filter(assignee = 'Pavithra').filter(status = 'Work in Progress').count()
                countgunapending = Tasklist.objects.filter(assignee = 'Guna').filter(status = 'Pending').count()
                countgunawip = Tasklist.objects.filter(assignee = 'Guna').filter(status = 'Work in Progress').count()
                countakashpending = Tasklist.objects.filter(assignee = 'Akash').filter(status = 'Pending').count()
                countakashwip = Tasklist.objects.filter(assignee = 'Akash').filter(status = 'Work in Progress').count()
                countbharathpending = Tasklist.objects.filter(assignee = 'Bharath').filter(status = 'Pending').count()
                countbharathwip = Tasklist.objects.filter(assignee = 'Bharath').filter(status = 'Work in Progress').count()

                countkalaipending = Tasklist.objects.filter(assignee = 'Kalai').filter(status = 'Pending').count()
                countkalaiwip = Tasklist.objects.filter(assignee = 'Kalai').filter(status = 'Work in Progress').count()

                all_tasks = Tasklist.objects.all()
                #print(count)
                #context2 = {'count': count}

                all_tasks_sorted = Tasklist.objects.order_by('fstatus')

                context = {
                    'all_tasks': all_tasks_sorted,
                    'countarulpending': countarulpending,
                    'countarulwip': countarulwip,
                    'countrampending': countrampending,
                    'countramwip': countramwip,
                    'countramapp': countramapp,

                    'countakashpending': countakashpending,
                    'countakashwip': countakashwip,
                    'countbharathpending': countbharathpending,
                    'countbharathwip': countbharathwip,
                    'countkalaipending': countkalaipending,
                    'countkalaiwip': countkalaiwip
                }

                return render(request, 'todolist.html',context)
     else:
          return  render(request, 'registration/login.html')

def todolist1(request):

                all_tasks = Tasklist.objects.filter(assignee ='Arul Murugan').all()
                countarulpending = Tasklist.objects.filter(assignee = 'Arul Murugan').filter(status = 'Pending').count()
                countarulwip = Tasklist.objects.filter(assignee = 'Arul Murugan').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countarulpending': countarulpending,
                    'countarulwip': countarulwip,
                }
                return render(request, 'todolist1.html',context)

def todolist2(request):

                all_tasks = Tasklist.objects.filter(assignee ='Ramajayam').all()
                countrampending = Tasklist.objects.filter(assignee = 'Ramajayam').filter(status = 'Pending').count()
                countramwip = Tasklist.objects.filter(assignee = 'Ramajayam').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countrampending': countrampending,
                    'countramwip': countramwip,
                }
                return render(request, 'todolist2.html',context)

def todolist3(request):

                all_tasks = Tasklist.objects.filter(assignee ='Akash').all()
                countrampending = Tasklist.objects.filter(assignee = 'Akash').filter(status = 'Pending').count()
                countramwip = Tasklist.objects.filter(assignee = 'Akash').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countrampending': countrampending,
                    'countramwip': countramwip,
                }
                return render(request, 'akashpage.html',context)
                
def todolist4(request):

                all_tasks = Tasklist.objects.filter(assignee ='Pavithra').all()
                countrampending = Tasklist.objects.filter(assignee = 'Pavithra').filter(status = 'Pending').count()
                countramwip = Tasklist.objects.filter(assignee = 'Pavithra').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countrampending': countrampending,
                    'countramwip': countramwip,
                }
                return render(request, 'pavithrapage.html',context)

def todolist5(request):

                all_tasks = Tasklist.objects.filter(assignee ='Bharath').all()
                countbharathpending = Tasklist.objects.filter(assignee = 'Bharath').filter(status = 'Pending').count()
                countbharathwip = Tasklist.objects.filter(assignee = 'Bharath').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countbharathpending': countbharathpending,
                    'countbharathwip': countbharathwip,
                }
                return render(request, 'Barathpage.html',context)

def todolist6(request):

                all_tasks = Tasklist.objects.filter(assignee ='Kalai').all()
                countkalaipending = Tasklist.objects.filter(assignee = 'Kalai').filter(status = 'Pending').count()
                countkalaiwip = Tasklist.objects.filter(assignee = 'Kalai').filter(status = 'Work in Progress').count()

                context = {
                    'all_tasks': all_tasks,
                    'countkalaipending': countkalaipending,
                    'countkalaiwip': countkalaiwip,
                }
                return render(request, 'kalaipage.html',context)

def edit_task(request, task_id):

        if request.method == "POST" and 'update' in request.POST: 
            
            updatedate=request.POST['updatedate']
            time_from=request.POST['time_from']
            time_to=request.POST['time_to']
            messagelogs=request.POST['messagelogs']
            old_id=Tasklist.objects.get(id=task_id)
            #number = Tasklist.objects.get(id=task_id)
            file = request.FILES['file']
            #file2 = request.FILES['file2']
            test_list = edit_page(file=file,old_id=old_id,updatedate=updatedate,time_from=time_from,time_to=time_to,messagelogs=messagelogs)
            #test_list2 = files(number=number,file2=file2)
            test_list.save()
            #test_list2.save()
        
            task = Tasklist.objects.get(pk=task_id)
            form = TaskForm(request.POST or None, instance = task)
            if form.is_valid(): 
                form.save()

                Work = task.task
                Client = task.clientname
                Assignee = task.assignee
            
            if Assignee ==  ('Ramajayam'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
               # Print (Assignee)

            elif Assignee ==  ('Arul Murugan'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9962138673&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
               # Print Assignee
            elif Assignee ==  ('Akash'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear "+ Assignee +", The task of M/s "+ Client +" for task " +  Work + " has been updated. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707163618197489155&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear "+ Assignee +", The task of M/s "+ Client +" for task " +  Work + " has been updated. Regards Ramajayam and Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707163618197489155&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Pavithra'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9600190835&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Bharath'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=8138986331&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Kalai'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=7338758831&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            else:
                print ("sms not sent")

            messages.success(request,("Task Updated Successfully!!!")) 
            return redirect('email_updatetask', (task_id))   
            return  redirect('todolist')

        if request.method == "POST" and 'reminder' in request.POST:
            task = Tasklist.objects.get(pk=task_id)
            Client = task.clientname
            Assignee = task.assignee
            Work = task.task
        
            if Assignee ==  ('Ramajayam'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
                #Print (Assignee)
            elif Assignee ==  ('Arul Murugan'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9962138673&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
                # Print Assignee
            elif Assignee ==  ('Akash'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear " + Assignee + ", The task of M/s " + Client + " for task " + Work + " has been marked urgent. Please complete soon.For more details please log on to www.app.ramajayam.in. RegardsRamajayam & Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707163618241251740&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear " + Assignee + ", The task of M/s " + Client + " for task " + Work + " has been marked urgent. Please complete soon.For more details please log on to www.app.ramajayam.in. RegardsRamajayam & Associates&mnumber=9345620789&entityid=1701159720921220642&templateid=1707163618241251740&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            elif Assignee ==  ('Pavithra'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9600190835&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
           
            elif Assignee ==  ('Kalai'):
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9884468111&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for " +  Client + " for " + Work + " has been added to your Worklist. Regards Ramajayam and Associates&mnumber=7338758831&entityid=1701159720921220642&templateid=1707161911583298075&smstype=Trans"
                requests.get(http_req)
                #print (http_req)
                #print (Client)
            else:
                print ("sms not sent")

            messages.success(request,("Sent Reminder!!!")) 
            return redirect('email_remindertask', (task_id))   
            return  redirect('todolist')

        else:
            #log = files.objects.filter(number=task_id)
            logger = edit_page.objects.filter(old_id=task_id).order_by('-updatedate','-time_to')
            task_obj = Tasklist.objects.get(pk=task_id)
            return render(request, 'edit.html', {'task_obj': task_obj,'logs':logger})  

#def upload(request):
#    context = {}
#    if request.method == 'POST':
#        uploaded_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(uploaded_file.name,uploaded_file)
#        context['url'] = fs.url(name)
#    return render (request,'upload.html',context)  

def view_task(request, task_id):
          task_obj = Tasklist.objects.get(pk=task_id)
          return render(request, 'viewlogs.html', {'task_obj': task_obj})

def complete_task(request):

          all_tasks = Tasklist.objects.all()
          all_tasks_sorted = Tasklist.objects.filter(fstatus=True).order_by('fstatus')
          return render(request, 'complete.html', {'all_tasks': all_tasks_sorted})

def finish1_task(request, task_id):
          task = Tasklist.objects.get(pk=task_id)
          task.fstatus = True
          task.status = "Finished - App"
          task.save()
          messages.success(request,("Task marked as Complete"))
          return  redirect('finish_task')

def finish_task(request):
    all_tasks = Tasklist.objects.all()
    all_tasks_sorted = Tasklist.objects.filter(status="Finished").order_by('fstatus')
    return render(request, 'finish.html', {'all_tasks': all_tasks_sorted})

def index(request):
    return  redirect('todolist')

def sms(request):
    http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for Test_Client has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9600190835&entityid=1701159720921220642&templateid=  1707161911583298075&smstype=Trans"
    requests.get(http_req)
    return redirect('todolist')

def sms_with_name(request, Client_name):

    http_req = "https://app.sollu.in/api/transactional_sms?apikey=3A93C4F42D2B9EFE8823EAB85EC&message=Dear Team, New Task for "

    http_req2 =  "has been added to your Worklist. Regards Ramajayam and Associates&mnumber=9600190835&entityid=1701159720921220642&templateid=  1707161911583298075&smstype=Trans"
    requests.get(http_req + Client_name + http_req2)
    return redirect('todolist')

def success(request):
     return  render(request, 'success.html')

def email(request):
    subject = ('New Task added' 's')
    message = ' Please check http://ramajayampro.pythonanywhere.com/todolist/ '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['accounts@ramajayam.in',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('success')

def email1(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    subject = 'New Task added to '  + task.assignee
    message = '\nClient Name = ' + task.clientname + '\nTask  ' + task.task +  '\nAssigned to ' + task.assignee  + ' \n\nPlease check the task  https://app.ramajayam.in/todolist// \n' + 'Regards\n\nBot126\n\nRamajayam and Associates dafdg'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['accounts@ramajayam.in',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('todolist')

def email_updatetask(request, id):
    task = Tasklist.objects.get(pk=id)
    subject = 'Task Updated for '  + task.assignee
    message = '\nClient Name = ' + task.clientname + '\nTask = ' + task.task +  '\nAssigned to ' + task.assignee  + ' \n\nPlease check the task  http://ramajayampro.pythonanywhere.com/todolist/ \n' + 'Regards\n\nBot126\n\nRamajayam and Associates'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['accounts@ramajayam.in',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('todolist')

def email_remindertask(request, id):
    task = Tasklist.objects.get(pk=id)
    subject = 'Task Reminder for '  + task.assignee
    message = '\nClient Name = ' + task.clientname + '\nTask = ' + task.task +  '\nAssigned to ' + task.assignee  + ' \n\nPlease check the task  http://ramajayampro.pythonanywhere.com/todolist/ \n' + 'Regards\n\nBot126\n\nRamajayam and Associates'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['accounts@ramajayam.in',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('todolist')

def export(request):
     response = HttpResponse(content_type='text/csv')
     writer = csv.writer(response)
     writer.writerow(['client Name', 'task'])
     for Tasklists in Tasklist.objects.all().values_list('clientname','task'):
          writer.writerow(Tasklists)
     response['Content-Disposition'] = 'attachment; filename="Tasklist.csv" '
     return(response)

from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook

def export2(request):

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-movies.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    workbook = Workbook()

    # Get active worksheet/tab
    worksheet = workbook.active
    worksheet.title = 'Movies'

    # Define the titles for columns
    columns = [
        'ID',
        'Title',
        'Description',
        'Length',
        'Rating',
        'Price',
    ]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Iterate through all movies
    workbook.save(response)
    return response


def attendence(request):
    if request.POST:        
        name = request.POST['name']
        date = request.POST['date']
        time1= request.POST['time1']
        time2= request.POST['time2']
        des = request.POST['des']
        attern = doc(name=name,date=date,time1=time1,time2=time2,des=des)
        attern.save()
        return HttpResponse("UPLOAD SUCCESSFULLY !!!")
    else:             
        return render(request,'at.html')

def view2(request):
    attern = doc.objects.all()
    return render(request,'details.html',{'attern':attern})

def newpage(request):
        if request.method == "POST" and 'update1' in request.POST:        
            name = request.POST['name']
            date = request.POST['date']
            time1= request.POST['time1']
            time2= request.POST['time2']
            des = request.POST['des']
            client = request.POST['client']
            attern1 = doc(name=name,date=date,time1=time1,time2=time2,des=des,client=client)
            attern1.save()
            return HttpResponse("UPLOAD SUCCESSFULLY !!!")
        
        if request.method == "POST" and 'update2' in request.POST:        
            name = request.POST['name']
            date = request.POST['date']
            time1= request.POST['time1']
            time2= request.POST['time2']
            des = request.POST['des']
            client = request.POST['client']
            attern2 = doc(name=name,date=date,time1=time1,time2=time2,des=des,client=client)
            attern2.save()
            return HttpResponse("UPLOAD SUCCESSFULLY !!!")
        else:            
            return render(request,'newpage.html')