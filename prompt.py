#Import the tkinter library
from tkinter import *
from tkinter import messagebox
#Create an instance of Tkinter frame
# win= Tk()
#Define the geometry of the function
# win.geometry("0x0")
answer = messagebox.askokcancel("Jatah anda sudah habis untuk hari ini","Untuk 1 hari, jatah anda hanya 1 kali saja, yuk coba lagi besok")
print(answer)
#Create a Label
# Label(win, text=answer, font= ('Georgia 20 bold')).pack()
# win.mainloop()