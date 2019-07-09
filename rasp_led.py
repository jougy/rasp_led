import RPi.GPIO as GPIO
import time
import sys
import os
import Adafruit_DHT
SLEEP_TIME = 0.5
LED_PIN = 18
DHT_PIN = 4


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

SENSOR = Adafruit_DHT.DHT11

def high():
    GPIO.output(LED_PIN, GPIO.HIGH)

def low():
    GPIO.output(LED_PIN, GPIO.LOW)

def get_hum_temp():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, DHT_PIN)
    return humidity, temperature
def oF():
    temperature = get_hum_temp()[1]
    return((temperature*(9/5))+32)
    
print("sys.argv vale {}".format(sys.argv))
if len(sys.argv) >= 2:
    if sys.argv[1] == 'high':
        high()
    elif sys.argv[1] == 'low':
        low()

else:
    try:
        while(True):
            high()
            humidity, temperature = get_hum_temp()
            temp_f = oF()
            print("umidade: {}\ntemperatura: {}C / {}F ".format(humidity,temperature,temp_f))
            time.sleep(SLEEP_TIME)
            low()
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        low()
        os.system('clear')
        print("saindo do programa...")
        sys.exit()
