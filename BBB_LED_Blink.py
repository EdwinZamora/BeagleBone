#This assumes you have installed Adafruit_BBIO, if not please read de readme file


import Adafruit_BBIO.GPIO as GPIO #import GPIO library
from time import sleep

config-pin P9_14 gpio #Configures pin to GPIO

OutputLED = "P9_12" #Select GPIO where you going to put the LED
#setup the pin as OUTPUT
GPIO.setup(OutputLED, GPIO.OUT)
#Start the cycle to blink LED
for i in range(0,5):
  GPIO.output(OutputLED, GPIO.HIGH)  
  sleep(5)
  GPIO.output(OutputLED, GPIO.LOW) 
  sleep(5)
GPIO.cleanup()
