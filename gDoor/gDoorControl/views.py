#from gDoor.gDoorControl.RaspberryPiControl import RaspberryPiControl

from .RaspberryPiControl  import PiControl
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
    toggled = PiControl.TriggerDoor()
    if toggled:
        resp = 'Door Toggled Sucessfuly'
    else:
        resp = "Door did't toggle - to fast? <br> Try again in 3 sec."

    data = {
            'toggled': resp, 
    }
    return JsonResponse(data)

@login_required
def getDoorState(request):
    stat= PiControl.getDoorState()

    data = {
            'state': str(stat), 
    }
    return JsonResponse(data)

def main():
    stat= PiControl.getDoorState()
    print(f"stat: {stat}")


if __name__ == "__main__":
   main()
