# Author   : Isaiah Jared

from tkinter import *
from tkinter import ttk
import random

# window
window = Tk()
window.title("Die Roller")
window.minsize(450,400)

header = Label(window, text="", bg="black", fg="green")
header.grid(column=1, row=0)
header.configure(text="DND Die Roller", bg="black", fg="green", font=("System", 20, "bold"), justify="center")

headerSep = ttk.Separator(window,orient=HORIZONTAL)

# label for roll results, could be improved by displaying images instead
lbl = Label(window, text="")
lbl.grid(column=1,row=3,padx=50)


# dice functions; called by button presses

def D4():
  d4_roll = random.sample(range(1,4), 1)
  lbl.configure(text="You rolled a {}".format(d4_roll))

def D6():
  d6_roll = random.sample(range(1,6), 1)
  lbl.configure(text="You rolled a {}".format(d6_roll))
def D8():
  d8_roll = random.sample(range(1,8), 1)
  lbl.configure(text="You rolled a {}".format(d8_roll))
def D10():
  d10_roll = random.sample(range(1,10), 1)
  lbl.configure(text="You rolled a {}".format(d10_roll))

def D12():
  d12_roll = random.sample(range(1,12), 1)
  lbl.configure(text="You rolled a {}".format(d12_roll))

def D20():
  d20_roll = random.sample(range(1,20), 1)
  lbl.configure(text="You rolled a {}".format(d20_roll))
    

# buttons

# adjust padding accordingly padx(#,#) pady(#,#), left/right and top/bottom respectively
btn = Button(window, text="Roll D4",command=D4)
btn.grid(column=0, row=1,padx=25,pady=10)
btn = Button(window, text="Roll D6",command=D6)
btn.grid(column=0, row=2,padx=25,pady=10)
btn = Button(window, text="Roll D8",command=D8)
btn.grid(column=0, row=3,padx=25,pady=10)
btn = Button(window, text="Roll D10",command=D10)
btn.grid(column=0, row=4,padx=25,pady=10)
btn = Button(window, text="Roll D12",command=D12)
btn.grid(column=0, row=5,padx=25,pady=10)
btn = Button(window, text="Roll D20",command=D20)
btn.grid(column=0, row=6,padx=25,pady=10)

window.mainloop()
