/*This assumes you have installed Adafruit_BBIO, if not please read de readme file*/


import Adafruit_BBIO.GPIO as GPIO
from time import sleep
OutputLED = "P9_12"
GPIO.setup(OutputLED, GPIO.OUT)
for i in range(0,5):
  GPIO.output(OutputLED, GPIO.HIGH)  
  sleep(5)
  GPIO.output(OutputLED, GPIO.LOW) 
  sleep(5)
GPIO.cleanup()
