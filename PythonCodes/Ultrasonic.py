from machine import Pin, PWM
import time
trig = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN, Pin.PULL_DOWN)
led= PWM(Pin(2, Pin.OUT))

def ultra():
    #Gets the value from the ultrasonic sensor
     trig.value(0)
     time.sleep(0.1)
     trig.value(1)
     time.sleep_us(2)
     #Turn on the trigger for 2microsecond
     trig.value(0)
     #Turns off the stigger
     while echo.value()==0:
          pulse_start = time.ticks_us()
    #Counts the amount of seconnds the pin does not read anything
     while echo.value()==1:
          pulse_end = time.ticks_us()
    #Counts the amount of seconnds the pin reads something
     pulse_duration = pulse_end - pulse_start
     distance = int(pulse_duration * 17165 / 1000000)
     #Converts the value to distance
     print (distance,"d")
     return distance

while True:
     ultra()
     change(ultra())
     time.sleep(0.01)

