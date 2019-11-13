#import serial
import time
from time import gmtime, strftime
import datalogger
import sqlsql
import os
import sqlsql

from flask import Flask, request, render_template
from datetime import date, datetime
from threading import Thread


class Sensor:
    nameList = ["Sensor:"]
    tempList = ["Temperature:"]
    linelist = []
    currentsensor = ""


date = strftime("%b-%d-%Y")

#open initially
f = open('size.txt', 'a')
f.close()
os.remove('size.txt')
f = open('size.txt', 'a')
f.close()
f = open('data.txt', 'a')
f.close()
os.remove('data.txt')
f = open("data.txt", "a")
f.close()

sqlsql.clean_All()

def toFile():
    i=0
    j=0
    while True: 
        #time.sleep(0.1)   
        f = open("data.txt", "a")
        data = datalogger.getData()
        temp, light, name = data[2:-5].split(' ')
        if Sensor.nameList.count(name) < 1:
            Sensor.nameList.append(name)
        i+=1
        afile = open("size.txt", "a")
        afile.write(str(len(Sensor.nameList)-1) + "\n")
        afile.close()
        # Sensor    temperature light   time    date
        f.write(name + '\t' + temp + '\t' + light + '\t' +
                strftime(strftime("%H:%M:%S", time.localtime())) + '\t' + date + '\n')
        f.close()

        f = open("data.txt", "r") 
        line = f.readlines()[-1]
        ssensor, tempr, llight, ttime, tdate = line.split('\t')
        f.close()
        #datalogger.logData(line)
        if(line[0] == "A"):
            sqlsql.table_A(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "B"):
            sqlsql.table_B(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "C"):
            sqlsql.table_C(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "D"):
            sqlsql.table_D(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "E"):
            sqlsql.table_E(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "F"):
            sqlsql.table_F(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "G"):
            sqlsql.table_G(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "H"):
            sqlsql.table_H(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "I"):
            sqlsql.table_I(ssensor, tempr, llight, ttime, tdate)
        elif(line[0] == "J"):
            sqlsql.table_J(ssensor, tempr, llight, ttime, tdate)

        j+=1

app = Flask(__name__)

time.sleep(1)
f = open("data.txt", "r")



@app.route("/")
def interface():
    
    sensorlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    templist = datalogger.get_templists()
    lightlist = datalogger.get_lightlists()
    timelist = datalogger.get_timelists()
    datelist = datalogger.get_datelists()

    sqlsql.clean_All()

    f = open("size.txt")
    size = f.readlines()[-1]
    f.close()

    data_A = sqlsql.get_lastA()
    for i in range(0,len(data_A)):
        datasplit = data_A[i]
        templist[0].append(datasplit[0])
        lightlist[0].append(datasplit[1])
        timelist[0].append(datasplit[2])
        datelist[0].append(datasplit[3])
    
    data_B = sqlsql.get_lastB()
    for i in range(0,len(data_B)):
        datasplit = data_B[i]
        templist[1].append(datasplit[0])
        lightlist[1].append(datasplit[1])
        timelist[1].append(datasplit[2])
        datelist[1].append(datasplit[3])
    
    data_C = sqlsql.get_lastC()
    for i in range(0,len(data_C)):
        datasplit = data_C[i]
        templist[2].append(datasplit[0])
        lightlist[2].append(datasplit[1])
        timelist[2].append(datasplit[2])
        datelist[2].append(datasplit[3])

    data_D = sqlsql.get_lastD()
    for i in range(0,len(data_D)):
        datasplit = data_D[i]
        templist[3].append(datasplit[0])
        lightlist[3].append(datasplit[1])
        timelist[3].append(datasplit[2])
        datelist[3].append(datasplit[3])

    data_E = sqlsql.get_lastE()
    for i in range(0,len(data_E)):
        datasplit = data_E[i]
        templist[4].append(datasplit[0])
        lightlist[4].append(datasplit[1])
        timelist[4].append(datasplit[2])
        datelist[4].append(datasplit[3])

    data_F = sqlsql.get_lastF()
    for i in range(0,len(data_F)):
        datasplit = data_F[i]
        templist[5].append(datasplit[0])
        lightlist[5].append(datasplit[1])
        timelist[5].append(datasplit[2])
        datelist[5].append(datasplit[3])

    data_G = sqlsql.get_lastG()
    for i in range(0,len(data_G)):
        datasplit = data_G[i]
        templist[6].append(datasplit[0])
        lightlist[6].append(datasplit[1])
        timelist[6].append(datasplit[2])
        datelist[6].append(datasplit[3])

    data_H = sqlsql.get_lastH()
    for i in range(0,len(data_H)):
        datasplit = data_H[i]
        templist[7].append(datasplit[0])
        lightlist[7].append(datasplit[1])
        timelist[7].append(datasplit[2])
        datelist[7].append(datasplit[3])

    data_I = sqlsql.get_lastI()
    for i in range(0,len(data_I)):
        datasplit = data_I[i]
        templist[8].append(datasplit[0])
        lightlist[8].append(datasplit[1])
        timelist[8].append(datasplit[2])
        datelist[8].append(datasplit[3])

    data_J = sqlsql.get_lastJ()
    for i in range(0,len(data_J)):
        datasplit = data_J[i]
        templist[9].append(datasplit[0])
        lightlist[9].append(datasplit[1])
        timelist[9].append(datasplit[2])
        datelist[9].append(datasplit[3])

    return render_template("interface.html", s=sensorlist, t=templist, l=lightlist, ct=timelist, d=datelist, len=int(size))

