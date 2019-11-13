from serial.tools.list_ports import comports as list_serial_ports
import serial
import time, microfs
from datetime import date, datetime


#print(int(data[0:8]))
#f.write(str(int(data[0:8])) + "\n")
#f.close()

def find_microbit():
    """
    Returns a tuple representation of the port and serial number for a
    connected micro:bit device. If no device is connected the tuple will be
    (None, None).
    """
    ports = list_serial_ports()
    for port in ports:
        if "VID:PID=0D28:0204" in port[2].upper():
            return (port[0], port.serial_number)
    return (None, None)

def getData():
    port = find_microbit()[0]
    baud = 115200
    s = serial.Serial(port)
    s.baudrate = baud
    data = s.readline()
    s.close()

    return str(data)

def get_templists():
    list_A = []
    list_B = []
    list_C = []
    list_D = []
    list_E = []
    list_F = []
    list_G = [] 
    list_H = [] 
    list_I = [] 
    list_J = []
    templist = [list_A, list_B, list_C, list_D, list_E,
                list_F, list_G, list_H, list_I, list_J]
    return templist

def get_lightlists():
    list_A = []
    list_B = []
    list_C = []
    list_D = []
    list_E = []
    list_F = []
    list_G = [] 
    list_H = [] 
    list_I = [] 
    list_J = []
    lightlist = [list_A, list_B, list_C, list_D, list_E,
                list_F, list_G, list_H, list_I, list_J]
    return lightlist

def get_timelists():
    list_A = []
    list_B = []
    list_C = []
    list_D = []
    list_E = []
    list_F = []
    list_G = [] 
    list_H = [] 
    list_I = [] 
    list_J = []
    timelist = [list_A, list_B, list_C, list_D, list_E,
                list_F, list_G, list_H, list_I, list_J]
    return timelist

def get_datelists():
    list_A = []
    list_B = []
    list_C = []
    list_D = []
    list_E = []
    list_F = []
    list_G = [] 
    list_H = [] 
    list_I = [] 
    list_J = []
    datelist = [list_A, list_B, list_C, list_D, list_E,
                list_F, list_G, list_H, list_I, list_J]
    return datelist

