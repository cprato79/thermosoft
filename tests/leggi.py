#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN)

value = GPIO.input(5)

print value

GPIO.cleanup()
