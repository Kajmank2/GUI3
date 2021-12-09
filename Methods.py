#POPRAWA WSZYSTKICH PLIKOW TEKSTOWYCH, STATE przepisanie z poprzedniego STATE WYLOSOWANEFO
import os
import sys
import GUIs as g
import gui as gs
from random import *
import re
import numpy as np
from functools import reduce
from  tkinter import messagebox as ms

#VALUE TO SAVE
q=0
f_alavie=0
minBatt=0
avBatt=0
sensorMethod=""
maxBatt=0
#ListData = []  # Reading List Of Data #X #Y
#ListPOI = []  # List which contains POI #X #Y
Radius=''
radiusTxt='' #Files which contain name of FIle
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
ListofNeighbourse=[]
ListSensorneighQ =[]
ListSensorneighQresult =[]
ListDebug=[]
#ListFor every experiment:
ListQ=[]
ListF=[]
ListminBatt=[]
ListmaxBatt=[]
lisavBatt=[]
listfreqKD=[]
listfreqKC=[]
listfreqKDC=[]
#tempListofNumbers=gs.ListofNumbers # ZMIANA WYCISZENIE ============================================
def donothing():
    abc=0
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
TempDebugList=[]
std_freqKC = []
av_freqKDC = []
tempListofNumbers =gs.ListofNumbers.copy()
std_freqKDcC = []
STATE=[]
RULES=[]
RULESSTABLE=[]
def Start():
    global STATE
    if(len(STATE)== 0):
        STATE=gs.STATES.copy()
    else:
        STATE.clear()
        for x in gs.ListofNumbers:
            rand = randint(0,1)
            STATE.append(rand)
    def Strategiesinput(): # METHOD
        if(g.staticStrategies.get()!=""):
            strategieslist = list(g.staticStrategies.get().split(","))
            for x in strategieslist:
                try:
                    if(x=="KD" or x=="kd"):
                        RULESSTABLE.append(1)
                    elif(x=="KC" or x =="kc"):
                        RULESSTABLE.append(2)
                    elif (x == "KDC" or x == "kdc"):
                        RULESSTABLE.append(3)
                    else:
                        RULESSTABLE.clear()
                        ms.showinfo(title="Error", message="you entred bad value: Program choose random strategies")
                        for x in range(int(gs.amountReadWSN)):
                            helper = random()
                            if (float(g.labelkDvalue.get()) > helper):
                                RULESSTABLE.append(1)
                            elif (float(g.labelkDvalue.get()) + (float(g.labelkCvalue.get())) > helper):
                                RULESSTABLE.append(2)
                            else:
                                RULESSTABLE.append(3)
                except:
                    ms.showinfo(title="Error", message="Something was wrong ...")
                    ms.ERROR("ERROR", "Please correct entry ")
        else:
            for x in range(int(gs.amountReadWSN)):
                helper = random()
                if (float(g.labelkDvalue.get()) > helper):
                    RULESSTABLE.append(1)
                elif (float(g.labelkDvalue.get()) + (float(g.labelkCvalue.get())) > helper):
                    RULESSTABLE.append(2)
                else:
                    RULESSTABLE.append(3)
    if(len(RULESSTABLE)>0):
        donothing()
    else:
        Strategiesinput()
    RULES=RULESSTABLE.copy()
    # ZMIANA STATE# problem z gs list of numbers
    print(gs.ListofNumbers)
    print(STATE)
    print(RULES)
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
    #NEIGHBOR FILE TXT
    K = []
    ListSensorneigh=[]
    BATTERY_STATE.clear() # ZAMIENIONE Z []
    #NEigh every singe Sensor
    Neighb=[]
    #Neighb.clear()
    def FindWSNGRAPH():  # find WSN grapph #GO GO GO
        # tempListofNumbers.clear()
        def circle(x1, y1, x2, y2, r1, r2):
            distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            radSumSq = (r1 + r2) * (r1 + r2)
            if (distSq == radSumSq):
                return 1
            elif (distSq > radSumSq):
                return -1
            else:
                return 0

        ys = " "  # zmiana ys na " " testowanie
        counter = 1
        TempDebugList.clear()
        for x in gs.ListofNumbers:
            id = 1
            helper = 0
            for y in gs.ListofNumbers:
                if (y[2:4] == ".3" or x[2:4] == ".3" or x[3:5] == ".3"):  # zmiana or z x
                    ListofNeighbourse.append(str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               0, 0)))
                    xs = str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               0, 0))
                    beng = '-'
                else:
                    ListofNeighbourse.append(str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get()))))
                    xs = str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get())))
                    beng = '-'
                if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[
                                                                             0:2]):  # or str(counter)==xs[0:2]): zmiana
                    donothing()
                else:
                    if (len(xs) < 3):  # 100 6-1
                        ys += xs[0] + " "
                        helper = helper + 1
                    else:
                        ys += xs[0:2] + " "
                        helper = helper + 1
                id = id + 1
            TempDebugList.append(str(helper))
            Neighb.append(ys)
            ys = " "
            ListofNeighbourse.clear()
            counter = counter + 1
    FindWSNGRAPH()

    '''
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
            with open("RESULT/sensor-neighbours .txt", 'w') as file:
                for row in ListSensorneigh:
                    s = "".join(map(str, row))
                    file.write(s + '\n')

        SaveFileSenss()
    #Call Neighbour
    OpenMYSensorNeighbour() #
    '''
    ListofAll.append("FIRST STATE :  " + str(STATE))
    #RULES LIST => Values [1-3]
    #print(RULES)
    ListofAll.append("RULES 1-KD , 2 -KC ,3 KDC ->" + str(RULES) )
    # K -APPROACH [1..N]
    for x in range(int(gs.amountReadWSN)):
        try:
            if(RULES[x]==1):
                K.append(g.valuesRadiokDstate.get())
            elif (RULES[x] == 2):
                K.append(g.valuesRadiokCstate.get())
            else:
                K.append(g.valuesRadiokDCstate.get())
        except:
            ms.showinfo(title="Error", message="Something was wrong ...")
            ms.ERROR("ERROR", "Please correct entry ")
    #print(K)
    # Battery State [1..N]
    for x in range(int(gs.amountReadWSN)):
        BATTERY_STATE.append(int(gs.battery.get()))
    #print(BATTERY_STATE)
    iterr=0
    for x in RULES:
        if (1 == int(STATE[iterr])):
            BATTERY_STATE[iterr] -= int(g.labelBattery.get())
            if (BATTERY_STATE[iterr] < int(g.labelBattery.get())):
                BATTERY_STATE[iterr] = 0
        iterr += 1
    ListofAll.append("BATTERY STATE [1..N]" + str(RULES))
    #Read neighb of onn LIST
    #BEFORE START ASSIGN SOME VARIABLE
    #List Sensor neigh result 1.txt
    #info about run
    if (len(ListSensorneighQresult)==0):
        ListSensorneighQresult.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneighQresult.append("METHOD" + gs.sensorMethod)
        ListSensorneighQresult.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneighQresult.append("#POI: " + str(len(gs.ListPOI)))
        ListSensorneighQresult.append("#Sensor for file: " + gs.filename)  # radiusTxt) CHANGE
        ListSensorneighQresult.append("Battery Unit : " + str(g.labelBattery.get()))
        ListSensorneighQresult.append("Iterations: " + str(g.labelIterationNumb.get()))
        ListSensorneighQresult.append("Multiruns: " + str(g.labelMuttiruns.get()))
        ListSensorneighQresult.append("prob KD: " + str(g.labelkDvalue.get()))
        ListSensorneighQresult.append("prob KC: " + str(g.labelkCvalue.get()))
        ListSensorneighQresult.append("prob KDC: " + str(g.labelkDCvalue.get()))
        stringRules = ""  # String with help with debug txt
        for x in RULES:
            if (x == 1):
                stringRules += str(g.valuesRadiokDstate.get()) + "D "
            elif (x == 2):
                stringRules += str(g.valuesRadiokCstate.get()) + "C "
            elif (x == 3):
                stringRules += str(g.valuesRadiokDCstate.get()) + "DC "
        ListSensorneighQresult.append("Strategies: " + stringRules)
        ListSensorneighQresult.append("#run ")
        ListSensorneighQresult.append("# iter  q  f_alive minBatt avBatt maxBatt freqkD freqkC freqkDC")
    else:
        ListSensorneighQresult.append("#run ")
        ListSensorneighQresult.append("# iter  q  f_alive minBatt avBatt maxBatt freqkD freqkC freqkDC")
    def MainIter():
        converted_ListData = []
        #NewState = []
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
            #NewState.clear()
            #STATE.clear()
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
                print(STATE)
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
                FEJKERBATTERY=BATTERY_STATE
                BATTERY_STATE_SORT=FEJKERBATTERY
                #BATTERY_STATE_SORT.sort() # UNCOMENT FOR AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                minBatt=BATTERY_STATE_SORT[0]
                maxBatt=max(BATTERY_STATE_SORT)
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
                #print("LISTQ",ListQ)
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
                    with open("RESULT/CA_result.txt"
                              "", 'w') as file:
                        for row in ListSensorneighQresult:
                            s = "".join(map(str, row))
                            file.write(s + '\n')
                SaveFileSensss()
        #FIrst ITeration
            CalcALLq()
            STATE.clear()
            iterr = 0
            for x in RULES:
                if (x == 1):  # StateListNeigh[iter][2]<K[iter]
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):  # int(re.search(r'\d+', x[0:2]).group())
                        STATE.append(1)  # int(re.search(r'\d+', x[0:2]).group()
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==" "): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                elif (x == 2):
                    if (int(re.search(r'\d+', StateListNeigh[iter][0:2]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        STATE.append(1)
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==" "): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                else:
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) > int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        STATE.append(1)
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==' '): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                #Battery STATE
                if (1 == int(STATE[iterr])):
                    BATTERY_STATE[iterr] -= int(g.labelBattery.get())
                    if(BATTERY_STATE[iterr]<int(g.labelBattery.get())):
                        BATTERY_STATE[iterr]=0
                iterr+=1
                '''
            print("STATE")
            print(STATE)
            print("STATE LIST NEIG")
            print(StateListNeigh)
            print("Neigh")
            print(Neighb)
            '''
            BatterY_STATE_SUM.append(sum(BATTERY_STATE))
            increse = 0
            for x in BATTERY_STATE:
                if (x <= 0):
                    tempListofNumbers[increse] = "3" + str(increse) + ".3 33.3"
                increse += 1

            def FindWSNGRAPH():  # find WSN grapph #GO GO GO
                # tempListofNumbers.clear()
                def circle(x1, y1, x2, y2, r1, r2):
                    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                    radSumSq = (r1 + r2) * (r1 + r2)
                    if (distSq == radSumSq):
                        return 1
                    elif (distSq > radSumSq):
                        return -1
                    else:
                        return 0

                ys = " "  # zmiana ys na " " testowanie
                counter = 1
                TempDebugList.clear()
                for x in tempListofNumbers:
                    id = 1
                    helper = 0
                    for y in tempListofNumbers:
                        if (y[2:4] == ".3" or x[2:4] == ".3" or x[3:5] == ".3"):  # zmiana or z x
                            ListofNeighbourse.append(str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       0, 0)))
                            xs = str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       0, 0))
                            beng = '-'
                        else:
                            ListofNeighbourse.append(str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       int(gs.radius.get()), int(gs.radius.get()))))
                            xs = str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       int(gs.radius.get()), int(gs.radius.get())))
                            beng = '-'
                        if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[0:2]):  # or str(counter)==xs[0:2]): zmiana
                            donothing()
                        else:
                            if (len(xs) < 3):  # 100 6-1
                                ys += xs[0] + " "
                                helper = helper + 1
                            else:
                                ys += xs[0:2] + " "
                                helper = helper + 1
                        id = id + 1
                    TempDebugList.append(str(helper))
                    Neighb.append(ys)
                    ys = " "
                    ListofNeighbourse.clear()
                    counter = counter + 1
            Neighb.clear()  # CHANGE
            FindWSNGRAPH()
            StateListNeigh.clear()
    MainIter()  # ZMIANA

