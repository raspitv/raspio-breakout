#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
# Using PWM with RPi.GPIO pt 2 - requires RPi.GPIO 0.5.2a or higher

import RPi.GPIO as GPIO         # always needed with RPi.GPIO
from time import sleep          # pull in the sleep function from time module
if GPIO.RPI_REVISION == 1:      # check Pi Revision to set port 21/27 correctly
    # define ports list for Revision 1 Pi
    ports = [7,8,25,24,23,18,15,14,0,1,4,17,21,22,10,9,11]
else:
    # define ports list all others
    ports = [7,8,25,24,23,18,15,14,2,3,4,17,27,22,10,9,11]   

leds = []
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
for port_num in ports:
    GPIO.setup(port_num, GPIO.OUT)                  # set up ports for output
    leds.append(GPIO.PWM(port_num, 100)) # build a list of leds for PWM

for i in range(len(leds)):
    leds[i].start(0)

pause_time = 0.0001

print "Press CTRL+C when you've had enough to exit the program"

counter = 1        # odd or even side
interval = 3       # e.g. flash every 2nd or third led

try:
    while True:
        if counter % 2 == 0:
            start = 0
            finish = 8
        else:
            start = 8
            finish = 17                
        for i in range(0,101):      # 101 because it stops when it finishes 100
            for j in range(start, finish, interval):
                leds[j].ChangeDutyCycle(i)
            sleep(pause_time)
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1
            for j in range(start, finish, interval):
                leds[j].ChangeDutyCycle(i)
            sleep(pause_time)
        counter += 1

finally:
    for i in range(len(leds)):
        leds[i].stop()
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit