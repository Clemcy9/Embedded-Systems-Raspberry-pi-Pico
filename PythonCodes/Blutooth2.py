from machine import UART, Pin
from time import sleep
import utime

#38400 is the baudrate and it has to be that number when working with AT commands
uart1 = UART(1, baudrate= 38400, tx = Pin(4), rx = Pin(5))
 
while True:
    uart1.write("AT+NAME:Blutooth\r\n")
    x = uart1.read(4)
    sleep(2)
    print(x)