def Mamut():
    for i in range(int(g.labelMuttiruns.get())):
        Start()
    if(int(g.labelMuttiruns.get())>1):
        def SaveFileSenss():
            with open("RESULT/Ca_result_std.txt"
                      "", 'w') as file:
                for row in ListSensorneighQ:
                    s = "".join(map(str, row))
                    file.write(s + '\n')
    else:
        def Exit():
            python = sys.executable
            os.execl(python, python, *sys.argv)

        Exit()

    ListSensorneighQ.append("#Number of Sensors " + str(gs.amountReadWSN))
    ListSensorneighQ.append("#Sensor Range: " + str(gs.radius.get()))
    ListSensorneighQ.append("#POI: " + str(len(gs.ListPOI)))
    ListSensorneighQ.append("#Sensor for file: " + str(gs.filename))  # radiusTxt) CHANGE
    ListSensorneighQ.append("Battery Unit : " + str(g.labelBattery.get()))
    ListSensorneighQ.append("Iterations: " + str(g.labelIterationNumb.get()))
    ListSensorneighQ.append("Multiruns: " + str(g.labelMuttiruns.get()))
    ListSensorneighQ.append("prob KD: " + str(g.labelkDvalue.get()))
    ListSensorneighQ.append("prob KC: " + str(g.labelkCvalue.get()))
    ListSensorneighQ.append("prob KDC: " + str(g.labelkDCvalue.get()))
    stringRules = ""  # String with help with debug txt
    for x in RULES:
        if (x == 1):
            stringRules += str(g.valuesRadiokDstate.get()) + "D "
        elif (x == 2):
            stringRules += str(g.valuesRadiokCstate.get()) + "C "
        elif (x == 3):
            stringRules += str(g.valuesRadiokDCstate.get()) + "DC "
    #ListSensorneighQresult.append("Strategies: " + stringRules)
    ListSensorneighQ.append(
            "iter, av_q, std_q, av_falive, std f_alive, av minBatt, std minBatt, av avBatt, std avBatt,  av maxBatt, std maxBatt, av freq_kD, std freq_kD, av freq_kC, std freq_kC, av freq_kDC, std freq_kDC")
    #HELPER VALUE FOR ITERATION
    ax=int(g.labelIterationNumb.get())
    for i in range(int(g.labelIterationNumb.get())):
        avqhelper = float(sum(ListQ[i::ax])/ (len(ListQ[i::ax])))
        #print(str(avqhelper) + " " + str(ListQ[i::8]))# Z KAZDEJ ITERACJI JEST LICZONA SREDNIA -> Dac for dzielacego na liczbe multirunow
        avalife= float(sum(ListF[i::ax]) / (len(ListF[i::ax])))
        minhelper = float(sum(ListminBatt[i::ax]) / (len(ListminBatt[i::ax])))
        avbathelperr = float(sum(lisavBatt[i::ax]) / (len(lisavBatt[i::ax])))
        maxbathelperr = float(sum(ListmaxBatt[i::ax]) / (len(ListmaxBatt[i::ax])))
        listkdhelperr = float(sum(listfreqKD[i::ax]) / (len(listfreqKD[i::ax])))
        listkchelper=float(sum(listfreqKC[i::ax]) / (len(listfreqKC[i::ax])))
        listkdchelper=float(sum(listfreqKDC[i::ax]) / (len(listfreqKDC[i::ax])))
        ListSensorneighQ.append(str(i) + "     " +str(round(avqhelper,2 )) + "    " + str(round(np.std(ListQ[i::ax]),2)) +
                                 "      "+ str(round(avalife,2  )) + "       "+ str(round(np.std(ListF[i::ax]),2)) +
                                 "         "+ str(round(minhelper,2 )) + "           "+ str(round(np.std(ListminBatt[i::ax]),2)) +
                                 "        "+ str(round(avbathelperr,2 )) + "        "+ str(round(np.std(lisavBatt[i::ax]),2)) +
                                 "         "+ str(round(maxbathelperr,2 )) + "          "+ str(round(np.std(ListmaxBatt[i::ax]),2)) +
                                 "       "+ str(round(listkdhelperr,2 )) + "         "+ str(round(np.std(listfreqKD[i::ax]),2)) +
                                 "        "+ str(round(listkchelper,2 )) + "           "+ str(round(np.std(listfreqKC[i::ax]),2)) +
                                 "        "+ str(round(listkdchelper,2 )) + "          "+ str(round(np.std(listfreqKDC[i::ax]),2)))
    SaveFileSenss()

    def Exit():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    Exit()
