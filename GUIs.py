import Methods as m
import tkinter as tk #Python3.7.8
Pi=3.14
ListPOI=[] #List which contains POI #X #Y
#LABELS VALUE
labelkDvalue = ""
labelkCvalue = ""
labelkDCvalue = ""
labelBattery=""
labelIterationNumb=""
labelMuttiruns=""
labelSetSeed=""
#1-10 KC-KD-KDC
valuesRadiokCstate=""
valuesRadiokDstate=""
valuesRadiokDCstate=""
staticStrategies=""
#BAttery STATE
labelBattery="kc,kd,kdc,kd,kc,kc,kd,kdc,kc,kc"
def InitGuis():
    #GLOVAL VALUE TO METHODS
    global labelkCvalue
    global labelkDvalue
    global labelkDCvalue
    global valuesRadiokCstate
    global valuesRadiokDstate
    global valuesRadiokDCstate
    global labelBattery
    global labelIterationNumb
    global labelSetSeed
    global labelMuttiruns
    global staticStrategies
    main_windower=tk.Tk()
    staticStrategies=tk.StringVar()
    labelkDvalue = tk.StringVar()
    labelkCvalue = tk.StringVar()
    labelkDCvalue = tk.StringVar()
    labelBattery = tk.StringVar()
    labelIterationNumb = tk.StringVar()
    labelMuttiruns = tk.StringVar()
    labelSetSeed = tk.StringVar()
    labelkDvalue.set("0.33")
    labelkCvalue.set("0.33")
    labelkDCvalue.set("0.34")
    #staticStrategies.set("kc,kd,kdc,kd,kc,kc,kd,kdc,kc,kc")
    labelBattery.set("1")
    labelIterationNumb.set("8")
    labelMuttiruns.set("1")
    labelSetSeed.set('None')
    def choiceD(text):
        valuesRadiokDstate.set(text)
    def choiceC(text):
        valuesRadiokCstate.set(text)
    def choiceDC(text):
        valuesRadiokDCstate.set(text)
    valuesRadiokD = {"0D": "0", "1D": "1", " 2D": "2", "3D": "3", "4D": '4', "5D": '5', "6D": '6', '7D': '7', '8D': '8',
                     '9D': '9', '10D': '10'}
    valuesRadiokDstate = tk.StringVar(main_windower, '2')
    valuesRadiokC = {"0C": "0", "1C": "1", " 2C": "2", "3C": "3", "4C": '4', "5C": '5', "6C": '6', '7C': '7', '8C': '8',
                     '9C': '9', '10C': '10'}
    valuesRadiokCstate = tk.StringVar(main_windower, '2')
    valuesRadiokDC = {"0DC": "0", "1DC": "1", " 2DC": "2", "3DC": "3", "4DC": '4', "5DC": '5', "6DC": '6', '7DC': '7', '8DC': '8',
                     '9DC': '9', '10DC': '10'}
    valuesRadiokDCstate = tk.StringVar(main_windower, '2')
    tk.Label(main_windower,text="kD").grid(row=0,column=0)
    iterKd=1
    for (text, value) in valuesRadiokD.items():
        tk.Radiobutton(main_windower, text=text, variable=valuesRadiokDstate,
                       value=value, command=choiceD(value)).grid(row=iterKd,column=0,sticky="NSEW")
        iterKd+=1
    iterKd=1
    tk.Label(main_windower, text="kC").grid(row=0, column=1)
    for (text, value) in valuesRadiokC.items():
        tk.Radiobutton(main_windower, text=text, variable=valuesRadiokCstate,
                       value=value, command=choiceC(value)).grid(row=iterKd,column=1,sticky="NSEW")
        iterKd+=1
    iterKd=1
    tk.Label(main_windower, text="kDC").grid(row=0, column=2)
    for (text, value) in valuesRadiokDC.items():
        tk.Radiobutton(main_windower, text=text, variable=valuesRadiokDCstate,
                       value=value, command=choiceDC(value)).grid(row=iterKd,column=2,sticky="NSEW")
        iterKd+=1
        #Display value of method
    def dispalyValRules():
        print(valuesRadiokCstate.get())
        print(valuesRadiokDstate.get())
        print(valuesRadiokDCstate.get())

    tk.Label(main_windower, text="Probability").grid(row=12)
    tk.Label(text="prob kD").grid(row=13,column=0)
    tk.Entry(main_windower, textvariable=labelkDvalue, width=10, borderwidth=5).grid(row=14,column=0)
    tk.Label(text="prob kC").grid(row=13, column=1)
    tk.Entry(main_windower, textvariable=labelkCvalue, width=10, borderwidth=5).grid(row=14, column=1)
    tk.Label(text="prob kDC").grid(row=13, column=2)
    tk.Entry(main_windower, textvariable=labelkDCvalue, width=10, borderwidth=5).grid(row=14, column=2)
    tk.Label(text="Battery unit charge").grid(row=15,column=0)
    tk.Entry(main_windower, textvariable=labelBattery, width=10, borderwidth=5).grid(row=15, column=1)
    tk.Label(text="iter numb").grid(row=16, column=0)
    tk.Entry(main_windower, textvariable=labelIterationNumb, width=10, borderwidth=5).grid(row=16, column=1)
    tk.Label(text="Multiruns").grid(row=17, column=0)
    tk.Entry(main_windower, textvariable=labelMuttiruns, width=10, borderwidth=5).grid(row=17, column=1)
    tk.Label(text="set seed").grid(row=18, column=0)
    tk.Entry(main_windower, textvariable=labelSetSeed, width=10, borderwidth=5).grid(row=18, column=1)
    tk.Button(main_windower,text="Start",command=m.Mamut).grid(row=20,column=1)
    tk.Button(main_windower, text="Start by iter", command=m.Mamut).grid(row=21, column=1)
    tk.Button(main_windower, text="DEBUG", command=m.MamutDebug).grid(row=22, column=1)
    tk.Label(text="For file WSN-5d: \n"
                  "If you choose file with 5 sensors you have to write \n correctly amount of strategies equal 5").grid(row=23, column=1)
    tk.Label(text="INPUT -> kc,kd,kdc,kd,kdc").grid(row=24, column=1)
    tk.Entry(main_windower, textvariable=staticStrategies, width=20, borderwidth=5).grid(row=25,column =1 )

    #tk.Button(main_window, text="Start ", command=m.Startstandard).grid(row=19, column=1)
    #==========================================================#
    #GUI DATA - > #READ POI #READ DATA X,Y
    #tk.Button(main_windower, text="READ WSN", command=m.OpenSensorWSN).grid(row=19, column=4)

















    main_windower.mainloop()