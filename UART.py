#This code assumes you have pyserial installed
#if not, run this on your terminal before sudo pip install pyserial

import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")

with serial.Serial(port = "/dev/ttyO1", baudrate=115200) as serial:
    print("Serial abierto")
    serial.write("Prueba serial")
