from Tkinter import *

def start_all():
   print("Roller 1 Setpoint: %s\nRoller 2 Setpoint: %s\n" % (e1.get(), e2.get()))

def stop_all():
   print("ALL Stop\n")

def start_1():
   print("Roller 1 Start at %s\n" % (e1.get()))

def stop_1():
   print("Roller 1 STOP\n")

def start_2():
   print("Roller 2 Start at %s\n" % (e1.get()))

def stop_2():
   print("Roller 2 STOP\n")

def clear():
   stop_all()
   e1.delete(0,END)
   e2.delete(0,END)
   e1.insert(5,"0")
   e2.insert(5,"0")

#
#
#	Main Loop
#
#

master = Tk()
master.title("Simple Roller Control v1.0")
Label(master, text="Roller 1 Line Speed").grid(row=0)
Label(master, text="Roller 2 Line Speed").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(5,"0")
e2.insert(5,"0")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Start', fg="green",command=start_1).grid(row=0, column=2, sticky=W, pady=4)
Button(master, text='STOP', fg="red", command=stop_1).grid(row=0, column=3, sticky=W, pady=4)
Button(master, text='Start', fg="green", command=start_2).grid(row=1, column=2, sticky=W, pady=4)
Button(master, text='STOP', fg="red", command=stop_2).grid(row=1, column=3, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Start ALL', bg="green", command=start_all).grid(row=4, column=2, sticky=W, pady=4)
Button(master, text='STOP ALL', bg="red", command=stop_all).grid(row=4, column=3, sticky=W, pady=4)
Button(master, text='Clear ALL', command=clear).grid(row=4, column=1, sticky=W, pady=4)
mainloop( )
