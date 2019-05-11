##import cv2
##import numpy as np
##cap = cv2.VideoCapture(1)
##while True:
##    ret,img=cap.read()
##    cv2.imshow('video output',img)
##    k=cv2.waitKey(10)& 0xff
##    if k==27:
##        break
##cap.release()
##cv2.destroyAllWindows()

import os
import subprocess
import time
import Tkinter,tkFileDialog
from Tkinter import *
from tkFileDialog import askopenfilename
import ttk
import tkMessageBox
import warnings

global entrybox
global kwargs
global pathvals

warnings.filterwarnings("ignore")

def getsettings():
    global pathvals
    pathvals = []
    with open("PATH.INI", 'r') as f:
        for line in f:
            pathvals.append(line.strip())

def takeone():
    result = tkMessageBox.askquestion("Take a Picture?", "Take a Picture?", icon='question')
    if result == 'yes':
        return True
    else:
        return False


def takeanother():
    result = tkMessageBox.askquestion("Take Another Picture?", "Take Another Picture?", icon='question')
    if result == 'yes':
        return True
    else:
        return False

def camera(serialnumber = None, count = 1, timestmp = ""):
    try:
        status = ""
        loc = str(pathvals[0])+"\\"
        os.chdir(loc)
        fldloc = str(pathvals[1])
        cmd = "CameraControlCmd.exe /filename C:\\test\\test.jpg /capture"
        cmd = cmd.replace('C:\\test', fldloc)
        nwfile = str(serialnumber)+"_"+timestmp+"_"+str(count)+".jpg"
        cmd = cmd.replace('test.jpg', nwfile)
        r = subprocess.check_output(cmd, shell=True)
        #If any issues occur IE focus problems an Error message will be returned
        if "Error" in r or "No connected device was found !" in r or r.count('connected') > 1:
            #Display a message is an issue occurs
            tkMessageBox.showinfo(title="OH NO!!!", message="Problem With Camera!!! "+r)
            status = "Error"
        else:
            status = "Success"
        return status
    except:
        status = "Error"
        return status


def camera_stat():
    try:
        status = ""
        loc = str(pathvals[0])+"\\"
        os.chdir(loc)
        #Get Camera Status using Verbose if camera not connected no device found message will be returned
        r = subprocess.check_output("CameraControlCmd.exe /verbose", shell=True)
        if "No connected device was found !" in r or r.count('connected') > 1:
            #Display a message is an issue occurs
            tkMessageBox.showinfo(title="OH NO!!!", message="Problem With Camera!!! "+r)
            return False
        else:
            return True
    except:
        return False



def close_window():
    try:
        root.destroy()
        sys.exit(0)
    except:
        pass

def x_override():
    pass

def anotherpic(stat):
    try:
        global kwargs
        count = kwargs.get('count')
        if stat == "Success":
            if (takeanother()):
                count +=1
                kwargs["count"]=count
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def main():
    global entrybox
    global kwargs
    count = 1
    sn=entrybox.get()
    tmstp = str(int(time.time()))
    if (len(sn) > 0):
        entrybox.delete(0, 'end')
        if takeone() and camera_stat():
            kwargs = {"serialnumber":sn,"count":count,"timestmp":tmstp}
            while True:
                try:
                    if not anotherpic(camera(**kwargs)):
                        break
                except:
                    tkMessageBox.showinfo(title="OH NO!!!", message="Problem With Camera!!!")
                    break

#Get folder path values from INI file
getsettings()
#Main GUI
root = Tkinter.Tk()
# this removes the maximize button
root.resizable(width=False, height=False)
#Removes the boarder
#root.overrideredirect(1)
root.title("MCA Visual Record")
root["padx"] = 200
root["pady"] = 60

W = Label(root, text="Please Enter a Serial Number")
entrybox=Entry(root)
entrybox.insert(0,"")
entrybox.select_range(0,END)
entrybox.focus_set()
entrybox.pack()
B = Tkinter.Button(root, text ="Start", command = main)
C = Tkinter.Button(root, text="Close", command=close_window)
W.pack()
B.pack()
C.pack()
#root.bind('<Return>', main)
#Overrides the X close button function has to be above
#this line to see what to do, no prototype
root.protocol('WM_DELETE_WINDOW', x_override)
root.mainloop()
