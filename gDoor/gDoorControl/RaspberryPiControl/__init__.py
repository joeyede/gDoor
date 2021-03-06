import logging
try:
    import RPi.GPIO as GPIO
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)

except ImportError:
    logger = logging.getLogger(__name__)
    logger.warning("RPi.GPIO Import failed.  This is normal only if not on RPi Platform!")

