'''
import subprocess
lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
#lpr.stdin.write("Heloo")

#this lines of code means that all data read from file as bytes objects not str 
with open('output.txt','rb') as file:
    for f in file:
        lpr.stdin.write(f)
'''

import os
os.system("lpr -P MFCL2700DW -o landscape -o fit-to-page -o media=A4 output.txt")
