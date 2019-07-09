import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

print("sys.argv vale {}".format(sys.argv))
if len(sys.argv) >= 2:
    if sys.argv[1] == 'high':
        GPIO.output(18, GPIO.HIGH)
    elif sys.argv[1] == 'low':
        GPIO.output(18, GPIO.LOW)

else:
    while(True):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
