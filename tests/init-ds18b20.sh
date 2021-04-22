#!/bin/bash

sudo modprobe w1-gpio
sudo modprobe w1-therm
# sensor device folder
cd /sys/bus/w1/devices/28-0213167a79aa

# read the temperature
cat w1_slave