def DisplayBeutyful():
    global STATE
    STATE=gs.STATES
    global RULES
    tempListofNumbers = gs.ListofNumbers
    stringNeighs=""
    # print(STATE)
    av_q.clear()
    av_alive.clear()
    av_minBatt.clear()
    av_Batt.clear()
    av_maxBatt.clear()
    av_freqKD.clear()
    av_freqKC.clear()
    av_freqKDC.clear()
    # Iteration
    RULES = []
    # NEIGHBOR FILE TXT
    K = []
    ListSensorneigh = []
    BATTERY_STATE.clear()  # ZAMIENIONE Z []
    # NEigh every singe Sensor
    Neighb = []

    def FindWSNGRAPH():  # find WSN grapph #GO GO GO
        # tempListofNumbers.clear()
        def circle(x1, y1, x2, y2, r1, r2):
            distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            radSumSq = (r1 + r2) * (r1 + r2)
            if (distSq == radSumSq):
                return 1
            elif (distSq > radSumSq):
                return -1
            else:
                return 0

        ys = " "  # zmiana ys na " " testowanie
        counter = 1
        TempDebugList.clear()
        for x in tempListofNumbers:
            id = 1
            helper = 0
            for y in tempListofNumbers:
                if (y[2:4] == ".3" or x[2:4] == ".3" or x[3:5] == ".3"):  # zmiana or z x
                    ListofNeighbourse.append(str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               0, 0)))
                    xs = str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               0, 0))
                    beng = '-'
                else:
                    ListofNeighbourse.append(str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get()))))
                    xs = str(id) + str(
                        circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                               int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                               int(gs.radius.get()), int(gs.radius.get())))
                    beng = '-'
                if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[0:2]):  # or str(counter)==xs[0:2]): zmiana
                    donothing()
                else:
                    if (len(xs) < 3):  # 100 6-1
                        ys += xs[0] + " "
                        helper = helper + 1
                    else:
                        ys += xs[0:2] + " "
                        helper = helper + 1
                id = id + 1
            TempDebugList.append(str(helper))
            Neighb.append(ys)
            ys = " "
            ListofNeighbourse.clear()
            counter = counter + 1
    FindWSNGRAPH()
    '''
    def OpenMYSensorNeighbour():  # find WSN grapph
        ListSensorneigh.clear()
        Neighb.clear()
        # LIST NEIGTBOUR
        ListSensorneigh.append("#parameters of run: ")
        ListSensorneigh.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneigh.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneigh.append("#POI: 36")
        ListSensorneigh.append("#Sensor for file: ")  # + radiusTxt) # CHANGEEE
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
    OpenMYSensorNeighbour()  #
    '''
    ListofAll.append("FIRST STATE :  " + str(STATE))
    # RULES LIST => Values [1-3]
    if (g.staticStrategies.get() != ""):
        strategieslist = list(g.staticStrategies.get().split(","))
        for x in strategieslist:
            try:
                if (x == "KD" or x == "kd"):
                    RULES.append(1)
                elif (x == "KC" or x == "kc"):
                    RULES.append(2)
                elif (x == "KDC" or x == "kdc"):
                    RULES.append(3)
            except:
                ms.ERROR("ERROR", "Please correct entry ")
    else:
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
    # print(RULES)
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
        BATTERY_STATE.append(int(gs.battery.get()))
    iterr = 0
    for x in RULES:
        if (1 == int(STATE[iterr])):
            BATTERY_STATE[iterr] -= int(g.labelBattery.get())
            if (BATTERY_STATE[iterr] < int(g.labelBattery.get())):
                BATTERY_STATE[iterr] = 0
        iterr += 1
    # print(BATTERY_STATE)
    ListofAll.append("BATTERY STATE [1..N]" + str(RULES))
    # Read neighb of onn LIST
    # BEFORE START ASSIGN SOME VARIABLE
    # List Sensor neigh result 1.txt
    # info about run
    if (len(ListSensorneighQresult) == 0):
        ListSensorneighQresult.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneighQresult.append("METHOD"+ gs.sensorMethod)
        ListSensorneighQresult.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneighQresult.append("#POI: " + str(len(gs.ListPOI)))
        ListSensorneighQresult.append("#Sensor for file: " + str(gs.filename))  # radiusTxt) CHANGE
        ListSensorneighQresult.append("Battery Unit : " + str(g.labelBattery.get()))
        ListSensorneighQresult.append("Iterations: " + str(g.labelIterationNumb.get()))
        ListSensorneighQresult.append("Multiruns: " + str(g.labelMuttiruns.get()))
        ListSensorneighQresult.append("prob KD: " + str(g.labelkDvalue.get()))
        ListSensorneighQresult.append("prob KC: " + str(g.labelkCvalue.get()))
        ListSensorneighQresult.append("prob KDC: " + str(g.labelkDCvalue.get()))
        stringRules = ""
        for x in RULES:
            if (x == 1):
                stringRules += str(g.valuesRadiokDstate.get()) + "D "
            elif (x == 2):
                stringRules += str(g.valuesRadiokCstate.get()) + "C "
            elif (x == 3):
                stringRules += str(g.valuesRadiokDCstate.get()) + "DC "
        ListSensorneighQresult.append("Strategies: " + stringRules)
        ListSensorneighQresult.append("#run ")
        ListSensorneighQresult.append("# iter  q  f_alive minBatt avBatt maxBatt freqkD freqkC freqkDC")
    else:
        ListSensorneighQresult.append("#run ")
        ListSensorneighQresult.append("# iter  q  f_alive minBatt avBatt maxBatt freqkD freqkC freqkDC")
        #DEBUG FILEEEE
    debugstringstate=""
    debugstringrules=""
    itera=0
    for x in gs.ListofNumbers:
        itera+=1
        debugstringstate=debugstringstate+'s'+str(itera)+ " "
        debugstringrules = debugstringrules + 'str' + str(itera) + " "

    if (len(ListDebug) == 0):
        ListDebug.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListDebug.append("#Sensor Range: " + str(gs.radius.get()))
        ListDebug.append("#POI: " + str(len(gs.ListPOI)))
        ListDebug.append("#Sensor for file: " + str(gs.filename))  # radiusTxt) CHANGE
        ListDebug.append("Battery Unit : " + str(g.labelBattery.get()))
        ListDebug.append("Iterations: " + str(g.labelIterationNumb.get()))
        ListDebug.append("Multiruns: " + str(g.labelMuttiruns.get()))
        ListDebug.append("prob KD: " + str(g.labelkDvalue.get()))
        ListDebug.append("prob KC: " + str(g.labelkCvalue.get()))
        ListDebug.append("prob KDC: " + str(g.labelkDCvalue.get()))
        stringRules = ""
        for x in RULES:
            if (x == 1):
                stringRules += str(g.valuesRadiokDstate.get()) + "D "
            elif (x == 2):
                stringRules += str(g.valuesRadiokCstate.get()) + "C "
            elif (x == 3):
                stringRules += str(g.valuesRadiokDCstate.get()) + "DC "
            else:
                stringRules += "OFF"
        #ListSensorneighQresult.append("Strategies: " + stringRules)
        ListDebug.append("#run ")

        ListDebug.append("#iter  "+ debugstringstate+ "  "+debugstringrules + "           "+ debugstringstate)
    else:
        ListDebug.append("#run ")
        ListDebug.append("#iter  "+ debugstringstate+ "  "+debugstringrules + "           "+ debugstringstate)


        ############################MAIN FUNCTION #######################
    def MainIter():
        converted_ListData = []
        #NewState = []
        StateListNeigh = []
        SensorHelper = []  # HELPER LIST
        if (len(gs.ListPOI) > 300):
            POIVALUE = 441
        elif (len(gs.ListPOI) < 300 and len(gs.ListPOI) > 40):
            POIVALUE = 144
        else:
            POIVALUE = 36
        IdPOICOV = []
        SensorHelperPoiID = []
        ALLPOICOV = []
        global STATE
        #global STATEDBUG
        #STATEDBUG=STATE
        #OpenMYSensorNeighbour()
        for i in range(int(g.labelIterationNumb.get())):
            iter = 0
            #print("STATE FROM START")
            #print(STATE)
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
                # FLATEN LIST
                flaten_list = reduce(lambda z, y: z + y, gs.ListPOI)
                ids = 1
                # COUNT COVERAE EVERY SENSOR
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
                FEJKERBATTERY = BATTERY_STATE
                BATTERY_STATE_SORT = FEJKERBATTERY
                #BATTERY_STATE_SORT.sort()
                minBatt = BATTERY_STATE_SORT[0]
                maxBatt = max(BATTERY_STATE_SORT)
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
                ListQ.append(round(coverageQ, 2))
                ListF.append(round(freq_alive, 2))
                ListminBatt.append(minBatt)
                lisavBatt.append(round(avgBatt, 2))
                ListmaxBatt.append(maxBatt)
                listfreqKD.append(KDfreq)
                listfreqKC.append(KCfreq)
                listfreqKDC.append(KDCfreq)
                av_q.append(round(coverageQ, 2))
                av_alive.append(round(freq_alive, 2))
                av_minBatt.append(minBatt)
                av_Batt.append(round(avgBatt, 2))
                av_maxBatt.append(maxBatt)
                av_freqKD.append(KDfreq)
                av_freqKC.append(KCfreq)
                av_freqKDC.append(KDCfreq)
                avhelper = float((len((av_q)) - sum(av_q)) / (len(av_q)))
                freq_alive = float((len(BATTERY_STATE)) - BatteryOFFcoun) / len(BATTERY_STATE)
                # DEBUG LIST ================!!!!!!!!!!!!!!++++++++++++++++++ :)
                stringRules="" #String with help with debug txt
                for x in RULES:
                    if(x==1):
                        stringRules+= str(g.valuesRadiokDstate.get())+"D "
                    elif (x == 2):
                        stringRules += str(g.valuesRadiokCstate.get()) + "C "
                    elif(x==3):
                        stringRules += str(g.valuesRadiokDCstate.get()) + "DC "
                    else:
                        stringRules += "OFF "
                stringNeigh=""
                hh=""
                for x in TempDebugList:
                    hh=str(x)
                    hh=hh.replace(" ", "")
                    stringNeigh+= str(hh) + "  "

                #FOR FIRST ITERATION
                stringNeighs = ""
                hhs = ""
                for x in Neighb:
                    hhs = str(x) #tutaj zawyza liczbe bo traktuje 10
                    hhs=hhs.replace("10","0")
                    hhs = hhs.replace("11", "0")
                    hhs = hhs.replace("12", "0") #ZMIANA REPLACE -{}-
                    hhs = hhs.replace(" ", "")
                    stringNeighs += str(len(hhs)) + "  "
                stringstatedisplay=""
                for x in STATE:
                    stringstatedisplay+= str(x) + "  "
                helperStringwithTempDebugList=str(tempListofNumbers)
                if(".3"in helperStringwithTempDebugList ):
                    ListDebug.append(str(int(
                        i)) + "       " + stringstatedisplay + "   " + stringRules + "             " + stringNeigh)
                else:
                    ListDebug.append(str(int(i)) + "       "+ stringstatedisplay +"   "+ stringRules + "             "+stringNeighs)
                TempDebugList.clear() # Clear after add to table
                def SaveFileSensss():
                    with open("RESULT/CA_result.txt"
                              "", 'w') as file:
                        for row in ListSensorneighQresult:
                            s = "".join(map(str, row))
                            file.write(s + '\n')
                def SaveFileDebug():
                    with open("RESULT/Debug.txt"
                              "", 'w') as file:
                        for row in ListDebug:
                            s = "".join(map(str, row))
                            file.write(s + '\n')

                SaveFileSensss()
                SaveFileDebug()
            # print("STATE LIST NEIGH")
            # print(StateListNeigh)
            #NewState.clear()
            # =====================================================================
            CalcALLq()
            STATE.clear()
            iterr = 0
            for x in RULES:
                if (x == 1):  # StateListNeigh[iter][2]<K[iter]
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):  # int(re.search(r'\d+', x[0:2]).group())
                        STATE.append(1)  # int(re.search(r'\d+', x[0:2]).group()
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==" "): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                elif (x == 2):
                    if (int(re.search(r'\d+', StateListNeigh[iter][0:2]).group()) <= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        STATE.append(1)
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==" "): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                else:
                    if (int(re.search(r'\d+', StateListNeigh[iter][2:4]).group()) >= int(K[iter]) and BATTERY_STATE[
                        iterr] > 0):
                        STATE.append(1)
                        iter += 1
                    else:
                        if(BATTERY_STATE[iterr]>0 and Neighb[iter]==' '): # TESTOWEEEE DO DEBUGA
                            STATE.append(1)
                            iter += 1
                        else:
                            STATE.append(0)
                            iter +=1
                # Battery STATE
                if (1 == int(STATE[iterr])):
                    BATTERY_STATE[iterr] -= int(g.labelBattery.get())
                    if(BATTERY_STATE[iterr]<int(g.labelBattery.get())):
                         BATTERY_STATE[iterr]=0
                iterr += 1
            #print("STATE")
            ##print(STATE)
            #print("STATE LIST NEIG")
            #print(StateListNeigh)
            #print("Neigh")
            #print(Neighb)
            #print("NEW STATE")
            #print(NewState)
            # ======================================================================ALL COV Q ##################################
            #CalcALLq() # uruchomienie glownego algorytmu
            #
            BatterY_STATE_SUM.append(sum(BATTERY_STATE))
            #print("BATTERY STATE")
            #print(BATTERY_STATE)
            increse=0
            for x in BATTERY_STATE:
                if(x<=0):
                    tempListofNumbers[increse]="3"+str(increse)+".3 33.3"
                increse+=1
            def FindWSNGRAPH():  # find WSN grapph #GO GO GO
                #tempListofNumbers.clear()
                def circle(x1, y1, x2, y2, r1, r2):
                    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                    radSumSq = (r1 + r2) * (r1 + r2)
                    if (distSq == radSumSq):
                        return 1
                    elif (distSq > radSumSq):
                        return -1
                    else:
                        return 0
                ys = " " # zmiana ys na " " testowanie
                counter = 1
                TempDebugList.clear()
                for x in tempListofNumbers:
                    id = 1
                    helper = 0
                    for y in tempListofNumbers:
                        if(y[2:4]==".3" or x[2:4] ==".3" or x[3:5]==".3"): # zmiana or z x
                            ListofNeighbourse.append(str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       0, 0)))
                            xs = str(id) + str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                       0, 0))
                            beng = '-'
                        else:
                            ListofNeighbourse.append(str(id) + str(
                            circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                   int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                   int(gs.radius.get()), int(gs.radius.get()))))
                            xs = str(id) + str(
                            circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                   int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                                   int(gs.radius.get()), int(gs.radius.get())))
                            beng = '-'
                        if (beng in xs or str(counter) == xs[0:1] or str(counter)==xs[0:2]): #or str(counter)==xs[0:2]): zmiana
                            donothing()
                        else:
                            if (len(xs) < 3): #100 6-1
                                ys += xs[0] + " "
                                helper = helper + 1
                            else:
                                ys += xs[0:2] + " "
                                helper = helper + 1
                        id = id + 1
                    TempDebugList.append(str(helper))
                    Neighb.append(ys)
                    ys = " "
                    ListofNeighbourse.clear()
                    counter = counter + 1
            #STATE = NewState
            Neighb.clear() #CHANGE
            FindWSNGRAPH()
            StateListNeigh.clear()
    MainIter()