@app.route("/data")
def data():
    
    templist = datalogger.get_templists()
    lightlist = datalogger.get_lightlists()
    timelist = datalogger.get_timelists()
    datelist = datalogger.get_datelists()

    sqlsql.clean_All()

    f = open("size.txt")
    size = f.readlines()[-1]
    f.close()

    data_A = sqlsql.get_A()
    for i in range(0,len(data_A)):
        datasplit = data_A[i]
        templist[0].append(datasplit[0])
        lightlist[0].append(datasplit[1])
        timelist[0].append(datasplit[2])
        datelist[0].append(datasplit[3])
    
    data_B = sqlsql.get_B()
    for i in range(0,len(data_B)):
        datasplit = data_B[i]
        templist[1].append(datasplit[0])
        lightlist[1].append(datasplit[1])
        timelist[1].append(datasplit[2])
        datelist[1].append(datasplit[3])
    
    data_C = sqlsql.get_C()
    for i in range(0,len(data_C)):
        datasplit = data_C[i]
        templist[2].append(datasplit[0])
        lightlist[2].append(datasplit[1])
        timelist[2].append(datasplit[2])
        datelist[2].append(datasplit[3])

    data_D = sqlsql.get_D()
    for i in range(0,len(data_D)):
        datasplit = data_D[i]
        templist[3].append(datasplit[0])
        lightlist[3].append(datasplit[1])
        timelist[3].append(datasplit[2])
        datelist[3].append(datasplit[3])

    data_E = sqlsql.get_E()
    for i in range(0,len(data_E)):
        datasplit = data_E[i]
        templist[4].append(datasplit[0])
        lightlist[4].append(datasplit[1])
        timelist[4].append(datasplit[2])
        datelist[4].append(datasplit[3])

    data_F = sqlsql.get_F()
    for i in range(0,len(data_F)):
        datasplit = data_F[i]
        templist[5].append(datasplit[0])
        lightlist[5].append(datasplit[1])
        timelist[5].append(datasplit[2])
        datelist[5].append(datasplit[3])

    data_G = sqlsql.get_G()
    for i in range(0,len(data_G)):
        datasplit = data_G[i]
        templist[6].append(datasplit[0])
        lightlist[6].append(datasplit[1])
        timelist[6].append(datasplit[2])
        datelist[6].append(datasplit[3])

    data_H = sqlsql.get_H()
    for i in range(0,len(data_H)):
        datasplit = data_H[i]
        templist[7].append(datasplit[0])
        lightlist[7].append(datasplit[1])
        timelist[7].append(datasplit[2])
        datelist[7].append(datasplit[3])

    data_I = sqlsql.get_I()
    for i in range(0,len(data_I)):
        datasplit = data_I[i]
        templist[8].append(datasplit[0])
        lightlist[8].append(datasplit[1])
        timelist[8].append(datasplit[2])
        datelist[8].append(datasplit[3])

    data_J = sqlsql.get_J()
    for i in range(0,len(data_J)):
        datasplit = data_J[i]
        templist[9].append(datasplit[0])
        lightlist[9].append(datasplit[1])
        timelist[9].append(datasplit[2])
        datelist[9].append(datasplit[3])

    return render_template("data.html", t = templist, l = lightlist, ct = timelist, d = datelist, len=120, s=int(size))

if __name__ == "__main__":
    Thread(target = app.run).start()
    Thread(target = toFile).start()
    #app.run(debug=True)



    







