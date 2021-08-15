from gDoor.gDoorControl.RaspberryPiControl import RaspberryPiControl

from random import randrange
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from django.http import JsonResponse




import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render(request, 'gDoorControl/index.html')

@login_required
def toggleDoor(request):
    toggled = RaspberryPiControl.TriggerDoor()
    url = reverse('/', kwargs={'toggled': str(toggled)})
    return HttpResponseRedirect(url)
#    return HttpResponseRedirect('/')

@login_required
def getDoorState(request):
    stat= RaspberryPiControl.getDoorState

    data = {
            'state': str(stat), 
    }
    return JsonResponse(data)