def MamutDebug():
    if(g.labelMuttiruns.get()>'1'):
        ms.showerror("! ! !","Debug mode only for Mulituns = 1")
    else:
        for i in range(int(g.labelMuttiruns.get())):
            DisplayBeutyful()
        if (int(g.labelMuttiruns.get()) > 1):
            def SaveFileSenss():
                with open("RESULT/Ca_result_std.txt"
                          "", 'w') as file:
                    for row in ListSensorneighQ:
                        s = "".join(map(str, row))
                        file.write(s + '\n')
        else:
            def Exit():
                python = sys.executable
                os.execl(python, python, *sys.argv)
            Exit()
        ListSensorneighQ.append("#Number of Sensors " + str(gs.amountReadWSN))
        ListSensorneighQ.append("#Sensor Range: " + str(gs.radius.get()))
        ListSensorneighQ.append("#POI: " + str(len(gs.ListPOI)))
        ListSensorneighQ.append("#Sensor for file: " + str(gs.filename))  # radiusTxt) CHANGE
        ListSensorneighQ.append("Battery Unit : " + str(g.labelBattery.get()))
        ListSensorneighQ.append("Iterations: " + str(g.labelIterationNumb.get()))
        ListSensorneighQ.append("Multiruns: " + str(g.labelMuttiruns.get()))
        ListSensorneighQ.append("prob KD: " + str(g.labelkDvalue.get()))
        ListSensorneighQ.append("prob KC: " + str(g.labelkCvalue.get()))
        ListSensorneighQ.append("prob KDC: " + str(g.labelkDCvalue.get()))
        ListSensorneighQ.append("Strategies 1-KD , 2 -KC ,3 KDC ->" + str(RULES))
        ListSensorneighQ.append(
            "iter, av_q, std_q, av_falive, std f_alive, av minBatt, std minBatt, av avBatt, std avBatt,  av maxBatt, std maxBatt, av freq_kD, std freq_kD, av freq_kC, std freq_kC, av freq_kDC, std freq_kDC")
        # HELPERS List
        # avhelper = float((len((av_alive)) - sum(av_alive)) / (len(av_alive)))
        # ListSensorneighQ.append(
        #    "       av_falive std f_alive " + str(round(avhelper, 2)) + " " + str(round(np.std(av_alive), 2)))
        # avhelper = float(sum(av_minBatt) / (len(BatterY_STATE_SUM)))
        ax = int(g.labelIterationNumb.get())
        for i in range(int(g.labelIterationNumb.get())):
            avqhelper = float(sum(ListQ[i::ax]) / (len(ListQ[i::ax])))
            #print(str(avqhelper) + " " + str(
            #    ListQ[i::8]))  # Z KAZDEJ ITERACJI JEST LICZONA SREDNIA -> Dac for dzielacego na liczbe multirunow
            avalife = float(sum(ListF[i::ax]) / (len(ListF[i::ax])))
            minhelper = float(sum(ListminBatt[i::ax]) / (len(ListminBatt[i::ax])))
            avbathelperr = float(sum(lisavBatt[i::ax]) / (len(lisavBatt[i::ax])))
            maxbathelperr = float(sum(ListmaxBatt[i::ax]) / (len(ListmaxBatt[i::ax])))
            listkdhelperr = float(sum(listfreqKD[i::ax]) / (len(listfreqKD[i::ax])))
            listkchelper = float(sum(listfreqKC[i::ax]) / (len(listfreqKC[i::ax])))
            listkdchelper = float(sum(listfreqKDC[i::ax]) / (len(listfreqKDC[i::ax])))
            ListSensorneighQ.append(
                str(i) + "     " + str(round(avqhelper, 2)) + "    " + str(round(np.std(ListQ[i::ax]), 2)) +
                "      " + str(round(avalife, 2)) + "       " + str(round(np.std(ListF[i::ax]), 2)) +
                "         " + str(round(minhelper, 2)) + "           " + str(round(np.std(ListminBatt[i::ax]), 2)) +
                "        " + str(round(avbathelperr, 2)) + "        " + str(round(np.std(lisavBatt[i::ax]), 2)) +
                "         " + str(round(maxbathelperr, 2)) + "          " + str(round(np.std(ListmaxBatt[i::ax]), 2)) +
                "       " + str(round(listkdhelperr, 2)) + "         " + str(round(np.std(listfreqKD[i::ax]), 2)) +
                "        " + str(round(listkchelper, 2)) + "           " + str(round(np.std(listfreqKC[i::ax]), 2)) +
                "        " + str(round(listkdchelper, 2)) + "          " + str(round(np.std(listfreqKDC[i::ax]), 2)))
        SaveFileSenss()
        def Exit():
                        python = sys.executable
                        os.execl(python, python, *sys.argv)
        Exit()




