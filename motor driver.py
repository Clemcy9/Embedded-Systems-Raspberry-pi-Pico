"""
this code runs a motor connected to a rPi pico via motor driver

"""
from machine import Pin, ADC, PWM
from time import sleep
in1 =Pin(0,Pin.OUT)
in2 =Pin(1,Pin.OUT)

print(dir(PWM))
print(dir(ADC))

enA = PWM(Pin(2))
enA.freq(1000)
in1.value(0)
in2.value(1)
enA.duty_u16(65500)