import tkinter
from tkinter import *
from tkinter import messagebox as tkMessageBox
import pywhatkit
import time


root = Tk()
root.geometry('400x400')
root.title('Whatsapp!')
root.resizable(False, False)
#########################################################################################################
inputboxtext =Label(root, text = "Skriv nummeret her", borderwidth=1, relief='sunken')
inputboxtext.place(x= 10, y=50)

number_str = StringVar()
inputbox = Entry(root, textvariable=number_str, bd=3, justify='center')
inputbox.insert(0, "+47")
inputbox.place(x= 6.5, y= 80, width=130)

def whatsapp():
   try:
      number = inputbox.get()
      message = tekst.get()
      time = int(inputbox1.get())
      time2 = int(inputbox2.get())
      pywhatkit.sendwhatmsg(number, message, time, time2, wait_time=60)

   except:
      tkMessageBox.showerror("error!!","Fill ut detalier!")
#####################################################################################################

#tid
inputboxtext1 =Label(root, text = "Skriv tida her", borderwidth=1, relief='sunken')
inputboxtext1.place(x= 30, y=140)

#tidfunksjon
inputbox1 = Entry(root, bd=3, justify='center')
inputbox1.place(x= 26, y= 170, width=40)
inputbox1.insert(0, "00")

inputbox2 = Entry(root, bd=3, justify='center')
inputbox2.place(x= 79, y= 170, width=40)
inputbox2.insert(0, "00")

klokke =Label(root, font=20,fg="white", bg="black")
klokke.place(x=130, y=10)

def localtime():
   t = time.localtime()
   current_time = time.strftime("%H:%M:%S", t)
   klokke.config(text="Localtime:"+current_time)
   klokke.after(200, localtime)

localtime()


#########################################################################################################
Melding = Label(text='Melding', borderwidth=1, relief='sunken')
Melding.place(x=250, y= 50)

message_str = StringVar()
tekst = (Entry(root, textvariable=message_str, bd=3, justify= "center"))
tekst.insert(0, "Skriv meldingen her")
tekst.place(x=160, y=80, width= 230, height=260)
#########################################################################################################


def callback():
   tkMessageBox.showinfo( "Info", "Meldingen er send")


send = tkinter.Button(root, text='Send Melding', width=25, command=whatsapp)
send.place(x=70, y=350)





root.mainloop()
