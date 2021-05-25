from django.urls import path

from . import views

app_name='guide'

urlpatterns = [
    path('', views.index, name='index'),
    path('support/', views.support, name='support'),
]