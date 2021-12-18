from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/',include('todolist_app.urls')),
    path('', todolist_views.index, name='index'),
    path('email', todolist_views.email, name='email'),
    path('accounts/', include('django.contrib.auth.urls')),    

]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)