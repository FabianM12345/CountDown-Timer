# Author: Fabian Martinez
# 12/25/18
# Just a countdown Timer.

from tkinter import*
from functools import partial
import time
import winsound

def timer():

    hour = int(hrEntry.get())
    minutes = int(minEntry.get())
    seconds = int(secEntry.get())

    while hour > -1:
        while minutes > -1:
            while seconds > 0:

                seconds = seconds - 1
                root.update()
                time.sleep(1)
                display.configure(text='\r' + str(hour) + ' : ' + str(minutes) + ' : ' + str(seconds))

            minutes = minutes - 1
            seconds = 60
        hour = hour - 1
        minutes = 59
    winsound.PlaySound('Alarm_Clock.wav', winsound.SND_FILENAME)

    return

# -------------------------------------------------------------------------------------------------------------------

root = Tk()
root.geometry('400x400')
root.title('CountDownTimer')
root.configure(bg='black')

# -------------------------------------------------------------------------------------------------------------------

titleLabel = Label(root, text='CountDown Timer', fg='white', font='Ariel, 25 bold', bg='black')
titleLabel.place(x=60, y=30)

# -------------------------------------------------------------------------------------------------------------------

hrEntry = IntVar()

entry1 = Entry(root, justify='right', textvariable=hrEntry)
entry1.place(x=120, y=100, width=30)

label1 = Label(root, text=':', fg='white', bg='black')
label1.place(x=160, y=100, width=10)

# ------------------------------------------------------------------------------------------------------------------

minEntry = IntVar()

entry2 = Entry(root, justify='right', textvariable=minEntry)
entry2.place(x=180, y=100, width=30)

label2 = Label(root, text=':', fg='white', bg='black')
label2.place(x=220, y=100, width=10)

# ----------------------------------------------------------------------------------------------------------------

secEntry = IntVar()

entry3 = Entry(root, justify='right', textvariable=secEntry)
entry3.place(x=240, y=100, width=30)


# ------------------------------------------------------------------------------------------------------------

display = Label(root, bg='black', font='Arial, 30 bold', fg='white')
display.place(x=25, y=170, width=350, height=150)

getTime = partial(timer)

strtBut = Button(root, text='Start', command=getTime)
strtBut.place(x=150, y=140, width=100)

root.mainloop()