#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# ::: Probe Reading
#
from flask import Flask, render_template
import os
import glob
import time

''' Set Global
'''
sonda1 = '28-0213167a79aa'
sonda2 = '28-021316aea0aa'

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
device_file_s1 = base_dir + sonda1 + '/w1_slave'
device_file_s2 = base_dir + sonda2 + '/w1_slave'

#print device_file_s1
#print device_file_s2

class ReadDevice():

    def __init__(self, device_file):
        self.device_file = device_file

    def read_temp_raw(self):
        with open(self.device_file, 'r') as f: lines = f.readlines()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        #print lines

        while lines[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
          temp_string = lines[1][equals_pos+2:]
          temp_c = float(temp_string) / 1000.0
          #temp_f = temp_c * 9.0 / 5.0 + 32.0
          #return temp_c, temp_f
          return temp_c

# while True:
#     #print(read_temp())
#     print('Sonda 1: ' + str(ReadDevice(device_file_s1).read_temp()) + '  ------- Sonda 2: ' + str(ReadDevice(device_file_s2).read_temp()))
#     #print(ReadDevice(device_file_s1).read_temp())
#     time.sleep(1)

#
# ::: Application Server
#
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Sonda 1: ' + str(ReadDevice(device_file_s1).read_temp())
    probes = [str(ReadDevice(device_file_s1).read_temp())]
    return render_template('index.html',probes=probes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
