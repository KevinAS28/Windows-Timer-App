#Import the required library
from tkinter import *
import time

def startTimer(h, m, s, pending_function, onclose_function):
    #Create an instance of tkinter frame
    win = Tk()
    win.protocol("WM_DELETE_WINDOW", lambda: onclose_function(win))
    win.geometry('300x100+0+0')
    
    win.resizable(False,False)
    #Configure the background
    win.config(bg='burlywood1')
    #Create Entry Widgets for HH MM SS
    sec = StringVar()
    Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=175, y=50)
    sec.set(str(s))
    mins= StringVar()
    Entry(win, textvariable = mins, width =2, font = 'Helvetica 14').place(x=135, y=50)
    mins.set(str(m))
    hrs= StringVar()
    Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=103, y=50)
    hrs.set(str(h))

    win.configure(background='gold')
    win.lift()

    #Define the function for the timer
    def countdowntimer():
        times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
        while times > -1:
                if times<=60:
                    win.config(bg='red')

                minute,second = (times // 60 , times % 60)
                hour =0
                if minute > 60:
                    hour , minute = (minute // 60 , minute % 60)
                sec.set(second)
                mins.set(minute)
                hrs.set(hour)
                #Update the time
                win.update()
                time.sleep(1)
                if(times == 0):
                    sec.set('00')
                    mins.set('00')
                    hrs.set('00')
                times -= 1
        pending_function(win)
    Label(win, font =('Helvetica bold',22), text = 'Sisa Waktu Anda',bg='burlywood1').place(x=50,y=0)
    # Button(win, text='START', bd ='2', bg = 'IndianRed1',font =('Helveticabold',10), command = countdowntimer).place(x=167, y=165)
    countdowntimer()
    win.mainloop()

if __name__=='__main__':
    startTimer(0, 1, 3)