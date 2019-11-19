from datetime import datetime, date
from datetime import timedelta
import datetime
from prettytable import PrettyTable
import textwrap

tdef = timedelta(hours=0, minutes=0)
rapportMensuel = {  "Khalifa":[0,"","",0,tdef,""],
                    "Saleh":[0,"","",0,tdef,""],
                    "Ali":[0,"","",0,tdef,""],
                    "Rihab":[0,"","",0,tdef,""],
                    "MedHedi":[0,"","",0,tdef,""],
                    "Aymen":[0,"","",0,tdef,""],
                    "Marwen":[0,"","",0,tdef,""],
                    "Mounira":[0,"","",0,tdef,""],
                    "Lazher":[0,"","",0,tdef,""],
                    "Ramzi":[0,"","",0,tdef,""],
                    "Sofiene":[0,"","",0,tdef,""],
                    "Narjess":[0,"","",0,tdef,""],
                    "Sedki":[0,"","",0,tdef,""],
                    "Habiba":[0,"","",0,tdef,""],
                    "Bilel":[0,"","",0,tdef,""],
                    "Taher":[0,"","",0,tdef,""],
                    "AmineBenAfia":[0,"","",0,tdef,""],
                    "ChokriChakroun":[0,"","",0,tdef,""],
                    "ChokriBrahem":[0,"","",0,tdef,""],
                    "MedAmeur":[0,"","",0,tdef,""],
                    "Ikhlass":[0,"","",0,tdef,""],
                    "Faiza":[0,"","",0,tdef,"",]            
    }

