#from gDoor.gDoorControl.RaspberryPiControl import RaspberryPiControl


import logging

from django.http.response import HttpResponse

from .RaspberryPiControl  import PiControl
from random import randrange
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from django.http import JsonResponse

from .models import HomeLocations



# Get an instance of a logger
logger = logging.getLogger(__name__)


@login_required
def index(request):
    loc = HomeLocations.objects.first()
    if  not loc:
        loc = HomeLocations(home_lat = 0 , home_long= 0 )
    context = {
        'location': loc,
    }    

    return render(request, 'gDoorControl/index.html',context)

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


@login_required
def homeLocation(request):
    locations = HomeLocations.objects.order_by('id')  # Only 1 home location
    context = {
        'locations': locations,
    }
    return render(request, 'gDoorControl/home_location.html', context)

@login_required
def updateHomeLocation(request):
    loc = HomeLocations.objects.first()
    if loc :
        loc.home_lat = request.POST['curlat']
        loc.home_long = request.POST['curlong']
    else:
        loc = HomeLocations(home_lat = request.POST['curlat'] , home_long= request.POST['curlong'] )
    
    loc.save()
    return HttpResponseRedirect(reverse('homeLocation'))
    
    

def main():
    stat= PiControl.getDoorState()
    print(f"stat: {stat}")


if __name__ == "__main__":
   main()
