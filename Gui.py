import tkinter
from tkinter import *


root = Tk()
root.geometry('400x400')
root.title('Whatsapp!')
root.resizable(False, False)

toplabel = Label(root, text='Whatsapp text program', font= 'verdana 15')
toplabel.place(x=110, y=0)

inputboxtext =Label(root, text = "Skriv nummeret her", borderwidth=1, relief='sunken')
inputboxtext.place(x= 10, y=50)

inputbox = Entry(root, bd=3, justify='center')
inputbox.place(x= 6.5, y= 80, width=130)

inputboxtext1 =Label(root, text = "Skriv tida her", borderwidth=1, relief='sunken')
inputboxtext1.place(x= 30, y=140)

inputbox1 = Entry(root, bd=3, justify='center')
inputbox1.place(x= 6.5, y= 170, width=130)

Melding = Label(text='Melding', borderwidth=1, relief='sunken')
Melding.place(x=250, y= 50)
tekst = Text(root)
tekst.place(x=160, y=80, width= 230, height=260)

selection = IntVar()

rb= Radiobutton(text='Send nå', variable=selection, value=4000).place(x=20, y= 290)
rb1= Radiobutton(text='Send på tida', variable=selection, value= 3850).place(x=20, y= 315)

selection.set(3850)

button = tkinter.Button(root, text='Send Melding', width=25, command=root.destroy)
button.place(x=70, y=350)






root.mainloop()
