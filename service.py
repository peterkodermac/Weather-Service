import os
from flask import Flask
import glob
import sys
import subprocess

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]

device_file = device_folder + '/w1_slave'

portNumber=81 #PORT THAT WILL BE USED

app = Flask(__name__)

def read_temp_raw():
        catdata = subprocess.Popen(['cat',device_file], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = catdata.communicate()
        out_decode = out.decode('utf-8')
        lines = out_decode.split('\n')
        return lines


@app.route("/temp/")     #this  indicates the url, so this means server/temp/
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
	#return str(temp_f) #uncomment if you want to return Fahrenheit, comment next line
	return str(temp_c)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=portNumber, debug=True)
