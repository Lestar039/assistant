from django.contrib import admin
from django.urls import path, include  # из библиотеки django.urls импортируем функцию path

from . import views  # ...а давать ей специальное имя не будем, оставим views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('about', views.about, name='about')
]
