#POPRAWA WSZYSTKICH PLIKOW TEKSTOWYCH, STATE przepisanie z poprzedniego STATE WYLOSOWANEFO
import GUIs as g
import csv
import gui as gs
from random import *
import re
import numpy as np
from functools import reduce
from tkinter import filedialog
from  tkinter import messagebox as ms
import tkinter as tk
#VALUE TO SAVE
q=0
f_alavie=0
minBatt=0
avBatt=0
maxBatt=0
#ListData = []  # Reading List Of Data #X #Y
#ListPOI = []  # List which contains POI #X #Y
Radius=''
radiusTxt='' #Files which contain name of FIle
STATE=[] # STATES
RULES=[] #RULES
K=[]
BATTERY_STATE=[] # List with lifetime battery
ALIVE_DEAD=[] #ALIVE OF SENSOR
FreqOn=[] #PLOT FREQ ON
FreqOff=[] #PLOT FREQ OFF
BatterY_STATE_SUM=[] #PLOT Battery
iters=[] #plotlib value Q
AmountWSN=0
ListofAll=[]
ListofNeighbour=[] #List which contains neighbour
ListSensorneighQ =[]
ListSensorneighQresult =[]
#ListFor every experiment:
ListQ=[]
ListF=[]
ListminBatt=[]
ListmaxBatt=[]
lisavBatt=[]
listfreqKD=[]
listfreqKC=[]
listfreqKDC=[]

def donothing():
    abc=0
