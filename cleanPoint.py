from datetime import date, timedelta
from prettytable import PrettyTable
import datetime

sdate = date(2019, 11, 11)   # start date
edate = date(2019, 11, 16)   # end date
delta = edate - sdate

def attendDate(string):
        fp = open('deviceOutput.txt', 'r')

        todayAttendance = []

        for line in fp:
            go = line.split()
            if(go[3] == string):
                todayAttendance.append(go)

        return todayAttendance

def findDate(today):
    if(today.weekday() == 0):
        day = "Lundi"
    if(today.weekday() == 1):
        day = "Mardi"
    if(today.weekday() == 2):
        day = "Mercredi"
    if(today.weekday() == 3):
        day = "Jeudi"
    if(today.weekday() == 4):
        day = "Vendredi"
    if(today.weekday() == 5):
        day = "Samedi"
    if(today.weekday() == 6):
        day = "Dimanche"

    return day 

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    today = datetime.datetime(int(str(day)[0:4]), int(str(day)[5:7]), int(str(day)[8:]))
    date = str(day)

    day = findDate(today)

    KhalifaAttendance= []
    TaherAttendance= []
    SalehAttendance= []
    MedAmeurAttendance= []
    ChokriBrahemAttendance= []
    AliAttendance= []
    RihabAttendance= []
    MedHediAttendance= []
    AymenAttendance= []
    MarwenAttendance= []
    MouniraAttendance= []
    LazherAttendance= []
    RamziAttendance= []
    SofieneAttendance= []
    BilelAttendance= []
    ChakrounAttendance= []
    AmineBenAfiaAttendance= []
    N55Attendance= []
    NN17Attendance= []
    HabibaAttendance = []
    IkhlassAttendance = []
    FaizaAttendance = []

    for nb in attendDate(date):
        if(nb[1] == '1'):
            nb[1] = "Khalifa"
            nb = nb[: len(nb) - 2]
            KhalifaAttendance.append(nb)
        if(nb[1] == '2'):
            nb[1] = "Taher"
            nb = nb[: len(nb) - 2]
            TaherAttendance.append(nb)
        if(nb[1] == '3'):
            nb[1] = "Saleh"
            nb = nb[: len(nb) - 2]
            SalehAttendance.append(nb)
        if(nb[1] == '4'):
            nb[1] = "MedAmeur"
            nb = nb[: len(nb) - 2]
            MedAmeurAttendance.append(nb)
        if(nb[1] == '5'):
            nb[1] = "ChokriBrahem"
            nb = nb[: len(nb) - 2]
            ChokriBrahemAttendance.append(nb)
        if(nb[1] == '7'):
            nb[1] = "Ali"
            nb = nb[: len(nb) - 2]
            AliAttendance.append(nb)
        if(nb[1] == '9'):
            nb[1] = "Rihab"
            nb = nb[: len(nb) - 2]
            RihabAttendance.append(nb)
        if(nb[1] == '10'):
            nb[1] = "MedHedi"
            nb = nb[: len(nb) - 2]
            MedHediAttendance.append(nb)
        if(nb[1] == '11'):
            nb[1] = "Aymen"
            nb = nb[: len(nb) - 2]
            AymenAttendance.append(nb)
        if(nb[1] == '12'):
            nb[1] = "Marwen"
            nb = nb[: len(nb) - 2]
            MarwenAttendance.append(nb)
        if(nb[1] == '13'):
            nb[1] = "Mounira"
            nb = nb[: len(nb) - 2]
            MouniraAttendance.append(nb)
        if(nb[1] == '14'):
            nb[1] = "Lazher"
            nb = nb[: len(nb) - 2]
            LazherAttendance.append(nb)
        if(nb[1] == '15'):
            nb[1] = "Ramzi"
            nb = nb[: len(nb) - 2]
            RamziAttendance.append(nb)
        if(nb[1] == '16'):
            nb[1] = "Sofiene"
            nb = nb[: len(nb) - 2]
            SofieneAttendance.append(nb)
        if(nb[1] == '19'):
            nb[1] = "Bilel"
            nb = nb[: len(nb) - 2]
            BilelAttendance.append(nb)
        if(nb[1] == '20'):
            nb[1] = "ChokriChakroun"
            nb = nb[: len(nb) - 2]
            ChakrounAttendance.append(nb)
        if(nb[1] == '8'):
            nb[1] = "AmineBenAfia"
            nb = nb[: len(nb) - 2]
            AmineBenAfiaAttendance.append(nb)
        if(nb[1] == '6'):
            nb[1] = "Narjess"
            nb = nb[: len(nb) - 2]
            N55Attendance.append(nb)
        if(nb[1] == '17'):
            nb[1] = "Sedki"
            nb = nb[: len(nb) - 2]
            NN17Attendance.append(nb)
        if(nb[1] == '18'):
            nb[1] = "Habiba"
            nb = nb[: len(nb) - 2]
            HabibaAttendance.append(nb)
        if(nb[1] == '21'):
            nb[1] = "Ikhlass"
            nb = nb[: len(nb) - 2]
            IkhlassAttendance.append(nb)
        if(nb[1] == '22'):
            nb[1] = "Faiza"
            nb = nb[: len(nb) - 2]
            FaizaAttendance.append(nb)               

    workerAttendance = [ChokriBrahemAttendance,
                        TaherAttendance ,
                        AmineBenAfiaAttendance,
                        KhalifaAttendance, 
                        SalehAttendance, 
                        AliAttendance, 
                        RihabAttendance, 
                        MedHediAttendance,
                        MedAmeurAttendance, 
                        AymenAttendance, 
                        MarwenAttendance, 
                        MouniraAttendance, 
                        LazherAttendance, 
                        RamziAttendance, 
                        SofieneAttendance, 
                        BilelAttendance, 
                        ChakrounAttendance, 
                        N55Attendance, 
                        NN17Attendance, 
                        HabibaAttendance,
                        IkhlassAttendance,
                        FaizaAttendance]
    
    #Rapport Journalier
    y = PrettyTable()
    y.field_names = ["Ouvrier(e)", "Attendance"]

    workerAttendance2 = {"Khalifa":KhalifaAttendance,
                        "Saleh":SalehAttendance,
                        "Ali":AliAttendance,
                        "Rihab":RihabAttendance,
                        "MedHedi":MedHediAttendance,
                        "Aymen":AymenAttendance,
                        "Marwen":MarwenAttendance,
                        "Mounira":MouniraAttendance,
                        "Lazher":LazherAttendance,
                        "Ramzi":RamziAttendance,
                        "Sofiene":SofieneAttendance,
                        "Narjess":N55Attendance,
                        "Sedki":NN17Attendance,
                        "Habiba":HabibaAttendance,
                        "Bilel":BilelAttendance,
                        "Taher":TaherAttendance,
                        "AmineBenAfia":AmineBenAfiaAttendance,
                        "ChokriChakroun":ChakrounAttendance,
                        "ChokriBrahem":ChokriBrahemAttendance,
                        "MedAmeur":MedAmeurAttendance,
                        "Ikhlass":IkhlassAttendance,
                        "Faiza":FaizaAttendance            
    }
    
    for item in workerAttendance2:
        if(len(workerAttendance2[item]) > 1 ):
            y.add_row([item, workerAttendance2[item][0][4]])
            for i in range(1,(len(workerAttendance2[item]))):
                y.add_row(["", workerAttendance2[item][i][4]])
        elif(len(workerAttendance2[item]) == 1):
            y.add_row([item, workerAttendance2[item][0][4]])
        else:
            y.add_row([item, workerAttendance2[item]])
    
    tableJourn = y.get_string()
    with open('outputJourn'+day+' '+date+'.txt','w') as file:
        file.write("++++++ Rapport Journalier "+day+" "+date+"++++++\n")
        file.write(tableJourn)

    flat_list = [item for sublist in workerAttendance for item in sublist]
    
    with open('pointage'+date+'.txt', 'w') as f:
        f.write("Attendance For "+day+" "+date+"\n\n")
        for item in flat_list:
            f.write("%s\n" % item)

    #This step for removing unecassery attendance
    for attendance in workerAttendance:
        ll = []
        for i in range(0,len(attendance)-1):
            
            temp = attendance[i][4].split(':')
            temp1 = attendance[i+1][4].split(':')
            
            if((int(temp1[0]+temp1[1]) - int(temp[0]+temp[1])) < 15 ):
                ll.append(i)
                #attendance.remove(attendance[i])
        
        while True:
            if len(ll)==0: 
                break
            attendance.remove(attendance[ll[0]]) #ll[0]
            ll.pop(0)            
            ll = [i-1 for i in ll]
            

    if(day != "Samedi"):
        for attendance in workerAttendance: 
            #This step for correcting 1 attendance
            #if(len(attendance) == 1):
                #attendance.remove(attendance[0])

            #This step for correcting 2 attendance
            if(len(attendance) == 2):
                addme1 = attendance[0][:]
                addme2 = attendance[0][:]
                temp = attendance[0][4].split(':')
                temp1 = attendance[1][4].split(':')

                if(((int(temp[0]) == 8) or (int(temp[0]) == 9) or (int(temp[0]) ==  7)) and ((int(temp1[0]) == 17) or (int(temp1[0]) == 16))):
                    addme1[-1] = '12:00:00'
                    addme2[-1] = '13:00:00'
                    attendance.insert(1, addme1)
                    attendance.insert(2, addme2)
            #This step for correcting 3 attendance
            #if(len(attendance) == 3):
                #for i in range(0,len(attendance)):
                    #attendance.remove(attendance[0])
            
            #This step for correcting 5 attendance or more
            if(len(attendance) > 4):
                ll = []
                for i in range(0,len(attendance)-1):
                    
                    temp = attendance[i][4].split(':')
                    temp1 = attendance[i+1][4].split(':')
                    
                    if((int(temp1[0]) - int(temp[0])) < 3 ):
                        ll.append(i)
                
                attendance.remove(attendance[ll[0]])
    else:
        for attendance in workerAttendance:
            if(len(attendance) == 1):
                attendance.remove(attendance[0])
            if(len(attendance) == 3):
                attendance.remove(attendance[0])
            if(len(attendance) == 5):
                ll = []
                for i in range(0,len(attendance)-1):
                    
                    temp = attendance[i][4].split(':')
                    temp1 = attendance[i+1][4].split(':')
                    
                    if((int(temp1[0]) - int(temp[0])) < 2 ):
                        ll.append(i)

                attendance.remove(attendance[ll[0]])

    flat_list = [item for sublist in workerAttendance for item in sublist]
    with open('cleanPointage'+date+'.txt', 'w') as f:
        f.write("Clean Attendance For "+day+" "+date+"\n\n")
        for item in flat_list:
            f.write("%s\n" % item)

