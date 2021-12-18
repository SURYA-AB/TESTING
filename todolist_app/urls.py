from typing import Pattern
from django.urls import path
from todolist_app import views


urlpatterns = [

    path('', views.todolist, name='todolist'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('view/<task_id>', views.view_task, name='view_task'),
    path('complete', views.complete_task, name='complete_task'),
    path('finish', views.finish_task, name='finish_task'),
    path('finish1/<task_id>', views.finish1_task, name='finish1_task'),
    path('success', views.success, name='success'),
    path('email1/<task_id>', views.email1, name='email1'),
    path('export', views.export, name='export'),

    path('export2', views.export2, name='export2'),
    path('email_updatetask/<id>', views.email_updatetask, name='email_updatetask'),
    path('email_remindertask/<id>', views.email_remindertask, name='email_remindertask'),
    path('arul', views.todolist1, name='todolist1'),
    path('ram', views.todolist2, name='todolist2'),
    path('akash', views.todolist3, name='todolist3'),
    path('Pavithra', views.todolist4, name='todolist4'),
    path('Barath', views.todolist5, name='todolist5'),
    path('kalai', views.todolist6, name='todolist6'),

    #path('update', views.test, name='test_list'),
    #path('update2', views.test2, name='test_list'),
    #path('updateform', views.testform, name='test_form'),
    #path('log',views.log,name='log'),
    path('sms', views.sms, name='sms'),
    #path('reminder',views.reminder,name='reminder'),
    path('upload', views.attendence, name='attendence'),
    path('uploadview', views.view2, name='view2'),
    path('newpage', views.newpage, name='newpage'),
    
]


#path('', views.subscribe, name = 'subscribe'),  path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),