'''
def OpenSensorWSN():
    #LOAD POI - LISTA POI CHANGE
    ListofAll.clear()
    ListData.clear()
    ListPOI.clear()
    global AmountWSN
    global Radius # assigment variable global
    with open("POI441.csv") as file:  # CHANGE TO PO 4412
        reader = csv.reader(file)
        for row in reader:
            ListPOI.append(row)
        ms.showinfo(title=None, message="Read Sensor Data To Experiment")
        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
                                               filetypes=(("Text Files", "*.txt"),))
        text_file = open(text_file, 'r')
        #text_file=open('WSN-5d-r35.txt','r')
        radiusTxt=text_file.name
        ListofAll.append("File: "+str(radiusTxt))
        radius=''
        #RADIUS VALUE FROM FILE
        for word in radiusTxt:
            if word.isdigit():
                radius+=str(word)
        Radius=radius[-2:]
        # DELETE FIRST PARAMETER
        #ADD XY TO LIST
        itera=-1
        for x in text_file:
            ListData.append(x)
            itera+=1
        AmountWSN=itera
        ListData.pop(0)
        #print(AmountWSN)
        #Print DATA
'''
av_q=[]
std_q=[]
av_alive=[]
std_f_alife=[]
av_minBatt=[]
std_minBatt=[]
av_Batt = []
std_Batt = []
av_maxBatt = []
std_maxBatt = []
av_freqKD = []
std_freqKD = []
av_freqKC = []
std_freqKC = []
av_freqKDC = []
std_freqKDcC = []
STATE=gs.STATES
#print(gs.STATES)
def Start():
    ListSensorneighQresult.append("#Number of Sensors " + str(gs.amountReadWSN))
    ListSensorneighQresult.append("#Sensor Range: " + str(gs.radius.get()))
    ListSensorneighQresult.append("#POI: " + str(len(gs.ListPOI)))
    ListSensorneighQresult.append("#Sensor for file: " + str(gs.textsVariable))  # radiusTxt) CHANGE
    ListSensorneighQresult.append("Battery Unit : " + str(g.labelBattery.get()))
    ListSensorneighQresult.append("Iterations: " + str(g.labelIterationNumb.get()))
    ListSensorneighQresult.append("Multiruns: " + str(g.labelMuttiruns.get()))
    ListSensorneighQresult.append("prob KD: " + str(g.labelkDvalue.get()))
    ListSensorneighQresult.append("prob KC: " + str(g.labelkCvalue.get()))
    ListSensorneighQresult.append("prob KDC: " + str(g.labelkDCvalue.get()))
    #print(ListPOI)
    #print(gs.radius.get())
    #print(gs.amountReadWSN)
    global  STATE
    global  RULES
    #print(STATE)
    av_q.clear()
    av_alive.clear()
    av_minBatt.clear()
    av_Batt.clear()
    av_maxBatt.clear()
    av_freqKD.clear()
    av_freqKC.clear()
    av_freqKDC.clear()
    #Iteration
    RULES=[]
    #NEIGHBOR FILE TXT
    K = []
    ListSensorneigh=[]
    BATTERY_STATE.clear() # ZAMIENIONE Z []
    #NEigh every singe Sensor
    Neighb=[]
    def OpenMYSensorNeighbour():  # find WSN grapph
        ListSensorneigh.clear()
        Neighb.clear()

        # LIST NEIGTBOUR
        ListSensorneigh.append("#parameters of run: ")
        ListSensorneigh.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneigh.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneigh.append("#POI: 36")
        ListSensorneigh.append("#Sensor for file: " )#+ radiusTxt) # CHANGEEE
        ListSensorneigh.append("#id num_of_neighb neigb-ID")
        id = 1

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
        for x in gs.ListofNumbers:
            id = 1
            helper=0
            for y in gs.ListofNumbers:
                ListofNeighbour.append(str(id) + str(
                    circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                           int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                           int(gs.radius.get()), int(gs.radius.get()))))
                xs = str(id) + str(
                    circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                           int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                           int(gs.radius.get()), int(gs.radius.get())))
                beng = '-'
                if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[0:2] ):
                    donothing()
                else:
                    if (len(xs) < 3):
                        ys += xs[0] + " "
                        helper = helper + 1
                    else:
                        ys += xs[0:2] + " "
                        helper = helper + 1
                id = id + 1
            ListSensorneigh.append(str(counter) + "    " + str(helper) + "     " + ys)
            Neighb.append(ys)
            ys = ""
            counter = counter + 1
        #print(Neighb)

        def SaveFileSenss():
            with open("sensor-neighbours .txt", 'w') as file:
                for row in ListSensorneigh:
                    s = "".join(map(str, row))
                    file.write(s + '\n')

        SaveFileSenss()
    #Call Neighbour
    OpenMYSensorNeighbour() #
    ListofAll.append("FIRST STATE :  " + str(STATE))
    #RULES LIST => Values [1-3]
    for x in range(int(gs.amountReadWSN)):
        helper=random()
        if(float(g.labelkDvalue.get())>helper):
            #print("KD")
            RULES.append(1)
        elif(float(g.labelkDvalue.get())+(float(g.labelkCvalue.get()))>helper):
            #print("KC")
            RULES.append(2)
        else:
            #print('KDC')
            RULES.append(3)
    #print(RULES)
    ListofAll.append("RULES 1-KD , 2 -KC ,3 KDC ->" + str(RULES) )
    # K -APPROACH [1..N]
    for x in range(int(gs.amountReadWSN)):
        if(RULES[x]==1):
            K.append(g.valuesRadiokDstate.get())
        elif (RULES[x] == 2):
            K.append(g.valuesRadiokCstate.get())
        else:
            K.append(g.valuesRadiokDCstate.get())
    #print(K)
    # Battery State [1..N]
    for x in range(int(gs.amountReadWSN)):
        BATTERY_STATE.append(int(gs.battery.get()))
    #print(BATTERY_STATE)
    ListofAll.append("BATTERY STATE [1..N]" + str(RULES))
    #Read neighb of onn LIST
    #BEFORE START ASSIGN SOME VARIABLE
    #List Sensor neigh result 1.txt
    xo= 1#info about run
    ListSensorneighQresult.append("#run 1 ")
    ListSensorneighQresult.append("# iter  q  f_alive minBatt avBatt maxBatt freqkD freqkC freqkDC")
    xo += 1
    def MainIter():
        converted_ListData = []
        NewState = []
        StateListNeigh = []
        SensorHelper = []  # HELPER LIST
        if (len(gs.ListPOI) > 300):
            POIVALUE = 441
        elif (len(gs.ListPOI) < 300 and len(gs.ListPOI) > 40):
            POIVALUE = 144
        else:
            POIVALUE = 36
        IdPOICOV=[]
        SensorHelperPoiID=[]
        ALLPOICOV=[]
        global STATE
        for i in range(int(g.labelIterationNumb.get())):
            iter = 0
            def ReadState():
                for x in Neighb:
                    c = 0
                    d = 0
                    i = 1
                    for y in STATE:
                        if (x.find(str(i) + ' ') == -1):
                            i += 1
                            continue
                        else:
                            if (y == 1):
                                c += 1
                            else:
                                d += 1
                            i += 1
                    StateListNeigh.append(str(c) + " " + str(d))
            ReadState()
            #print("STATE LIST NEIGH")
            #print(StateListNeigh)
            NewState.clear()
        #=====================================================================
            def CalcALLq(): # WRITE COVERAGE METHOD
                def circle(x1, y1, x2, y2, r1, r2):
                    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                    radSumSq = (r1 + r2) * (r1 + r2)
                    if (distSq == radSumSq):
                        return 1
                    elif (distSq > radSumSq):
                        return -1
                    else:
                        return 0
                #STATE #SENSORSTATES
                #ListData#->XY
                #ListPOI#->POI
                variableAm=0

                for x in gs.ListofNumbers:
                    converted_ListData.append(x.strip())
                    variableAm += 1
                #print("COnverted List Data")
                #print(converted_ListData)
                #ADD STATE TO THE LIST
                #LIST TO TXT FILE
                #ListSensorneighQ.append(str(i) + "  " + str(STATE))
                #ListSensorneighQ.append("#q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
                #FLATEN LIST
                flaten_list=reduce(lambda z, y :z + y,gs.ListPOI)
                ids=1
                #COUNT COVERAE EVERY SENSOR
                for x in converted_ListData:
                    helper = 0
                    for y in flaten_list:
                        if (y[0] == '0' or y[0:2] == '5;' or y[0:2] == '8;'):  # SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                            SensorHelper.append(str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0]), int(y[2:]), int(gs.radius.get()), 1)))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0]), int(y[2:]), int(gs.radius.get()), 1))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1  # VALUE WHEN SENSOR STATE IS 1
                        elif (y[0:3] == '100'):
                            SensorHelper.append(
                                str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()), int(y[0:3]), int(y[4:]),
                                           int(gs.radius.get()), 1)))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0:3]), int(y[4:]), int(gs.radius.get()), 1))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1
                        else:
                            SensorHelper.append(
                                str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]),
                                           int(gs.radius.get()), 1)))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0:2]), int(y[3:]),int(gs.radius.get()), 1))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1

                    coverage = POIVALUE - helper  # ZMINA Z 411
                    IdPOICOV.append(str(coverage))  # ID + AMOUNT OF
                    pom = 0
                    for x in SensorHelper:
                        ALLPOICOV.append(x)
                        SensorHelperPoiID.append(x + " - " + str(pom))
                        pom = pom + 1
                    # ALLPOICOV.extend(SensorHelper)
                    ids += 1
                    SensorHelper.clear()
                chunkser = [ALLPOICOV[x:x + POIVALUE] for x in range(0, len(ALLPOICOV), POIVALUE)]  #
                #chunkserPoi = [SensorHelperPoiID[x:x + POIVALUE] for x in range(0, len(SensorHelperPoiID), POIVALUE)]
                idstates = 0
                arubaCloud = []
                counterchuk = 0
                abc = ""
                for x in STATE:
                    if (x == 0):
                        donothing()
                    else:
                        trucrypt = chunkser[counterchuk]
                        for y in chunkser:
                            printerek = 0
                            amount = 0
                            for z in y:
                                if (trucrypt[printerek] == z):
                                    if (z == '0'):  # and trucrypt != y
                                        amount = amount + 1
                                        arubaCloud.append(str(printerek))  # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek = printerek + 1
                            abc += str(idstates) + "-" + str(amount) + "\n"  # AMOUNT + STATES ON
                    counterchuk = counterchuk + 1
                    idstates = idstates + 1
                finalStates = dict.fromkeys(arubaCloud)  # DELETE DUPLICATE
                # COVERAGE Q
                coverageQ = len(finalStates) / POIVALUE
                # CALC SENSOR ID TO TXT
                #helper Values
                #BATTERY ======================================
                helpnis=0 #Helper to battery ALIVE
                BatteryOFFcoun=0
                KDfreq = 0
                KCfreq =0
                KDCfreq =0
                for x in BATTERY_STATE:
                    if(BATTERY_STATE[helpnis]==0):
                        BatteryOFFcoun+=1
                        RULES[helpnis] = 4
                        helpnis+=1
                    else:
                        helpnis += 1
                    KDfreq = round(RULES.count(1) / len(RULES), 2)
                    KCfreq = round(RULES.count(2) / len(RULES), 2)
                    KDCfreq = round(RULES.count(3) / len(RULES), 2)
                freq_alive=float((len(BATTERY_STATE))-BatteryOFFcoun)/len(BATTERY_STATE)
                #MIN BATTERY
                BATTERY_STATE_SORT=BATTERY_STATE
                BATTERY_STATE_SORT.sort()
                minBatt=BATTERY_STATE_SORT[0]
                maxBatt=BATTERY_STATE_SORT[-1]
                avgBatt=sum(BATTERY_STATE_SORT)/len(BATTERY_STATE_SORT)

                # BATTERY ======================================
                sensOn=STATE.count(1)
                sensOff=STATE.count(0)
                amountSens=len(STATE)
                FreqOff.append(round(sensOff / amountSens, 2))
                FreqOn.append(round(sensOn / amountSens, 2))
                iters.append(str(round(coverageQ, 2)))
                ListSensorneighQresult.append("    " + str(int(i))+ "  "+
                    str(round(coverageQ, 2)) + "  "+str(round(freq_alive,2))+"      "+ str(minBatt) +"     " +str(round(avgBatt,2))+"       "
                                              +str(maxBatt)+"       " +str(KDfreq)+ "     "+str(KCfreq) + "      "+ str(KDCfreq))
                                               #str(round(sensOn/amountSens,2)) + "  " +str(round(sensOff/amountSens,2)))
                ListQ.append(round(coverageQ, 2))
                ListF.append(round(freq_alive,2))
                ListminBatt.append(minBatt)
                lisavBatt.append(round(avgBatt,2))
                ListmaxBatt.append(maxBatt)
                listfreqKD.append(KDfreq)
                listfreqKC.append(KCfreq)
                listfreqKDC.append(KDCfreq)
                # CA RESULT _ STD
                #av_q.append(round(float((1-coverageQ)/1),2))
                #std_q.append(round())
                av_q.append(round(coverageQ, 2))
                av_alive.append(round(freq_alive,2))
                av_minBatt.append(minBatt)
                av_Batt.append(round(avgBatt,2))
                av_maxBatt.append(maxBatt)
                av_freqKD.append(KDfreq)
                av_freqKC.append(KCfreq)
                av_freqKDC.append(KDCfreq)
                #"iter av_q std_q  av_falive std f_alive av minBatt std minBatt av avBatt std avBatt av maxBatt std maxBatt av freq_kD std freq_kD av freq_kC std freq_kC av freq_kDC std freq_kDC"
                avhelper = float((len((av_q)) - sum(av_q)) / (len(av_q)))
                freq_alive = float((len(BATTERY_STATE)) - BatteryOFFcoun) / len(BATTERY_STATE)
                #avq=round(float((1-coverageQ)/1),2)
                #av_std=np.std(coverageQ) #np.std(arr)
                #ListSensorneighQ.append("av_q std_q" +str(avq))
                def SaveFileSensss():
                    with open("CA_result.txt"
                              "", 'w') as file:
                        for row in ListSensorneighQresult:
                            s = "".join(map(str, row))
                            file.write(s + '\n')
                SaveFileSensss()
        #FIrst ITeration
            iterr = 0
            for x in RULES:
                if(x==1):# StateListNeigh[iter][2]<K[iter]
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):  # int(re.search(r'\d+', x[0:2]).group())
                        NewState.append(1)  # int(re.search(r'\d+', x[0:2]).group()
                        iter += 1
                    else:
                        NewState.append(0)
                        iter += 1
                elif (x == 2):
                    if (int(re.search(r'\d+', StateListNeigh[iter][0:2]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        NewState.append(1)
                        iter += 1
                    else:
                        NewState.append(0)
                        iter += 1
                else:
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) >= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        NewState.append(1)
                        iter += 1
                    else:
                        NewState.append(0)
                        iter += 1
                #Battery STATE
                if (1 == int(STATE[iterr])):
                    BATTERY_STATE[iterr] -= int(g.labelBattery.get())
                iterr+=1
            #=====================================================================================
            #QOVERAGE
            #print("STATE")
            #print(STATE)
            #======================================================================ALL COV Q ##################################
            CalcALLq()
            #BATTERY ALIVE
            #print("BATTERY STATE")
            #print(BATTERY_STATE)
            #ZAMIANA STATE PROBLEM
            STATE=NewState
            StateEnd = []
            BatterY_STATE_SUM.append(sum(BATTERY_STATE))
            #print("BATTERY STATE")
            #print(BATTERY_STATE)
            #CalcALLq()
            #CLEAR
            StateListNeigh.clear()
    MainIter()
def Mamut():
    for i in range(int(g.labelMuttiruns.get())):
        Start()

    def SaveFileSenss():
            with open("Ca_result_std.txt"
                      "", 'w') as file:
                for row in ListSensorneighQ:
                    s = "".join(map(str, row))
                    file.write(s + '\n')

    ListSensorneighQ.append("#Number of Sensors " + str(gs.amountReadWSN))
    ListSensorneighQ.append("#Sensor Range: " + str(gs.radius.get()))
    ListSensorneighQ.append("#POI: " + str(len(gs.ListPOI)))
    ListSensorneighQ.append("#Sensor for file: " + str(gs.textsVariable))  # radiusTxt) CHANGE
    ListSensorneighQ.append("Battery Unit : " + str(g.labelBattery.get()))
    ListSensorneighQ.append("Iterations: " + str(g.labelIterationNumb.get()))
    ListSensorneighQ.append("Multiruns: " + str(g.labelMuttiruns.get()))
    ListSensorneighQ.append("prob KD: " + str(g.labelkDvalue.get()))
    ListSensorneighQ.append("prob KC: " + str(g.labelkCvalue.get()))
    ListSensorneighQ.append("prob KDC: " + str(g.labelkDCvalue.get()))
    ListSensorneighQ.append(
            "iter, av_q, std_q, av_falive, std f_alive, av minBatt, std minBatt, av avBatt, std avBatt,  av maxBatt, std maxBatt, av freq_kD, std freq_kD, av freq_kC, std freq_kC, av freq_kDC, std freq_kDC")
        #HELPERS List
    #avhelper = float((len((av_alive)) - sum(av_alive)) / (len(av_alive)))
    #ListSensorneighQ.append(
    #    "       av_falive std f_alive " + str(round(avhelper, 2)) + " " + str(round(np.std(av_alive), 2)))
    #avhelper = float(sum(av_minBatt) / (len(BatterY_STATE_SUM)))
    for i in range(int(g.labelIterationNumb.get())):
        avqhelper = float(sum(ListQ[i::8])/ (len(ListQ[i::8])))# Z KAZDEJ ITERACJI JEST LICZONA SREDNIA -> Dac for dzielacego na liczbe multirunow
        avalife= float(sum(ListF[i::8]) / (len(ListF[i::8])))
        minhelper = float(sum(ListminBatt[i::8]) / (len(ListminBatt[i::8])))
        avbathelperr = float(sum(lisavBatt[i::8]) / (len(lisavBatt[i::8])))
        maxbathelperr = float(sum(ListmaxBatt[i::8]) / (len(ListmaxBatt[i::8])))
        listkdhelperr = float(sum(listfreqKD[i::8]) / (len(listfreqKD[i::8])))
        listkchelper=float(sum(listfreqKC[i::8]) / (len(listfreqKC[i::8])))
        listkdchelper=float(sum(listfreqKDC[i::8]) / (len(listfreqKDC[i::8])))
        ListSensorneighQ.append( str(i) + "     " +str(round(avqhelper,2 )) + "    " + str(round(np.std(ListQ[i::8]),2)) +
                                 "      "+ str(round(avalife,2  )) + "       "+ str(round(np.std(ListF[i::8]),2)) +
                                 "         "+ str(round(minhelper,2 )) + "           "+ str(round(np.std(ListminBatt[i::8]),2)) +
                                 "        "+ str(round(avbathelperr,2 )) + "        "+ str(round(np.std(lisavBatt[i::8]),2)) +
                                 "         "+ str(round(maxbathelperr,2 )) + "          "+ str(round(np.std(ListmaxBatt[i::8]),2)) +
                                 "       "+ str(round(listkdhelperr,2 )) + "         "+ str(round(np.std(listfreqKD[i::8]),2)) +
                                 "        "+ str(round(listkchelper,2 )) + "           "+ str(round(np.std(listfreqKC[i::8]),2)) +
                                 "        "+ str(round(listkdchelper,2 )) + "          "+ str(round(np.std(listfreqKDC[i::8]),2)))
    SaveFileSenss()

def DisplayBeutyful():
        # print(ListPOI)
        global STATE
        global RULES
        av_q.clear()
        av_alive.clear()
        av_minBatt.clear()
        av_Batt.clear()
        av_maxBatt.clear()
        av_freqKD.clear()
        av_freqKC.clear()
        av_freqKDC.clear()
        # Iteration
        t = 0
        RULES = []
        STATE = []
        # NEIGHBOR FILE TXT
        K = []
        ListSensorneigh = []
        BATTERY_STATE.clear()  # ZAMIENIONE Z []
        # NEigh every singe Sensor
        Neighb = []

        def OpenMYSensorNeighbour():  # find WSN grapph
            ListSensorneigh.clear()
            Neighb.clear()

            # LIST NEIGTBOUR
            ListSensorneigh.append("#parameters of run: ")
            ListSensorneigh.append("#Number of Sensors " + str(gs.amountReadWSN))
            ListSensorneigh.append("#Sensor Range: " + str(gs.radius.get()))
            ListSensorneigh.append("#POI: 36")
            ListSensorneigh.append("#Sensor for file: " )#radiusTxt) CHANGE
            ListSensorneigh.append("#id num_of_neighb neigb-ID")
            id = 1

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
            for x in gs.ListofNumbers:
                id = 1
                helper = 0
                for y in gs.ListofNumbers:
                    ListofNeighbour.append(str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get()))))
                    xs = str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get())))
                    beng = '-'
                    if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[0:2]):
                        donothing()
                    else:
                        if (len(xs) < 3):
                            ys += xs[0] + " "
                            helper = helper + 1
                        else:
                            ys += xs[0:2] + " "
                            helper = helper + 1
                    id = id + 1
                ListSensorneigh.append(str(counter) + "    " + str(helper) + "     " + ys)
                Neighb.append(ys)
                ys = ""
                counter = counter + 1

            # print(Neighb)

            def SaveFileSenss():
                with open("sensor-neighbours .txt", 'w') as file:
                    for row in ListSensorneigh:
                        s = "".join(map(str, row))
                        file.write(s + '\n')

            SaveFileSenss()

        # Call Neighbour
        OpenMYSensorNeighbour()
        # STATE LIST | RANDOM STATE FORM 0,1
        for x in range(int(gs.amountReadWSN)):
            if (len(g.labelSetSeed.get()) > 0):
                seed(g.labelSetSeed.get())
            STATE.append(randint(0, 1))
        print("FIRST STATE ")
        print(STATE)
        ListofAll.append("FIRST STATE :  " + str(STATE))
        # RULES LIST => Values [1-3]
        for x in range(int(gs.amountReadWSN)):
            helper = random()
            if (float(g.labelkDvalue.get()) > helper):
                # print("KD")
                RULES.append(1)
            elif (float(g.labelkDvalue.get()) + (float(g.labelkCvalue.get())) > helper):
                # print("KC")
                RULES.append(2)
            else:
                # print('KDC')
                RULES.append(3)
        print("RULES 1-KD,2KC,3KDC ->")
        print(RULES)
        ListofAll.append("RULES 1-KD , 2 -KC ,3 KDC ->" + str(RULES))
        # K -APPROACH [1..N]
        for x in range(int(gs.amountReadWSN)):
            if (RULES[x] == 1):
                K.append(g.valuesRadiokDstate.get())
            elif (RULES[x] == 2):
                K.append(g.valuesRadiokCstate.get())
            else:
                K.append(g.valuesRadiokDCstate.get())
        # print(K)
        # Battery State [1..N]
        for x in range(int(gs.amountReadWSN)):
            BATTERY_STATE.append(int(g.labelBattery.get()))
        # print(BATTERY_STATE)
        ListofAll.append("BATTERY STATE [1..N]" + str(BATTERY_STATE))
        print("BATTERY STATE [1..N]")
        print(BATTERY_STATE)
        # Read neighb of onn LIST
        # BEFORE START ASSIGN SOME VARIABLE
        # LIST SENSOR NEIGH result-2.txt
        ListSensorneighQ.append("#")
        ListSensorneighQ.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneighQ.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneighQ.append("#POI:" + str(len(gs.ListPOI)))
        ListSensorneighQ.append("#Sensor for file: " + str(gs.textsVariable))  # radiusTxt) CHANGE
        ListSensorneigh.append("Battery Unit : " + str(g.labelBattery.get()))
        ListSensorneighQ.append("Iterations: " + str(g.labelIterationNumb.get()))
        ListSensorneighQ.append("Multiruns"+ str(g.labelMuttiruns.get()))
        ListSensorneighQ.append("prob KD" + str(g.labelkDvalue.get()))
        ListSensorneighQ.append("prob KC" + str(g.labelkCvalue.get()))
        ListSensorneighQ.append("prob KDC" + str(g.labelkDCvalue.get()))
        ListSensorneighQ.append("# parameters of experiment")
        ListSensorneighQ.append("#")
        ListSensorneighQ.append("iter av_q std_q  av_falive std f_alive av minBatt std minBatt av avBatt std avBatt av maxBatt std maxBatt av freq_kD std freq_kD av freq_kC std freq_kC av freq_kDC std freq_kDC")
        # List Sensor neigh result 1.txt
        ListSensorneighQresult.append("#")
        ListSensorneighQresult.append("# parameters of experminet")
        ListSensorneighQresult.append('#')
        ListSensorneighQresult.append("# iter  q  f_alive minBatt, avBatt, maxBatt, freqkD freqkC freqkDC")

        def MainIter():
            converted_ListData = []
            NewState = []
            StateListNeigh = []
            SensorHelper = []  # HELPER LIST
            if(len(gs.ListPOI)>300):
                POIVALUE = 441
            elif(len(gs.ListPOI)<300 and len(gs.ListPOI)>40):
                POIVALUE=144
            else:
                POIVALUE=36

            IdPOICOV = []
            SensorHelperPoiID = []
            ALLPOICOV = []
            global STATE
            for i in range(int(g.labelIterationNumb.get())):
                iter = 0

                def ReadState():
                    for x in Neighb:
                        c = 0
                        d = 0
                        i = 1
                        for y in STATE:
                            if (x.find(str(i) + ' ') == -1):
                                i += 1
                                continue
                            else:
                                if (y == 1):
                                    c += 1
                                else:
                                    d += 1
                                i += 1
                        StateListNeigh.append(str(c) + " " + str(d))

                ReadState()
                # print("STATE LIST NEIGH")
                # print(StateListNeigh)
                NewState.clear()

                def CalcALLq():  # WRITE COVERAGE METHOD
                    def circle(x1, y1, x2, y2, r1, r2):
                        distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                        radSumSq = (r1 + r2) * (r1 + r2)
                        if (distSq == radSumSq):
                            return 1
                        elif (distSq > radSumSq):
                            return -1
                        else:
                            return 0

                    # STATE #SENSORSTATES
                    # ListData#->XY
                    # ListPOI#->POI
                    variableAm = 0

                    for x in gs.ListofNumbers:
                        converted_ListData.append(x.strip())
                        variableAm += 1
                    # print("COnverted List Data")
                    # print(converted_ListData)
                    # ADD STATE TO THE LIST
                    # LIST TO TXT FILE
                    # ListSensorneighQ.append(str(i) + "  " + str(STATE))
                    # ListSensorneighQ.append("#q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
                    # FLATEN LIST
                    flaten_list = reduce(lambda z, y: z + y, gs.ListPOI)
                    ids = 1
                    # COUNT COVERAE EVERY SENSOR
                    for x in converted_ListData:
                        helper = 0
                        for y in flaten_list:
                            if (y[0] == '0' or y[0:2] == '5;' or y[
                                                                 0:2] == '8;'):  # SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                                SensorHelper.append(str(
                                    circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()),
                                           int(y[0]), int(y[2:]), int(gs.radius.get()), 1)))
                                ys = str(
                                    circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()),
                                           int(y[0]), int(y[2:]), int(gs.radius.get()), 1))
                                if (ys[0] == '0'):
                                    donothing()
                                else:
                                    helper += 1  # VALUE WHEN SENSOR STATE IS 1
                            elif (y[0:3] == '100'):
                                SensorHelper.append(
                                    str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                               int(re.search(r'\d+', x[5:7]).group()), int(y[0:3]), int(y[4:]),
                                               int(gs.radius.get()), 1)))
                                ys = str(
                                    circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()),
                                           int(y[0:3]), int(y[4:]), int(gs.radius.get()), 1))
                                if (ys[0] == '0'):
                                    donothing()
                                else:
                                    helper += 1
                            else:
                                SensorHelper.append(
                                    str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                               int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]),
                                               int(gs.radius.get()), 1)))
                                ys = str(
                                    circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()),
                                           int(y[0:2]), int(y[3:]), int(gs.radius.get()), 1))
                                if (ys[0] == '0'):
                                    donothing()
                                else:
                                    helper += 1

                        coverage = POIVALUE - helper  # ZMINA Z 411
                        IdPOICOV.append(str(coverage))  # ID + AMOUNT OF
                        pom = 0
                        for x in SensorHelper:
                            ALLPOICOV.append(x)
                            SensorHelperPoiID.append(x + " - " + str(pom))
                            pom = pom + 1
                        # ALLPOICOV.extend(SensorHelper)
                        ids += 1
                        SensorHelper.clear()
                    chunkser = [ALLPOICOV[x:x + POIVALUE] for x in range(0, len(ALLPOICOV), POIVALUE)]  #
                    # chunkserPoi = [SensorHelperPoiID[x:x + POIVALUE] for x in range(0, len(SensorHelperPoiID), POIVALUE)]
                    idstates = 0
                    arubaCloud = []
                    counterchuk = 0
                    abc = ""
                    for x in STATE:
                        if (x == 0):
                            donothing()
                        else:
                            trucrypt = chunkser[counterchuk]
                            for y in chunkser:
                                printerek = 0
                                amount = 0
                                for z in y:
                                    if (trucrypt[printerek] == z):
                                        if (z == '0'):  # and trucrypt != y
                                            amount = amount + 1
                                            arubaCloud.append(str(printerek))  # USUNIECIE PRINTERKA
                                    else:
                                        donothing()
                                    printerek = printerek + 1
                                abc += str(idstates) + "-" + str(amount) + "\n"  # AMOUNT + STATES ON
                        counterchuk = counterchuk + 1
                        idstates = idstates + 1
                    finalStates = dict.fromkeys(arubaCloud)  # DELETE DUPLICATE
                    # COVERAGE Q
                    coverageQ = len(finalStates) / POIVALUE
                    # CALC SENSOR ID TO TXT
                    # helper Values
                    # BATTERY ======================================
                    helpnis = 0  # Helper to battery ALIVE
                    BatteryOFFcoun = 0
                    KDfreq = 0
                    KCfreq = 0
                    KDCfreq = 0
                    for x in BATTERY_STATE:
                        if (BATTERY_STATE[helpnis] == 0):
                            BatteryOFFcoun += 1
                            RULES[helpnis] = 4
                            helpnis += 1
                        else:
                            helpnis += 1
                        KDfreq = round(RULES.count(1) / len(RULES), 2)
                        KCfreq = round(RULES.count(2) / len(RULES), 2)
                        KDCfreq = round(RULES.count(3) / len(RULES), 2)
                    freq_alive = float((len(BATTERY_STATE)) - BatteryOFFcoun) / len(BATTERY_STATE)
                    # MIN BATTERY
                    BATTERY_STATE_SORT = BATTERY_STATE
                    BATTERY_STATE_SORT.sort()
                    minBatt = BATTERY_STATE_SORT[0]
                    maxBatt = BATTERY_STATE_SORT[-1]
                    avgBatt = sum(BATTERY_STATE_SORT) / len(BATTERY_STATE_SORT)

                    # BATTERY ======================================
                    sensOn = STATE.count(1)
                    sensOff = STATE.count(0)
                    amountSens = len(STATE)
                    FreqOff.append(round(sensOff / amountSens, 2))
                    FreqOn.append(round(sensOn / amountSens, 2))
                    iters.append(str(round(coverageQ, 2)))
                    ListSensorneighQresult.append("    " + str(int(i)) + "  " +
                                                  str(round(coverageQ, 2)) + "  " + str(
                        round(freq_alive, 2)) + "      " + str(minBatt) + "     " + str(round(avgBatt, 2)) + "       "
                                                  + str(maxBatt) + "       " + str(KDfreq) + "     " + str(
                        KCfreq) + "      " + str(KDCfreq))
                    # str(round(sensOn/amountSens,2)) + "  " +str(round(sensOff/amountSens,2)))
                    # CA RESULT _ STD
                    # av_q.append(round(float((1-coverageQ)/1),2))
                    # std_q.append(round())
                    av_q.append(round(coverageQ, 2))
                    av_alive.append(round(freq_alive, 2))
                    av_minBatt.append(minBatt)
                    av_Batt.append(round(avgBatt, 2))
                    av_maxBatt.append(maxBatt)
                    av_freqKD.append(KDfreq)
                    av_freqKC.append(KCfreq)
                    av_freqKDC.append(KDCfreq)

                    def SaveFileSensss():
                        with open("CA_result.txt"
                                  "", 'w') as file:
                            for row in ListSensorneighQresult:
                                s = "".join(map(str, row))
                                file.write(s + '\n')

                    SaveFileSensss()
                print("NEIGHBOURS")
                print(StateListNeigh)
                # FIrst ITeration
                iterr = 0
                for x in RULES:
                    if (x == 1):  # StateListNeigh[iter][2]<K[iter]
                        if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) <= int(K[iter]) and BATTERY_STATE[
                            iterr] > 0):  # int(re.search(r'\d+', x[0:2]).group())
                            NewState.append(1)  # int(re.search(r'\d+', x[0:2]).group()
                            iter += 1
                        else:
                            NewState.append(0)
                            iter += 1
                    elif (x == 2):
                        if (int(re.search(r'\d+', StateListNeigh[iter][0:2]).group()) <= int(K[iter]) and BATTERY_STATE[
                            iterr] > 0):
                            NewState.append(1)
                            iter += 1
                        else:
                            NewState.append(0)
                            iter += 1
                    else:
                        if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) >= int(K[iter]) and BATTERY_STATE[
                            iterr] > 0):
                            NewState.append(1)
                            iter += 1
                        else:
                            NewState.append(0)
                            iter += 1
                    # Battery STATE
                    if (1 == int(STATE[iterr])):
                        BATTERY_STATE[iterr] -= 1
                    iterr += 1
                # =====================================================================================
                # QOVERAGE
                # print("STATE")
                # print(STATE)
                # ======================================================================ALL COV Q ##################################
                CalcALLq()
                # BATTERY ALIVE
                # print("BATTERY STATE")
                # print(BATTERY_STATE)
                # ZAMIANA STATE PROBLEM
                print("NEXT STATE")
                print(NewState)
                STATE = NewState
                StateEnd = []
                BatterY_STATE_SUM.append(sum(BATTERY_STATE))
                print("BATTERY STATE")
                print(BATTERY_STATE)
                # for x in range(len(STATE)):
                #    StateEnd.append(0)

                # if (STATE == StateEnd):
                #     break
                # print("BATTERY STATE")
                # print(BATTERY_STATE)
                # CalcALLq()
                # CLEAR
                StateListNeigh.clear()

        MainIter()
