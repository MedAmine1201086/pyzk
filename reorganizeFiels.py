import shutil, glob, os
try:
    for text_file in glob.iglob('clean*.txt'):
        shutil.move("/home/medamine/pyzk/"+text_file, "/home/medamine/pyzk/Clean Pointage/"+text_file)
except:
    pass

try:
    for text_file in glob.iglob('finalRapport*.txt'):
        shutil.move("/home/medamine/pyzk/"+text_file, "/home/medamine/pyzk/Rapport Journalier/"+text_file)
except:
    pass

try:
    for text_file in glob.iglob('outputJourn*.txt'):
        shutil.move("/home/medamine/pyzk/"+text_file, "/home/medamine/pyzk/Output Journalier/"+text_file)
except:
    pass

try:
    for text_file in glob.iglob('pointage*.txt'):
        shutil.move("/home/medamine/pyzk/"+text_file, "/home/medamine/pyzk/Pointages/"+text_file)
except:
    pass

try:
    for text_file in glob.iglob('output*.txt'):
        shutil.move("/home/medamine/pyzk/"+text_file, "/home/medamine/pyzk/Rapport Mensuel ou Par Semaine/"+text_file)
except:
    pass