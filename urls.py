from django.urls import path

from wframe1 import views

urlpatterns = [path('', views.index, name='index'),]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('wframe1/', include('wframe1.urls')),
    path('admin/', admin.site.urls),
]