import random
import csv
import re
from functools import reduce
from tkinter import filedialog
from  tkinter import messagebox as ms
import tkinter as tk
import os
import sys
import miner as mn
s="#id x y"
listSenss = []
ListXySensCov=[]
ListSensorneigh=[]
ListCover=[]
ListPOI=[]
battery=""
radius=""
ALLPOICOV=[]
Poir=1 # Zmiana z 1
calcSensorID=[]
calcSensorID.append(s)
SquareArenas=40000
Pi=3.14
STATES=[]
AmountWSN=0
filename = ""
textsVariable=""
ListofNumbers=[]
amountReadWSN=0
helpVal=0
InitCounter=0 #Value HELPP OFF DOUBLE BUTTON
def InitGui():
        main_window =tk.Tk()
        global ListofNumbers
        global textsVariable
        global STATES
        ListofNumbers = []
        ListofNumbersCalcSingleq=[]
        converted_listCalcSingleq = []
        ListofNumbersCalcSingleqState=[]
        IdPOICOV=[]
        SensorHelper=[]
        SensorHelperPoiID=[]
        ListofNeighbour=[]
        global ListPOI
        tk.Label(text="X 0-100").pack(side="bottom")
        tk.Label(text="Y 0-100").pack(side="left")
        c = tk.Canvas(main_window, width=400, height=400, bg="white")
        c.pack(side="left")
        #POI 411
        #FIRST POI
        def OpenMYSensorStates(): #SENSOR ID FILE
                    global STATES
                    global amountReadWSN
                    if(len(ListofNumbers)>0):
                        ms.showinfo(title="Error", message="you have already loaded this file ! ! !")
                    else:
                        c.delete('all')
                        ExitButton = tk.Button(main_window, text="Next Page", command=Destroyer)
                        ExitButton.pack(side="right")
                        text_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                        text_file = open(text_file, 'r')
                        ListofNumbers.clear() #CLEAR LIST
                        for x in text_file:
                            if(x[2]==" "):
                                ListofNumbers.append(x[3:])
                            else:
                                ListofNumbers.append(x[2:])
                        ListofNumbers.pop(0)
                        global  filename
                        filename = text_file.name
                        print(ListofNumbers)
                        for x in ListofNumbers:
                            amountReadWSN = amountReadWSN + 1
                        ListPOI.clear()
                        if (str(variableRadio.get()) == '441'):
                            POIVALUE = 441
                        elif (str(variableRadio.get()) == '144'):
                            POIVALUE = 144
                        else:
                            POIVALUE = 36
                        with open("POI" + str(POIVALUE) + '.csv') as file:  # CHANGE TO PO 4412 /36
                            reader = csv.reader(file)
                            for row in reader:
                                ListPOI.append(row)
                        id = 1
                        for x in ListofNumbers:
                                try:
                                    xx=int(x[0:2])
                                except ValueError:
                                    xx =int(x[0:1])
                                try:
                                    yy=100 - int(x[5:7])
                                except ValueError:
                                    yy=100 - int(x[4:6])
                                try:
                                    state=int(x[10])
                                except ValueError:
                                    state=int(x[9])
                                STATES.append(int(state))
                                print(state)
                                if state=='0': # CHange '' char to int
                                        colo="red"
                                else:
                                        colo="green"
                                c.create_oval(int(xx) * 4, int(yy) * 4, int(xx) * 4 - 2, int(yy) * 4 + 2,
                                              stipple="gray50",
                                              fill="black", tags=id)
                                c.create_oval(int(xx) * 4 + int(radius.get()) * 4,
                                              int(yy) * 4 + int(radius.get()) * 4,
                                              int(xx) * 4 - int(radius.get()) * 4,
                                              int(yy) * 4 - int(radius.get()) * 4,
                                              stipple="gray50",
                                              outline=colo)
                                c.create_text(int(xx)*4 + 8,
                                              int(yy)*4 + 8,
                                              font="Times 10 italic bold", text=id)
                                id += 1
                        print(ListofNumbers)
                        RadioVariable = variableRadio.get()
                        longb = 5
                        i = 0
                        if (RadioVariable == "36"):
                            for x in range(6):
                                c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                                c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                                c.create_oval(0 + i, 133, 0 + i + longb, 138, fill="black")
                                c.create_oval(0 + i, 199, 0 + i + longb, 204, fill="black")
                                c.create_oval(0 + i, 265, 0 + i + longb, 270, fill="black")
                                c.create_oval(0 + i, 331, 0 + i + longb, 336, fill="black")
                                i = i + 66;
                        elif (RadioVariable == "144"):
                            for x in range(12):
                                c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                                c.create_oval(0 + i, 33, 0 + i + longb, 38, fill="black")
                                c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                                c.create_oval(0 + i, 99, 0 + i + longb, 104, fill="black")
                                c.create_oval(0 + i, 132, 0 + i + longb, 137, fill="black")
                                c.create_oval(0 + i, 165, 0 + i + longb, 170, fill="black")
                                c.create_oval(0 + i, 198, 0 + i + longb, 203, fill="black")
                                c.create_oval(0 + i, 231, 0 + i + longb, 236, fill="black")
                                c.create_oval(0 + i, 264, 0 + i + longb, 269, fill="black")
                                c.create_oval(0 + i, 297, 0 + i + longb, 302, fill="black")
                                c.create_oval(0 + i, 330, 0 + i + longb, 335, fill="black")
                                c.create_oval(0 + i, 363, 0 + i + longb, 368, fill="black")
                                c.create_oval(0 + i, 396, 0 + i + longb, 401, fill="black")
                                i = i + 33
                        elif (RadioVariable == "441"):
                            for x in range(20):
                                c.create_oval(0 + i, 0, 0 + i + longb, 2, fill="black")
                                c.create_oval(0 + i, 20, 0 + i + longb, 22, fill="black")
                                c.create_oval(0 + i, 40, 0 + i + longb, 42, fill="black")
                                c.create_oval(0 + i, 60, 0 + i + longb, 62, fill="black")
                                c.create_oval(0 + i, 80, 0 + i + longb, 82, fill="black")
                                c.create_oval(0 + i, 100, 0 + i + longb, 102, fill="black")
                                c.create_oval(0 + i, 120, 0 + i + longb, 122, fill="black")
                                c.create_oval(0 + i, 140, 0 + i + longb, 142, fill="black")
                                c.create_oval(0 + i, 160, 0 + i + longb, 162, fill="black")
                                c.create_oval(0 + i, 180, 0 + i + longb, 182, fill="black")
                                c.create_oval(0 + i, 200, 0 + i + longb, 202, fill="black")
                                c.create_oval(0 + i, 220, 0 + i + longb, 222, fill="black")
                                c.create_oval(0 + i, 240, 0 + i + longb, 242, fill="black")
                                c.create_oval(0 + i, 260, 0 + i + longb, 262, fill="black")
                                c.create_oval(0 + i, 280, 0 + i + longb, 282, fill="black")
                                c.create_oval(0 + i, 300, 0 + i + longb, 302, fill="black")
                                c.create_oval(0 + i, 320, 0 + i + longb, 322, fill="black")
                                c.create_oval(0 + i, 340, 0 + i + longb, 342, fill="black")
                                c.create_oval(0 + i, 360, 0 + i + longb, 362, fill="black")
                                c.create_oval(0 + i, 380, 0 + i + longb, 382, fill="black")
                                c.create_oval(0 + i, 400, 0 + i + longb, 402, fill="black")
                                i = i + 20
                        id+=1


        def OpenSensorWSN():
                    try:
                        if(len(ListofNumbers)>0):
                            ms.showinfo(title="Error", message="you have already loaded this file ! ! !")
                        else:
                            counter=0
                            text_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open TextFile",
                                                               filetypes=(("Text Files", "*.txt"),))
                            text_file = open(text_file, 'r')
                            # DELETE FIRST PARAMETER
                            for x in text_file:
                                if (counter>0):
                                    if(x[5:7]=="0."):
                                        ad = 100 - int(x[4:6])
                                        string_list = list(x)
                                        string_list[4:6] = str(ad)
                                        new_string = "".join(string_list)
                                        ListofNumbers.append(new_string)
                                    else:
                                        ad = 100 - int(x[5:7])
                                        string_list = list(x)
                                        string_list[5:7] = str(ad)
                                        new_string = "".join(string_list)
                                        ListofNumbers.append(new_string)
                                else:
                                    ListofNumbers.append(x)
                                counter=+1
                            ListofNumbers.pop(0)
                            for x in ListofNumbers:
                                    print(x)
                            global filename
                            filename = text_file.name
                    except:
                        ms.showinfo(title="ERROR",message="Read one more time")



        longb=2
        i=0

        for x in range(6):
            c.create_oval(0 + i, 0, 0 + i + longb, 4, fill="black")
            s = "" + str(0 + i / 4) + " " + str(0 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 66, 0 + i + longb, 70, fill="black")
            s = "" + str(0 + i / 4) + " " + str(68 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 134, 0 + i + longb, 138, fill="black")
            s = "" + str(0 + i / 4) + " " + str(136 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 200, 0 + i + longb, 204, fill="black")
            s = "" + str(0 + i / 4) + " " + str(202 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 264, 0 + i + longb, 270, fill="black")
            s = "" + str(0 + i / 4) + " " + str(268 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 332, 0 + i + longb, 336, fill="black")
            s = "" + str(0 + i / 4) + " " + str(334 / 4)
            ListPOI.append(s)
            i = i + 66;
        '''
        for x in range(12):
            c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
            s = "" + str(0 + i / 4) + " " + str(0 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 33, 0 + i + longb, 38, fill="black")
            s = "" + str(0 + i / 4) + " " + str(36 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
            s = "" + str(0 + i / 4) + " " + str(68 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 99, 0 + i + longb, 104, fill="black")
            s = "" + str(0 + i / 4) + " " + str(102 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 132, 0 + i + longb, 137, fill="black")
            s = "" + str(0 + i / 4) + " " + str(134 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 165, 0 + i + longb, 170, fill="black")
            s = "" + str(0 + i / 4) + " " + str(168 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 198, 0 + i + longb, 203, fill="black")
            s = "" + str(0 + i / 4) + " " + str(202 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 231, 0 + i + longb, 236, fill="black")
            s = "" + str(0 + i / 4) + " " + str(234 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 264, 0 + i + longb, 269, fill="black")
            s = "" + str(0 + i / 4) + " " + str(264 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 297, 0 + i + longb, 302, fill="black")
            s = "" + str(0 + i / 4) + " " + str(300 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 330, 0 + i + longb, 335, fill="black")
            s = "" + str(0 + i / 4) + " " + str(334 / 4)
            ListPOI.append(s)
            c.create_oval(0 + i, 363, 0 + i + longb, 368, fill="black")
            s = "" + str(0 + i / 4) + " " + str(366 / 4)
            ListPOI.append(s)
            i = i + 33
            '''
        '''
        # DLA POI 411 -------
        for x in range(21):
                c.create_oval(0 + i, 0, 0 + i + longb, 2, fill="black")
                s=""+str(0+i/4) + " " + str(0/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 20, 0 + i + longb, 22, fill="black")
                s = "" + str(0 + i/4) + " " + str(20/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 40, 0 + i + longb, 42, fill="black")
                s = "" + str(0 + i/4) + " " + str(40/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 60, 0 + i + longb, 62, fill="black")
                s = "" + str(0 + i/4) + " " + str(60/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 80, 0 + i + longb, 82, fill="black")
                s = "" + str(0 + i/4) + " " + str(80/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 100, 0 + i + longb, 102, fill="black")
                s = "" + str(0 + i/4) + " " + str(100/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 120, 0 + i + longb, 122, fill="black")
                s = "" + str(0 + i/4) + " " + str(120/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 140, 0 + i + longb, 142, fill="black")
                s = "" + str(0 + i/4) + " " + str(140/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 160, 0 + i + longb, 162, fill="black")
                s = "" + str(0 + i/4) + " " + str(160/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 180, 0 + i + longb, 182, fill="black")
                s = "" + str(0 + i/4) + " " + str(180/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 200, 0 + i + longb, 202, fill="black")
                s = "" + str(0 + i/4) + " " + str(200/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 220, 0 + i + longb, 222, fill="black")
                s = "" + str(0 + i/4) + " " + str(220/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 240, 0 + i + longb, 242, fill="black")
                s = "" + str(0 + i/4) + " " + str(240/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 260, 0 + i + longb, 262, fill="black")
                s = "" + str(0 + i/4) + " " + str(260/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 280, 0 + i + longb, 282, fill="black")
                s = "" + str(0 + i/4) + " " + str(280/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 300, 0 + i + longb, 302, fill="black")
                s = "" + str(0 + i/4) + " " + str(300/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 320, 0 + i + longb, 322, fill="black")
                s = "" + str(0 + i/4) + " " + str(320/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 340, 0 + i + longb, 342, fill="black")
                s = "" + str(0 + i/4) + " " + str(340/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 360, 0 + i + longb, 362, fill="black")
                s = "" + str(0 + i/4) + " " + str(360/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 380, 0 + i + longb, 382, fill="black")
                s = "" + str(0 + i/4) + " " + str(380/4)
                ListPOI.append(s)
                c.create_oval(0 + i, 400, 0 + i + longb, 402, fill="black")
                s = "" + str(0 + i/4) + " " + str(400/4)
                ListPOI.append(s)
                i = i + 2
                '''
                #X and Y
        #print(ListPOI)
                # ENTRY

        def SaveFile():
                        with open("RESULT/MYPOI .txt", 'w') as file:
                                for row in ListPOI:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')
        SaveFile()
        global radius
        radius = tk.StringVar()
        color = tk.StringVar()
        global battery
        battery = tk.StringVar()
        radius.set("35")
        color.set("0.5")
        battery.set("10")
                ######################################RADIO BUTTONS##################
        variableRadio = tk.StringVar(main_window, "36")
        def choice(text):
                variableRadio.set(text)
        valuesRadioPOI = {"POI 36": "36", "POI 144":"144", " POI 441" : "441"}
        variableRadio=tk.StringVar(main_window,"36")
        tk.Label(text="---Points of interests (POIs)---").pack()
        for (text, value) in valuesRadioPOI.items():
                        tk.Radiobutton(main_window, text=text, variable=variableRadio,
                                    value=value ,command=choice(value)).pack(ipady=5)
        amountReadWSN = 0
