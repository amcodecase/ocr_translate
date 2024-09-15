# ocr_project/ocr_project/urls.py

from django.contrib import admin
from django.urls import path  # Make sure this line is present
from ocr_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ocr_and_translate, name='ocr_and_translate'),
]
