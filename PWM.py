#This code assumes you have installed Adafruit_BBIO
#If not, go to the readme file

import Adafruit_BBIO.PWM as PWM

servo1 = "P9_14"
PWM.start(servo1,2,50)

while(1):
  Angulo=input("Escribe el angulo: ")
  dutyCycle=1./18.*Angulo+2
  PWM.set_duty_cycle(servo1,dutyCycle)
