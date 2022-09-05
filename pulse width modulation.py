from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(1))
pwm.freq(1000)

#print(dir(sleep))
while True:
    for duty in range(0,65025,10):
        pwm.duty_u16(duty)
        #sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        #sleep(0.0001)