sdate = date(2019, 11, 11)   # start date
edate = date(2019, 11, 16)   # end date
delta = edate - sdate
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    today = datetime.datetime(int(str(day)[0:4]), int(str(day)[5:7]), int(str(day)[8:]))
    date = str(day)
    fp = open('cleanPointage'+date+'.txt', 'r')
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

    workerAttendance = {"Khalifa":KhalifaAttendance,
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

    for line in fp:
        if line.startswith("["):
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace('\'', '')
            line = line.replace(',', '')
            newLine = line.split()
            if(newLine[1] == "Khalifa"):
                KhalifaAttendance.append(newLine)
            if(newLine[1] == "Taher"):
                TaherAttendance.append(newLine)
            if(newLine[1] == "Saleh"):
                SalehAttendance.append(newLine)
            if(newLine[1] == "MedAmeur"):
                MedAmeurAttendance.append(newLine)
            if(newLine[1] == "ChokriBrahem"):
                ChokriBrahemAttendance.append(newLine)
            if(newLine[1] == "Ali"):
                AliAttendance.append(newLine)
            if(newLine[1] == "Rihab"):
                RihabAttendance.append(newLine)
            if(newLine[1] == "MedHedi"):
                MedHediAttendance.append(newLine)
            if(newLine[1] == "Aymen"):
                AymenAttendance.append(newLine)
            if(newLine[1] == "Marwen"):
                MarwenAttendance.append(newLine)
            if(newLine[1] == "Mounira"):
                MouniraAttendance.append(newLine)
            if(newLine[1] == "Lazher"):
                LazherAttendance.append(newLine)
            if(newLine[1] == "Ramzi"):
                RamziAttendance.append(newLine)
            if(newLine[1] == "Sofiene"):
                SofieneAttendance.append(newLine)
            if(newLine[1] == "Bilel"):
                BilelAttendance.append(newLine)
            if(newLine[1] == "ChokriChakroun"):
                ChakrounAttendance.append(newLine)
            if(newLine[1] == "AmineBenAfia"):
                AmineBenAfiaAttendance.append(newLine)
            if(newLine[1] == "Narjess"):
                N55Attendance.append(newLine)
            if(newLine[1] == "Sedki"):
                NN17Attendance.append(newLine)
            if(newLine[1] == "Habiba"):
                HabibaAttendance.append(newLine)
            if(newLine[1] == "Ikhlass"):
                IkhlassAttendance.append(newLine)
            if(newLine[1] == "Faiza"):
                FaizaAttendance.append(newLine)

    f = open('finalRapport'+date+'.txt', 'w')
    f.write("*****************Attendance of "+day+" "+date+"*****************\n")
    for attendance in workerAttendance:
        t = []
        tdef = timedelta(hours=0, minutes=0)
        ret = timedelta(hours=0, minutes=15)

        if(day != "Samedi"):
            t5 = timedelta(hours=8, minutes=30)
            t6 = timedelta(hours=16, minutes=30)
        else:
            t5 = timedelta(hours=8, minutes=30)
            t6 = timedelta(hours=13, minutes=30)

        f.write("++++++++"+attendance+" attendance during this day is: \n")

        for attend in workerAttendance[attendance]:
            f.write(str(attend))
            f.write("\n")

        if(len(workerAttendance[attendance]) == 0):
            f.write(attendance+" is ABSENT today!\n")
            rapportMensuel[attendance][0] += 1
            rapportMensuel[attendance][1] += day+" "+date+"\n"
            rapportMensuel[attendance][2] += "Absent\n"
            continue
        if(len(workerAttendance[attendance]) == 1):
            f.write(attendance+" is ABSENT today!\n")
            rapportMensuel[attendance][0] += 1
            rapportMensuel[attendance][1] += day+" "+date+"\n"
            rapportMensuel[attendance][2] += "Manque du pointage\n"
            ''' Rest a verifier avec 30 october
            if((t[0] - t5) > ret):
                f.write("RETARD: "+str((t[0] - t5) - ret)+"\n")
                rapportMensuel[attendance][3] += 1
                rapportMensuel[attendance][4] += ((t[0] - t5) - ret)
                rapportMensuel[attendance][5] += day+" "+date+"\n"
            '''
            continue
        if(len(workerAttendance[attendance]) == 3):
            f.write(attendance+" is ABSENT today!\n")
            rapportMensuel[attendance][0] += 1
            rapportMensuel[attendance][1] += day+" "+date+"\n"
            rapportMensuel[attendance][2] += "Manque du pointage\n"
            #continue

        if(attendance == "Habiba"):
            for i in range(0,2):
                attend = workerAttendance[attendance][i][4]
                t.insert(i, timedelta(hours=int(attend[0:2]), minutes=int(attend[3:5])))
            workedHour = t[1]-t[0]
            if((t[0] - t5) > ret):
                f.write("RETARD: "+str((t[0] - t5) - ret)+"\n")
                rapportMensuel[attendance][3] += 1
                rapportMensuel[attendance][4] += ((t[0] - t5) - ret)
                rapportMensuel[attendance][5] += day+" "+date+"\n"
        else:
            try:
                for i in range(0,4):
                    attend = workerAttendance[attendance][i][4]
                    t.insert(i, timedelta(hours=int(attend[0:2]), minutes=int(attend[3:5])))
                workedHour = (t[1]-t[0]) + (t[3]-t[2])
                lunch = (t[2] - t[1])
                if((t[0] - t5) > ret):
                    f.write("RETARD: "+str((t[0] - t5) - ret)+"\n")
                    rapportMensuel[attendance][3] += 1
                    rapportMensuel[attendance][4] += ((t[0] - t5) - ret)
                    rapportMensuel[attendance][5] += day+" "+date+"\n"
            except:
                for i in range(0,2):
                    attend = workerAttendance[attendance][i][4]
                    t.insert(i, timedelta(hours=int(attend[0:2]), minutes=int(attend[3:5])))
                workedHour = t[1]-t[0]
                lunch = tdef
                if((t[0] - t5) > ret):
                    f.write("RETARD: "+str((t[0] - t5) - ret)+"\n")
                    rapportMensuel[attendance][3] += 1
                    rapportMensuel[attendance][4] += ((t[0] - t5) - ret)
                    rapportMensuel[attendance][5] += day+" "+date+"\n"
            
        if(lunch > timedelta(hours=1)):
            f.write("More than 1 hour lunch --> "+str(lunch))
            f.write("\n")

        if((t6-t5) < workedHour):
            Phours = abs((t6-t5) - workedHour)
            Mhours = tdef
        else:
            Mhours = abs((t6-t5) - workedHour)
            Phours = tdef

        f.write("Worked Hours: "+str(workedHour))
        f.write(" Plus Hours: "+str(Phours))
        f.write(" Minus hours: "+str(Mhours))
        f.write("\n")

#Rapport mensuel
x = PrettyTable()

x.field_names = ["Ouvrier(e)", "Nbr Absence","Jours Absent","Type d'Absence", "Nbr Retard", "Nbr Heurs Retard","Jours Retard"]
for i in rapportMensuel:
    x.add_row([i, str(rapportMensuel[i][0]), rapportMensuel[i][1], rapportMensuel[i][2], str(rapportMensuel[i][3]), str(rapportMensuel[i][4]), rapportMensuel[i][5]])

table_txt = x.get_string() 

with open('output11-16.txt','w') as file:
    st = '++++++ Rapport 11 - 16 November 2019 ++++++'
    file.write(f'\n{st:^100}\n')
    file.write(table_txt)


#Use tabulate instead
#Other method is to create docx file

