from django.contrib import admin
from django.db.models.fields.files import FileDescriptor
from todolist_app.models import Tasklist,edit_page,doc
# Register your models here.

admin.site.register(Tasklist)
admin.site.register(edit_page)
admin.site.register(doc)
#admin.site.register(files)
