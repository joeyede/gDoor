from datetime import datetime, timedelta
from unittest.mock import Mock

from enum import Enum, unique, IntEnum
import logging
import time

#Sensors:
# 16 : Closed - 0 when closed 1 when open 
# 18: Open - 1 when door not open all the way.  0 when triggerd

# Get an instance of a logger
logger = logging.getLogger(__name__)
lastToggle  = datetime.now() - timedelta(seconds=5)

class PinID(IntEnum):
    CLOSED = 16
    OPEN = 18
    DOOR_TRIGGER = 7

try:
    import RPi.GPIO as GPIO
    
except ImportError:
    logger.warning("RPi.GPIO Import failed.  This is normal only if not on RPi Platform!")

    # This section setups Mocking for testing on Non Raspberi Pi enviroment 
    GPIO = Mock()
    def inputMock(id):
        if id == PinID.CLOSED: return GPIO.HIGH
        if id == PinID.OPEN: return GPIO.LOW
        return GPIO.UNKNOWN
    
    GPIO.input.side_effect  = inputMock
    # End mocking section 
  


@unique
class DoorState(Enum):
    OPEN = 'Fully-Open'
    CLOSED = 'Closed'
    PART_OPEN = 'Part-Open'
    SENSOR_ERROR = 'Invalid-State-Sensor-Error'

    def __str__(self) -> str:
        return self.value





def TriggerDoor():
    """
    Check if minimum wait happend if so TriggerDoor door else ingnore
    Return: True if door actualy TriggerDoor. 
    """
    global lastToggle
    if  datetime.now() - lastToggle < timedelta(seconds=2) :
        logger.info('Toggle To Fast')
        return False

    logger.info('Door toggled!')
    _UnsafeTriggerDoor()
    lastToggle = datetime.now()
    return True


def getDoorState():
    
    if GPIO.input(PinID.CLOSED) == GPIO.HIGH and GPIO.input(PinID.OPEN) == GPIO.HIGH :
        return DoorState.PART_OPEN
    elif GPIO.input(PinID.CLOSED) == GPIO.LOW and GPIO.input(PinID.OPEN) == GPIO.HIGH :
        return DoorState.CLOSED
    elif GPIO.input(PinID.CLOSED) == GPIO.HIGH and GPIO.input(PinID.OPEN) == GPIO.LOW :
        return DoorState.OPEN
    else:
        logger.error("Invalid door State")
        return DoorState.SENSOR_ERROR

def registerForChange(callback):
    GPIO.add_event_detect(PinID.CLOSED, GPIO.BOTH, callback=callback,bouncetime=300)
    GPIO.add_event_detect(PinID.OPEN, GPIO.BOTH, callback=callback,bouncetime=300)
    


def _UnsafeTriggerDoor():
    GPIO.output(PinID.DOOR_TRIGGER, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(PinID.DOOR_TRIGGER, GPIO.LOW)

