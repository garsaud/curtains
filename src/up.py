import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20, GPIO.OUT);
GPIO.setup(16, GPIO.OUT);

# disable down
GPIO.output(16, False)

# enable up
GPIO.output(20, True)
time.sleep(43)
GPIO.output(20, False)
