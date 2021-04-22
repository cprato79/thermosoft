#!/usr/bin/python3.5
import RPi.GPIO as GPIO
from time import sleep


# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
#GPIO.setup(6, GPIO.OUT)
#GPIO.setup(26, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

#while (True):
    
    # Turn all relays ON
#    GPIO.output(4, GPIO.HIGH)
#    GPIO.output(22, GPIO.HIGH)
#    GPIO.output(6, GPIO.HIGH)
#    GPIO.output(26, GPIO.HIGH)
GPIO.output(4, GPIO.HIGH)
    # Sleep for 5 seconds
#    sleep(5) 
    # Turn all relays OFF
#    GPIO.output(4, GPIO.LOW)
#    GPIO.output(22, GPIO.LOW)
#    GPIO.output(6, GPIO.LOW)
#    GPIO.output(26, GPIO.LOW)   
#GPIO.output(26, GPIO.LOW)   
    # Sleep for 5 seconds
#    sleep(5)

GPIO.setup(5, GPIO.IN)
value = GPIO.input(5)
print(value)

sleep(5)

GPIO.cleanup()
