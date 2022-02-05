from tkinter import Label, mainloop,Tk
from datetime import datetime
from tkinter import *

root= Tk()
root.title("Digital clock")
width,height= root.winfo_screenwidth(),root.winfo_screenheight()
def time():
    now= datetime.now()
    dots=[":"," "]
    seconds = datetime.strftime(now,"%S")
    if(int(seconds)% 2) == 0:
        dt_1 = str(dots[0])
        dot = (dt_1)

    else:
        dt_2 = str(dots[1])
        dot = (dt_2)
    string = datetime.strftime(now,"%A, %b %d\n%I{0}%M{1}%S %p".format(dot, dot))
    label_time.config(text=string, justify = "center")
    label_time.after(1000,time)
    

label_time = Label(
    root,
    font = ("digital numbers",65),
    background="#918887",
    foreground="#233873",
    width=width,
    height=height
)


label_time.pack(anchor="center")
label_time.master.overrideredirect(True)
label_time.master.lift()

time()

root.eval('tk::PlaceWindow . center')
root.overrideredirect(True)
root.overrideredirect(False)
root.geometry("+0+0")
root.geometry("1920x1080")
root.mainloop()
