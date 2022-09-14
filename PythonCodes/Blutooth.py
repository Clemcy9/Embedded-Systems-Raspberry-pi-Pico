from machine import Pin,UART
from time import sleep

#9600 is the baudrate and it has to be 9600 while receiving commands
uart = UART(1,9600)
led = Pin(16, Pin.OUT)

while True:
    if uart.any():
        #Puts the new line into variable command
        command = uart.readline(2)
        print(command)   # uncomment this line to see the recieved data
        if command==b'1':
            led.high()
            print("ON")
        elif command==b'0':
            led.low()
            print("OFF")
        elif command ==b'3':
            while True:
                led.high()
                sleep(1)
                led.low()
                sleep(1)
                if command != b'3':
                    break
                else :
                    command=uart.readline()
            print("AT")
