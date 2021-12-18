from django import forms
from django.forms import fields
from todolist_app.models import Tasklist,edit_page




class TaskForm(forms.ModelForm):
    class Meta:
       model = Tasklist
       fields = '__all__'


class TaskForm2(forms.ModelForm):
    class Meta:
       model = edit_page
       fields = '__all__'




  








