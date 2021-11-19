from django.urls import path

from . import views

app_name = 'form_name'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('done/', views.done, name='done'),
]
