from datetime import timedelta

t5 = timedelta(hours=8, minutes=30)
t6 = timedelta(hours=16, minutes=30)

tdef = timedelta(hours=0, minutes=0)

t1 = timedelta(hours=8, minutes=30)
t2 = timedelta(hours=0, minutes=0)
t3 = timedelta(hours=0, minutes=0)
t4 = timedelta(hours=13, minutes=35)

lunch = (t3 - t2) 
workedHour = (t2-t1) + (t4-t3)

if(lunch > timedelta(hours=1)):
    print("More than 1 hour lunch!!!")

if((t6-t5) < workedHour):
    Phours = abs((t6-t5) - workedHour)
    Hp = Phours.total_seconds()//3600
    Mp = Phours.total_seconds()//60
    Mhours = tdef
    print("Hours plus: ",Hp,"\nMinutes plus: ",Mp)
else:
    Phours = tdef
    Mhours = abs((t6-t5) - workedHour)
    Hm = Mhours.total_seconds()//3600
    Mm = Mhours.total_seconds()//60
    print("Hours minus: ",Hm,"\nMinutes minus: ",Mm)

print(lunch, workedHour, Phours, Mhours)
