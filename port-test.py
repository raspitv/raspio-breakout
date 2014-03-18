import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

if GPIO.RPI_REVISION == 1:
    leds = [7,8,25,24,23,18,15,14,0,1,4,17,21,22,10,9,11]
    leds1 = [7,8,25,24,23,18,15,14]
    leds2 = [0,1,4,17,21,22,10,9,11]
else:
    leds = [7,8,25,24,23,18,15,14,2,3,4,17,27,22,10,9,11]
    leds1 = [7,8,25,24,23,18,15,14]
    leds2 = [2,3,4,17,27,22,10,9,11]

for i in leds:
    GPIO.setup(i, GPIO.OUT, initial=0) # sets i to output and 0V, off 

try:
    x = 0
    while x < 100:
        x += 1
        for i in range(8):
            GPIO.output(leds1[i], 1) # sets port on
            GPIO.output(leds2[i], 1) # sets port on
            sleep(0.1/x)
            GPIO.output(leds1[i], 0) # sets port off
            GPIO.output(leds2[i], 0) # sets port off
            if i == 7:
                GPIO.output(leds2[i+1], 1) # sets port on
                sleep(0.1/x)
                GPIO.output(leds2[i+1], 0) # sets port off
        for i in range(7,-1,-1):
            GPIO.output(leds1[i], 1) # sets port on
            GPIO.output(leds2[i], 1) # sets port on
            sleep(0.1/x)
            GPIO.output(leds1[i], 0) # sets port off
            GPIO.output(leds2[i], 0) # sets port off
finally:
    GPIO.cleanup()
