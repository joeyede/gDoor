from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggleDoor', views.toggleDoor, name='toggleDoor'),
    path('getDoorState', views.getDoorState, name='getDoorState'),
    path('homeLocation', views.homeLocation, name='homeLocation'),
    path('updateHomeLocation', views.updateHomeLocation, name='updateHomeLocation'),

]