############ RIGHT GUI#########################
        tk.Label(text="---Sensor Parameters---").pack()
        ReadButton = tk.Button(main_window, text="Read WSN", command=OpenSensorWSN).pack()
        tk.Label(text="RADIUS").pack()
        radiusSens = tk.Entry(main_window,textvariable =radius ,width=10, borderwidth=5).pack()
        tk.Label(text="Battery Capacity").pack()
        batteryCapacity = tk.Entry(main_window, textvariable=battery, width=10, borderwidth=5).pack()
        tk.Label(text="---ACTIVE Sensor---").pack()
        tk.Label(text="Probabilistic").pack()
        ReadButtonOnOF = tk.Button(main_window, text="Read WSN ON/OFF", command=OpenMYSensorStates).pack()
        tk.Label(text="Randomly % Sensor Activity VALUE: 0-1").pack()
        propabilityEntry = tk.Entry(main_window, textvariable=color, width=10, borderwidth=5).pack()
# INICJACJA
        def Init():
            if(len(ListofNumbers)==0 or len(ListofNumbers[0])>11):
                ms.showinfo(title="Error", message="failed to load the WSN file -> Read WSN")
            else:
                c.delete('all')
                sensorId=0
                listSens= []
                global STATES
                global InitCounter
                global amountReadWSN
                amountReadWSN = 0
                STATES.clear()
                if (InitCounter==0):
                    ExitButton = tk.Button(main_window, text="Next Page", command=Destroyer)
                    ExitButton.pack(side="right")
                    SaveButton = tk.Button(main_window, text="cal sensor ID", command=SaveFileSens)
                    SaveButton.pack(side="left")
                    InitCounter=+1
                #List which save param for
                for x in ListofNumbers:
                    amountReadWSN = amountReadWSN + 1
                ListPOI.clear()
                if (str(variableRadio.get()) == '441'):
                    POIVALUE = 441
                elif (str(variableRadio.get()) == '144'):
                    POIVALUE = 144
                else:
                    POIVALUE = 36
                with open("POI" + str(POIVALUE) + '.csv') as file:  # CHANGE TO PO 4412 /36
                    reader = csv.reader(file)
                    for row in reader:
                       # print(row)
                        ListPOI.append(row)
                # COLOR FOR CIRCLE
                id = 1
                calcSensorID.clear()
                calcSensorID.append("#id x y")
                for x in ListofNumbers:
                    rand = random.uniform(0, 1)
                    if (rand < float(color.get())):
                                    xval = int(re.search(r'\d+', x[0:2]).group())
                                    STATES.append(1) # ADD OF SENSOR
                                    yval = int(re.search(r'\d+', x[5:7]).group())
                                    sensorId +=1
                                    s2 = c.create_oval(xval*4 + int(radius.get()) * 4,
                                                   yval*4 + int(radius.get()) * 4,
                                                   xval*4 - int(radius.get()) * 4,
                                                   yval*4 - int(radius.get()) * 4, stipple="gray12",
                                                   outline="Green",
                                                    tags=sensorId)
                                    s1 = c.create_oval(xval*4-2, yval*4-2, xval*4+2 , yval*4+2, stipple="gray12" ,
                                                                             outline="Green",
                                                                                fill="light green",tags=sensorId)
                                    s3 = c.create_text(xval*4 + 8,
                                                   yval*4 + 8,
                                                   font="Times 10 italic bold", text=sensorId)
                                    s = str(id) + " " + str(round(int(xval))) + ".0 " + str(round(int(yval))) + ".0 "+ "1" # STATE - green = 1
                                    calcSensorID.append(s)
                                    #print(calcSensorID)
                                    id += 1;

                    else :
                                    xval = int(re.search(r'\d+', x[0:2]).group())
                                    STATES.append(0) # ADD OFF SENSOR
                                    yval = int(re.search(r'\d+', x[5:7]).group())
                                    sensorId += 1
                                    s2 = c.create_oval(xval * 4 + int(radius.get()) * 4,
                                           yval * 4 + int(radius.get()) * 4,
                                           xval * 4 - int(radius.get()) * 4,
                                           yval * 4 - int(radius.get()) * 4, stipple="gray12",
                                           outline="Red",
                                           tags=sensorId)
                                    s1 = c.create_oval(xval * 4 - 2, yval * 4 - 2, xval * 4 + 2, yval * 4 + 2, stipple="gray12",
                                           outline="Green",
                                           fill="light green", tags=sensorId)
                                    s3 = c.create_text(xval * 4 + 8,
                                           yval * 4 + 8,
                                           font="Times 10 italic bold", text=sensorId)
                                    s = str(id) + " " + str(round(int(xval))) + ".0 " + str(round(int(yval))) + ".0 " + "0"
                                    calcSensorID.append(s)
                                    #print(calcSensorID)
                                    id += 1;
                RadioVariable = variableRadio.get()
                longb = 5
                i = 0
                if(RadioVariable=="36"):
                                for x in range(6):
                                                c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                                                c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                                                c.create_oval(0 + i, 133, 0 + i + longb, 138, fill="black")
                                                c.create_oval(0 + i, 199, 0 + i + longb, 204, fill="black")
                                                c.create_oval(0 + i, 265, 0 + i + longb, 270, fill="black")
                                                c.create_oval(0 + i, 331, 0 + i + longb, 336, fill="black")
                                                i = i + 66;
                elif (RadioVariable == "144"):
                                        for x in range(12):
                                                c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                                                c.create_oval(0 + i, 33, 0 + i + longb, 38, fill="black")
                                                c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                                                c.create_oval(0 + i, 99, 0 + i + longb, 104, fill="black")
                                                c.create_oval(0 + i, 132, 0 + i + longb, 137, fill="black")
                                                c.create_oval(0 + i, 165, 0 + i + longb, 170, fill="black")
                                                c.create_oval(0 + i, 198, 0 + i + longb, 203, fill="black")
                                                c.create_oval(0 + i, 231, 0 + i + longb, 236, fill="black")
                                                c.create_oval(0 + i, 264, 0 + i + longb, 269, fill="black")
                                                c.create_oval(0 + i, 297, 0 + i + longb, 302, fill="black")
                                                c.create_oval(0 + i, 330, 0 + i + longb, 335, fill="black")
                                                c.create_oval(0 + i, 363, 0 + i + longb, 368, fill="black")
                                                c.create_oval(0 + i, 396, 0 + i + longb, 401, fill="black")
                                                i = i + 33
                elif (RadioVariable == "441"):
                                        for x in range(20):
                                                c.create_oval(0 + i, 0, 0 + i + longb, 2, fill="black")
                                                c.create_oval(0 + i, 20, 0 + i + longb, 22, fill="black")
                                                c.create_oval(0 + i, 40, 0 + i + longb, 42, fill="black")
                                                c.create_oval(0 + i, 60, 0 + i + longb, 62, fill="black")
                                                c.create_oval(0 + i, 80, 0 + i + longb, 82, fill="black")
                                                c.create_oval(0 + i, 100, 0 + i + longb, 102, fill="black")
                                                c.create_oval(0 + i, 120, 0 + i + longb, 122, fill="black")
                                                c.create_oval(0 + i, 140, 0 + i + longb, 142, fill="black")
                                                c.create_oval(0 + i, 160, 0 + i + longb, 162, fill="black")
                                                c.create_oval(0 + i, 180, 0 + i + longb, 182, fill="black")
                                                c.create_oval(0 + i, 200, 0 + i + longb, 202, fill="black")
                                                c.create_oval(0 + i, 220, 0 + i + longb, 222, fill="black")
                                                c.create_oval(0 + i, 240, 0 + i + longb, 242, fill="black")
                                                c.create_oval(0 + i, 260, 0 + i + longb, 262, fill="black")
                                                c.create_oval(0 + i, 280, 0 + i + longb, 282, fill="black")
                                                c.create_oval(0 + i, 300, 0 + i + longb, 302, fill="black")
                                                c.create_oval(0 + i, 320, 0 + i + longb, 322, fill="black")
                                                c.create_oval(0 + i, 340, 0 + i + longb, 342, fill="black")
                                                c.create_oval(0 + i, 360, 0 + i + longb, 362, fill="black")
                                                c.create_oval(0 + i, 380, 0 + i + longb, 382, fill="black")
                                                c.create_oval(0 + i, 400, 0 + i + longb, 402, fill="black")
                                                i = i + 20
                listSenss.extend(listSens)

        def Exit():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)

        def SaveFileSens():
                        with open("RESULT/sensorId.txt", 'w') as file:
                                for row in calcSensorID:
                                        s = "".join(map(str, row))
                                        file.write(s + '\n')

        def donothing():  # HELPER
                        x = 0

        POIVALUE=0
        def OpenMYSensorNeighbour(): #find WSN grapph
                        c.delete('all')
                        #ListofNumbers.clear()
                        #
                        if (len(ListofNumbers) == 0):
                            ms.showinfo(title="Error", message="failed to load the WSN file -> Read WSN first ...")
                        # LIST NEIGTBOUR
                        ListSensorneigh.append("#parameters of run: ")
                        ListSensorneigh.append("#Number of Sensors " + str(amountReadWSN))
                        ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
                        ListSensorneigh.append("#POI: "+str(variableRadio.get()))
                        ListSensorneigh.append("#Sensor for file: " + str(filename))
                        ListSensorneigh.append("#id num_of_neighb neigb-ID")
                        id = 1
                        for x in ListofNumbers:
                                xx = int(re.search(r'\d+', x[0:2]).group())
                                yy = int(re.search(r'\d+', x[5:7]).group())
                                c.create_oval(int(xx) * 4-2, int(yy) * 4-2, int(xx) * 4 + 2,
                                              int(yy) * 4 + 2, stipple="gray50",
                                              outline="green",fill="green", width=1)
                                c.create_oval(int(xx) * 4 - (int(radius.get())*4),
                                              int(yy) * 4 - (int(radius.get())*4),
                                              int(xx) * 4 + (int(radius.get())*4),
                                              int(yy) * 4 + (int(radius.get())*4),
                                              outline="Green", tags=id)
                                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                                              font="Times 10 italic bold", text=id)
                                id += 1;

                        def circle(x1, y1, x2, y2, r1, r2):
                            distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                            radSumSq = (r1 + r2) * (r1 + r2)
                            if (distSq == radSumSq):
                                return 1
                            elif (distSq > radSumSq):
                                return -1
                            else:
                                return 0

                        ys = ""
                        counter = 1
                        for x in ListofNumbers:
                            id=1
                            helper = 0
                            for y in ListofNumbers:
                                    ListofNeighbour.append(str(id) + str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),int(radius.get()),int(radius.get()))))
                                    xs=str(id) + str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(re.search(r'\d+', y[0:2]).group()),int(re.search(r'\d+', y[5:7]).group()),int(radius.get()),int(radius.get())))
                                    beng='-'
                                    if(beng in xs or  str(counter) == xs[0:1] or str(counter) == xs[0:2]):
                                        donothing()
                                    else:
                                        if(len(xs)<3):
                                            ys+=xs[0] + " "
                                            helper=helper+1
                                        else:
                                            ys+=xs[0:2] + " "
                                            helper = helper + 1
                                    id = id + 1
                            ListSensorneigh.append(str(counter) + "    "+str(helper) + "     " +ys)
                            ys=" "
                            ListofNeighbour.clear()
                            counter=counter+1
                        #print(ListSensorneigh)
                        def SaveFileSenss():
                            with open("RESULT/sensor-neighbours"+str(len(ListofNumbers))+".txt", 'w') as file:
                                for row in ListSensorneigh:
                                    s = "".join(map(str, row))
                                    file.write(s + '\n')
                        SaveFileSenss()


        def CalcSingleq():
            # calc single q
            counter = 0
            SensorStates=[]
            ListofNumbers.clear()
            IdPOICOV.clear()
            global ListPOI
            ListPOI.clear()
            ListSensorneigh.clear()
            converted_listCalcSingleq.clear()
            ListofNumbersCalcSingleq.clear()
            ListofNumbersCalcSingleqState.clear()
            if (str(variableRadio.get())=='441'):
                POIVALUE=441
            elif (str(variableRadio.get()) == '144'):
                POIVALUE=144
            else:
                POIVALUE=36
            with open( "POI"+str(POIVALUE)+'.csv') as file:  # CHANGE TO PO 4412 /36
                reader=csv.reader(file)
                for row in reader:
                    #print(row)
                    ListPOI.append(row)

            ms.showinfo(title=None, message="Read Sensor States -> \"sensor-states-10\" ")
            text_fileq = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open TextFile",
                                                  filetypes=(("Text Files", "*.txt"),))
            text_fileq = open(text_fileq, 'r')

            state = []
            #text_fileq = open("FILES/sensor-states-10.txt") #do usuniecia potem STEJTY
            for x in text_fileq:
                ListofNumbersCalcSingleqState.append(x)
                state.append(x[12])
            ListofNumbersCalcSingleqState.pop(0)
            state.pop(0)
            # print(ListofNumbersCalcSingleqState)
            # print(state)

            ms.showinfo(title=None, message="Read WSN FILE ->\"WSN-5d\"")
            text_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open TextFile",
                                                   filetypes=(("Text Files", "*.txt"),))
            text_file = open(text_file, 'r')
            variableAm = 0
            #text_file = open("FILES/WSN-5d.txt")
            for x in text_file:
                    ListofNumbersCalcSingleq.append(x)
            ListofNumbersCalcSingleq.pop(0)
            for x in ListofNumbersCalcSingleq:
                converted_listCalcSingleq.append(x.strip())
                variableAm+=1
            for i in range(len(converted_listCalcSingleq)):
                converted_listCalcSingleq[i]+= state[i]
            #print(converted_listCalcSingleq)

            # LIST NEIGTBOUR
            ListSensorneigh.append("#parameters of run: ")
            ListSensorneigh.append("#Number of Sensors " +str(variableAm))
            ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
            ListSensorneigh.append("#POI: " + str(variableRadio.get()))
            ListSensorneigh.append("#Sensor for file: " + str(text_file.name))
            ListSensorneigh.append("Sensor for file: :WSN-5d-test0.txt")
            ListSensorneigh.append("#q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
            id = 1
            c.delete('all')
            RadioVariable = variableRadio.get()
            if (RadioVariable == "36"):
                for x in range(6):
                    c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                    c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                    c.create_oval(0 + i, 133, 0 + i + longb, 138, fill="black")
                    c.create_oval(0 + i, 199, 0 + i + longb, 204, fill="black")
                    c.create_oval(0 + i, 265, 0 + i + longb, 270, fill="black")
                    c.create_oval(0 + i, 331, 0 + i + longb, 336, fill="black")
                    i = i + 66;
            elif (RadioVariable == "144"):
                for x in range(12):
                    c.create_oval(0 + i, 0, 0 + i + longb, 5, fill="black")
                    c.create_oval(0 + i, 33, 0 + i + longb, 38, fill="black")
                    c.create_oval(0 + i, 66, 0 + i + longb, 71, fill="black")
                    c.create_oval(0 + i, 99, 0 + i + longb, 104, fill="black")
                    c.create_oval(0 + i, 132, 0 + i + longb, 137, fill="black")
                    c.create_oval(0 + i, 165, 0 + i + longb, 170, fill="black")
                    c.create_oval(0 + i, 198, 0 + i + longb, 203, fill="black")
                    c.create_oval(0 + i, 231, 0 + i + longb, 236, fill="black")
                    c.create_oval(0 + i, 264, 0 + i + longb, 269, fill="black")
                    c.create_oval(0 + i, 297, 0 + i + longb, 302, fill="black")
                    c.create_oval(0 + i, 330, 0 + i + longb, 335, fill="black")
                    c.create_oval(0 + i, 363, 0 + i + longb, 368, fill="black")
                    c.create_oval(0 + i, 396, 0 + i + longb, 401, fill="black")
                    i = i + 33
            elif (RadioVariable == "441"):
                for x in range(20):
                    c.create_oval(0 + i, 0, 0 + i + longb, 2, fill="black")
                    c.create_oval(0 + i, 20, 0 + i + longb, 22, fill="black")
                    c.create_oval(0 + i, 40, 0 + i + longb, 42, fill="black")
                    c.create_oval(0 + i, 60, 0 + i + longb, 62, fill="black")
                    c.create_oval(0 + i, 80, 0 + i + longb, 82, fill="black")
                    c.create_oval(0 + i, 100, 0 + i + longb, 102, fill="black")
                    c.create_oval(0 + i, 120, 0 + i + longb, 122, fill="black")
                    c.create_oval(0 + i, 140, 0 + i + longb, 142, fill="black")
                    c.create_oval(0 + i, 160, 0 + i + longb, 162, fill="black")
                    c.create_oval(0 + i, 180, 0 + i + longb, 182, fill="black")
                    c.create_oval(0 + i, 200, 0 + i + longb, 202, fill="black")
                    c.create_oval(0 + i, 220, 0 + i + longb, 222, fill="black")
                    c.create_oval(0 + i, 240, 0 + i + longb, 242, fill="black")
                    c.create_oval(0 + i, 260, 0 + i + longb, 262, fill="black")
                    c.create_oval(0 + i, 280, 0 + i + longb, 282, fill="black")
                    c.create_oval(0 + i, 300, 0 + i + longb, 302, fill="black")
                    c.create_oval(0 + i, 320, 0 + i + longb, 322, fill="black")
                    c.create_oval(0 + i, 340, 0 + i + longb, 342, fill="black")
                    c.create_oval(0 + i, 360, 0 + i + longb, 362, fill="black")
                    c.create_oval(0 + i, 380, 0 + i + longb, 382, fill="black")
                    c.create_oval(0 + i, 400, 0 + i + longb, 402, fill="black")
                    i = i + 20
            for x in converted_listCalcSingleq:
                xx = int(re.search(r'\d+', x[0:2]).group())
                yy = int(re.search(r'\d+', x[5:7]).group())
                state=(str(int(re.search(r'\d+', x[8:]).group())))
                #print(state)
                if state == '0':
                    colo = "red"
                else:
                    colo = "green"
                c.create_oval(int(xx) * 4 - 2, int(yy) * 4 - 2, int(xx) * 4 + 2,
                              int(yy) * 4 + 2, stipple="gray50",
                              outline="green", fill="green", width=1)
                c.create_oval(int(xx) * 4 - (int(radius.get()) * 4),
                              int(yy) * 4 - (int(radius.get()) * 4),
                              int(xx) * 4 + (int(radius.get()) * 4),
                              int(yy) * 4 + (int(radius.get()) * 4),
                              outline=colo, tags=id)
                c.create_text(int(xx) * 4 + 15, int(yy) * 4 + 15,
                              font="Times 10 italic bold", text=id)
                SensorStates.append(state)
                id += 1;

            #print(ListSensorneigh)
            als = "" # Value helper
            def circle(x1, y1, x2, y2, r1, r2):
                distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                radSumSq = (r1 + r2) * (r1 + r2)
                if (distSq == radSumSq):
                    return 1
                elif (distSq > radSumSq):
                    return -1
                else:
                    return 0

            #POI TO 1d ARRAY
            flaten_list=reduce(lambda z, y :z + y,ListPOI)
            ids = 1
            # Coverage each sensor POI
            for x in converted_listCalcSingleq:
                helper = 0
                for y in flaten_list:
                    if(y[0]=='0'or y[0:2]=='5;' or y[0:2]=='8;'): #SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                        SensorHelper.append(str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(y[0]),  int(y[2:]), int(radius.get()),Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(y[0]),  int(y[2:]), int(radius.get()),Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1 #VALUE WHEN SENSOR STATE IS 1
                    elif(y[0:3]=='100'):
                        SensorHelper.append(
                            str(circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),int(y[0:3]),  int(y[4:]), int(radius.get()), Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1
                    else:
                        SensorHelper.append(
                            str(circle(int(re.search(r'\d+', x[0:2]).group()),  int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]), int(radius.get()), Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()),  int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]), int(radius.get()), Poir))
                        if(ys[0]=='0'):
                            donothing()
                        else:
                            helper+=1

                coverage=POIVALUE-helper # ZMINA Z 411
                IdPOICOV.append(str(coverage)) # ID + AMOUNT OF
                pom=0
                for x in SensorHelper:
                    ALLPOICOV.append(x)
                    SensorHelperPoiID.append(x+ " - " + str(pom))
                    pom=pom+1
               # ALLPOICOV.extend(SensorHelper)
                ids += 1
                SensorHelper.clear()
            ########################################## END POI AMOUNT####################
            chunkser = [ALLPOICOV[x:x + POIVALUE] for x in range(0, len(ALLPOICOV), POIVALUE)] #
            chunkserPoi=[SensorHelperPoiID[x:x + POIVALUE] for x in range(0, len(SensorHelperPoiID), POIVALUE)] # POI in EVERY SENSEOR
            '''
            print(chunkser)
            print("POI COV")
            print(ALLPOICOV)
            print("COVEREGE SENSOR BY POI")
            print(IdPOICOV)
            '''
            idstates=0
            arubaCloud=[]
            counterchuk=0
            amount=0
            abc=""
            for x in SensorStates:
                if(x=='0'):
                    donothing()
                else:
                    trucrypt = chunkser[counterchuk]
                    for y in chunkser:
                        printerek=0
                        amount = 0
                        for z in y:
                                if(trucrypt[printerek]==z):
                                    if(z=='0' ): #and trucrypt != y
                                        amount=amount+1
                                        arubaCloud.append(str(printerek)) # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek=printerek+1
                        abc += str(idstates)+ "-" + str(amount) + "\n" #AMOUNT + STATES ON
                counterchuk=counterchuk+1
                idstates=idstates+1
            finalStates=dict.fromkeys(arubaCloud) #DELETE DUPLICATE
            #COVERAGE Q
            coverageQ=len(finalStates)/POIVALUE
            # COVERAGE EVERY Q
            qoverageString=0
            Lista = []
            strPoi=""
            for x in chunkserPoi:
                for y in x:
                    if(y[0:2]=='-1'):
                        donothing()
                    else:
                        strPoi+=y+"."
                Lista.append(strPoi) # WSZYSTKIe POI ID z Pokryciem
                strPoi=""

            def calsum(l):
                # returning sum of list using List comprehension
                return sum([int(i) for i in l if type(i) == int or i.isdigit()])
            # DLA 36 trening
            ListwihCov=[]
            asa="0"
            ListwihCovPercent=[]
            idCoverage=1
            for x in Lista:
                    abc=x.split('.')
                    helperCov=0
                    for z in abc:
                        for y in finalStates:
                            if(z[4:]==y):
                                helperCov=helperCov+1
                    asa= str(helperCov)    #str(helperCov - calsum(ListwihCov))
                    abc.clear()
                    idCoverage+=1
                    #Calculate % POV
                    ListwihCov.append(asa)
            # LIST CALCULATION
            z=[int(x) for x in ListwihCov]
            x=([int(x) for x in IdPOICOV])
            products = [a / b for a, b in zip(z, x)]
            #print(products)
            #CALC SENSOR ID TO TXT
            ListSensorneigh.append(str(round(coverageQ,2)) + "  " + "10   " + ' '.join(SensorStates) + "   " + '  '.join(str(round(e,1)) for e in products))
            '''
            print("COVERAGE Q")
            print(ListSensorneigh)

            print("ASA")
            print(IdPOICOV)
            print(ListwihCov)
            print("STR POI")
            print(strPoi)
            print(Lista)
            print("ARUBA")
            print(arubaCloud)
            print("PO KONWERSJI")
            print(list(finalStates))
            '''


            def SaveFileSenss():
                with open("RESULT/creates cov-5-WSN-"+str(len(ListofNumbersCalcSingleqState))+"d.txt"
                          "", 'w') as file:
                    for row in ListSensorneigh:
                        s = "".join(map(str, row))
                        file.write(s + '\n')
            SaveFileSenss()
                ###########################################################################################

        def CalcALLq():  # calc single q
            SensorStates=[]
            ListPOI.clear()
            IdPOICOV.clear()
            counter = 0
            ListofNumbers.clear()
            ListSensorneigh.clear()
            converted_listCalcSingleq.clear()
            ListofNumbersCalcSingleq.clear()
            if (str(variableRadio.get()) == '441'):
                POIVALUE = 441
            elif (str(variableRadio.get()) == '144'):
                POIVALUE = 144
            else:
                POIVALUE = 36
            with open("POi"+str(POIVALUE)+'.csv') as file:  # CHANGE TO PO 4412
                reader=csv.reader(file)
                for row in reader:
                    #print(row)
                    ListPOI.append(row)

            ms.showinfo(title=None, message="READ WSN FILE")
            text_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open TextFile",
                                                   filetypes=(("Text Files", "*.txt"),))
            variableAm = 0
            text_file = open(text_file, 'r')
            for x in text_file:
                if (counter > 0):
                    if (x[5:7] == "0."):
                        ad = 100 - int(x[4:6])
                        string_list = list(x)
                        string_list[4:6] = str(ad)
                        new_string = "".join(string_list)
                        ListofNumbers.append(new_string)
                    else:
                        ad = 100 - int(x[5:7])
                        string_list = list(x)
                        string_list[5:7] = str(ad)
                        new_string = "".join(string_list)
                        ListofNumbers.append(new_string)
                else:
                    ListofNumbersCalcSingleq.append(x)
                counter = +1
            ListofNumbersCalcSingleq.pop(0)
            for x in ListofNumbersCalcSingleq:
                converted_listCalcSingleq.append(x.strip())
                variableAm += 1

            ListSensorneigh.clear()
            # LIST NEIGTBOUR
            ListSensorneigh.append("#parameters of run: ")
            ListSensorneigh.append("#Number of Sensors " + str(variableAm))
            ListSensorneigh.append("#Sensor Range: " + str(radius.get()))
            ListSensorneigh.append("#POI: " + str(variableRadio.get()))
            ListSensorneigh.append("#Sensor for file: " + str(text_file.name))
            ListSensorneigh.append("Sensor states for file: not appiled")
            ListSensorneigh.append("#id q    s    1 2 3 4 5   q1   q2   q3   q4   q5 ...")
            id = 1

            #print(ListSensorneigh)
            def circle(x1, y1, x2, y2, r1, r2):
                distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                radSumSq = (r1 + r2) * (r1 + r2)
                if (distSq == radSumSq):
                    return 1
                elif (distSq > radSumSq):
                    return -1
                else:
                    return 0

            #POI TO 1d ARRAY
            flaten_list=reduce(lambda z, y :z + y,ListPOI)
            ids = 1
            # OBLICZANIE POKRYCIE KAŻDEGO SENSORA
            for x in converted_listCalcSingleq:
                helper = 0
                for y in flaten_list:
                    if(y[0]=='0'or y[0:2]=='5;' or y[0:2]=='8;'): #SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                        SensorHelper.append(str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(y[0]),  int(y[2:]), int(radius.get()),Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()),int(re.search(r'\d+', x[5:7]).group()), int(y[0]),  int(y[2:]), int(radius.get()),Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1 #VALUE WHEN SENSOR STATE IS 1
                    elif(y[0:3]=='100'):
                        SensorHelper.append(
                            str(circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()) ,int(y[0:3]),  int(y[4:]), int(radius.get()), Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),int(y[0:3]),  int(y[4:]), int(radius.get()), Poir))
                        if (ys[0] == '0'):
                            donothing()
                        else:
                            helper += 1
                    else:
                        SensorHelper.append(
                            str(circle(int(re.search(r'\d+', x[0:2]).group()),  int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]), int(radius.get()), Poir)))
                        ys=str(circle(int(re.search(r'\d+', x[0:2]).group()),  int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]), int(radius.get()), Poir))
                        if(ys[0]=='0'):
                            donothing()
                        else:
                            helper+=1

                coverage=POIVALUE-helper # ZMINA Z 411
                IdPOICOV.append(str(coverage)) # ID + AMOUNT OF
                pom=0
                for x in SensorHelper:
                    ALLPOICOV.append(x)
                    SensorHelperPoiID.append(x+ " - " + str(pom))
                    pom=pom+1
               # ALLPOICOV.extend(SensorHelper)
                ids += 1
                SensorHelper.clear()
            ########################################## END POI AMOUNT####################
            chunkser = [ALLPOICOV[x:x + POIVALUE] for x in range(0, len(ALLPOICOV), POIVALUE)] # ZMIANA Z 411
            chunkserPoi=[SensorHelperPoiID[x:x + POIVALUE] for x in range(0, len(SensorHelperPoiID), POIVALUE)] # POI in EVERY SENSEOR
            #print(chunkser)
            #rint("POI COV")
            #print(ALLPOICOV)
            #print("COVEREGE SENSOR BY POI")
            #print(IdPOICOV)
            idstates=0
            arubaCloud=[]
            counterchuk=0
            amount=0
            idAllq = 0
            abc=""
            #FORMAT
            BinaryList=[]
            tempBinary=""
            # BINARKA DO POPRAWY ListofNumbersCalcSingleq
            #12-4095, 10-1023]
            if(len(ListofNumbersCalcSingleq)==10):
                for x in range (0,1024):
                    Binary='{:010b}'.format(x)
                    BinaryList.append(Binary)
                #print(BinaryList)
            elif(len(ListofNumbersCalcSingleq)==5):
                for x in range (0,32):
                    Binary='{:05b}'.format(x)
                    BinaryList.append(Binary)
                #print(BinaryList)
            elif (len(ListofNumbersCalcSingleq) == 12):
                for x in range(0, 4096):
                    Binary = '{:12b}'.format(x)
                    BinaryList.append(Binary)
            elif (len(ListofNumbersCalcSingleq) == 7):
                for x in range(0, 128):
                    Binary = '{:07b}'.format(x)
                    BinaryList.append(Binary)
            elif (len(ListofNumbersCalcSingleq) == 6):
                for x in range(0, 64):
                    Binary = '{:06b}'.format(x)
                    BinaryList.append(Binary)
            elif (len(ListofNumbersCalcSingleq) == 8):
                for x in range(0, 256):
                    Binary = '{:08b}'.format(x)
                    BinaryList.append(Binary)
            elif (len(ListofNumbersCalcSingleq) == 9):
                for x in range(0, 512):
                    Binary = '{:09b}'.format(x)
                    BinaryList.append(Binary)
            elif (len(ListofNumbersCalcSingleq) == 11):
                for x in range(0, 2048):
                    Binary = '{:11b}'.format(x)
                    BinaryList.append(Binary)
            else:
                ms.showerror("Error", "This option is for WSN x> 5 and x <12. If you choose 45 a program spends a lot of time computing ")
            for x in BinaryList:
             abde=x
             arubaCloud.clear()
             for z in x:
                abfsd=0
                if(z=='0'):
                    donothing()
                else:
                    trucrypt = chunkser[counterchuk]
                    for y in chunkser:
                        printerek=0
                        amount = 0
                        for z in y:
                                if(trucrypt[printerek]==z):
                                    if(z=='0' ): #and trucrypt != y
                                        amount=amount+1
                                        arubaCloud.append(str(printerek)) # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek=printerek+1
                       # abc += str(idstates)+ "-" + str(amount) + "\n" #AMOUNT + STATES ON
                counterchuk=counterchuk+1
                 # IMPORTANT FOR
             finalStates = dict.fromkeys(arubaCloud)  # DELETE DUPLICATE
             # COVERAGE Q
             coverageQ = len(finalStates) / POIVALUE
             # COVERAGE EVERY Q
             qoverageString = 0
             Lista = []
             strPoi = ""
             for x in chunkserPoi:
                 for y in x:
                     if (y[0:2] == '-1'):
                         donothing()
                     else:
                         strPoi += y + "."
                 Lista.append(strPoi)  # WSZYSTKIe POI ID z Pokryciem
                 strPoi = ""

             def calsum(l):
                 # returning sum of list using List comprehension
                 return sum([int(i) for i in l if type(i) == int or i.isdigit()])

             # DLA 36 trening
             ListwihCov = []
             asa = "0"
             ListwihCovPercent = []
             idCoverage = 1
             for x in Lista:
                 abc = x.split('.')
                 helperCov = 0
                 for z in abc:
                     for y in finalStates:
                         if (z[4:] == y):
                             helperCov = helperCov + 1
                 asa = str(helperCov)  # str(helperCov - calsum(ListwihCov))
                 abc.clear()
                 idCoverage += 1
                 # Calculate % POV
                 ListwihCov.append(asa)
             # LIST CALCULATION
             z = [int(x) for x in ListwihCov]
             x = ([int(x) for x in IdPOICOV])
             products = [a / b for a, b in zip(z, x)]
             print(products)
             # CALC SENSOR ID TO TXT

             counterchuk=0
             idstates=idstates+1
             ListSensorneigh.append(str(idAllq) + " " + str(round(coverageQ, 2)) + "  " + str(idAllq)+ "    " + abde+  '  '.join(
             SensorStates) + "   " + '  '.join(str(round(e, 1)) for e in products))
             idAllq+=1


            def SaveFileSenss():
                with open("RESULT/creates all-WSN-"+str(len(ListofNumbersCalcSingleq))+".txt"
                          "", 'w') as file:
                    for row in ListSensorneigh:
                        s = "".join(map(str, row))
                        file.write(s + '\n')

            SaveFileSenss()
        def Destroyer():
            import GUIs as g
            if(len(ListofNumbers)==0):
                ms.showerror("ERORR","No this way list of your WSN is empty")
            else:
                main_window.destroy()
                g.InitGuis()
        def Clear():
            ListPOI.clear()
            ListofNumbers.clear()
            ListSensorneigh.clear()
            converted_listCalcSingleq.clear()
            ListofNumbersCalcSingleq.clear()
            ListofNumbersCalcSingleqState.clear()
            IdPOICOV.clear()
            STATES.clear()


        myButton = tk.Button(main_window, text="SHOW WSN", command=Init)
        myButton.pack()
        #SaveButton=tk.Button(main_window,text="cal sensor ID",command=SaveFileSens)
        #SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="find WSN graph", command=OpenMYSensorNeighbour)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="calc single q", command=CalcSingleq)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="calc all q", command=CalcALLq)
        SaveButton.pack(side="left")
        SaveButton = tk.Button(main_window, text="Clear", command=Clear)
        SaveButton.pack(side="left")

#########################################################################################################################

        #INSTANCE
        main_window.mainloop()
