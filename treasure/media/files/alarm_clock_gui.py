from tkinter import *
import tkinter as tk
from time import strftime, sleep
import pygame
from tkinter import filedialog
import datetime
import threading
import sys


window = tk.Tk()

window.title("ALARM CLOCK")
window.configure(height=400, width= 600)


alarm = dict()

alarm_sound = None

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)


def get_music():
    Tk().withdraw()
    filename = filedialog.askopenfilename()
    alarm['file'] = filename
    music_lb['text'] = str(filename)
    
    
    


##def get_time():
##    h = int(hour.get())
##    m = int(minute.get())
##    dn = variable.get()
##    current = datetime.datetime.now()
##    if dn == "AM":
##        alarm_time = datetime.datetime(current.year, current.month, \
##                                       current.day, h, m)
##
##    elif dn == "PM":
##        if h >= 12:
##            alarm_time = datetime.datetime(current.year, current.month, \
##                                       current.day, h, m)
##        elif h < 12:
##            alarm_time = datetime.datetime(current.year, current.month, \
##                                       current.day, h + 12, m)
##
##    alarm['time'] = alarm_time





def start_alarm(difference):
    pygame.mixer.init()
    pygame.mixer.music.load(alarm['file'])
    sleep(difference)
    pygame.mixer.music.play()
    message['text'] = "ALARM IS ON!"
    

def stop_alarm():
    pygame.quit()
        
    
###Stop music when button pressed and destroy button
    

alarm_start = None

def show_alarm():
    global alarm_start
    h = int(hour.get())
    m = int(minute.get())
    dn = variable.get()
    current = datetime.datetime.now()
    if dn == "AM":
        alarm_time = datetime.datetime(current.year, current.month, \
                                       current.day, h, m)

    elif dn == "PM":
        if h >= 12:
            alarm_time = datetime.datetime(current.year, current.month, \
                                       current.day, h, m)
        elif h < 12:
            alarm_time = datetime.datetime(current.year, current.month, \
                                       current.day, h + 12, m)

    alarm['time'] = alarm_time
    diff = alarm['time']-datetime.datetime.now()
    alarm_lb["text"] = "Alarm at " + str(alarm["time"])
    alarm_start = threading.Thread(target=start_alarm, args = (diff.seconds,))
    alarm_start.start()
    
    
    

    



lbl = Label(window, font = ('calibri', 40, 'bold'), 
            foreground = 'black')

hour = Entry(window)
symbol = Label(window, text = ":")
minute = Entry(window)

#save = Button(window, text="SAVE", command=get_time)
music = Button(window, text="SELECT MUSIC FILE", command=get_music)


l = ["AM", "PM"]

variable = StringVar(window)
variable.set(l[0])
day_night = OptionMenu(window, variable, *l)
set_button = Button(window, text="SET", command=show_alarm, width=10)

music_lb = Label(window, text="File: ")
alarm_lb = Label(window, text="Your alarm: ")

message = Label(window, text="")
stop_button = Button(window, text="STOP ALARM", command=stop_alarm)
    



time()


lbl.grid(row=0, columnspan=4)
hour.grid(row=1, column=0, sticky=W, padx=10)
symbol.grid(row=1, column=1)
minute.grid(row=1, column=2, sticky=W, padx=10)
day_night.grid(row=1, column=3, sticky=W)

music.grid(row=2, column=0, sticky=W+E, padx=10, columnspan=2, pady=10)

set_button.grid(row=2, column=2, columnspan=1, sticky=W+E, pady=10)

music_lb.grid(row=3, columnspan=4)

alarm_lb.grid(row=4, columnspan=4)

message.grid(row=5, columnspan=4)

stop_button.grid(row=6, columnspan=4)





window.mainloop()


sys.exit()






