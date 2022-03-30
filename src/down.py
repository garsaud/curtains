import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20, GPIO.OUT);
GPIO.setup(16, GPIO.OUT);

# disable up
GPIO.output(20, False)

# enable down
GPIO.output(16, True)
time.sleep(40)
GPIO.output(16, False)
