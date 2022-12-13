import pyautogui as pg
import time
import os
import tkinter as tk

#place the cursor in the whatsapp chat windows before executing the code
def autoTagger():

    time.sleep(5)
    try:
        participantCount = int(npVariable.get())
        for i in range(participantCount - 1):
            pg.write('@')
            if i > 0:
                pg.press('down')
            pg.press('enter')
            time.sleep(0.2)
    except:
        print("Invalid Paricipant Count")
        return




windowMain = tk.Tk(className=' Auto Tagger')
windowMain.geometry("400x200")
npVariable = tk.StringVar()

label = tk.Label(windowMain, text="No of Participants")
npEntry = tk.Entry(windowMain, textvariable=npVariable)
btnTag = tk.Button(windowMain, text="Tag", command=autoTagger)
btnTag.config(width=20, height=2)

label.pack()
npEntry.pack()
btnTag.pack()
windowMain.mainloop()


