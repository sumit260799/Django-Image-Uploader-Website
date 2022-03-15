
from django.contrib import admin
from django.urls import path,include
from ImageUploader import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('',views.home,name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
