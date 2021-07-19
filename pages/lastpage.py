import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
FONT = ("Verdana", 15)
result=True

def lastPage():
    wind=tk.Tk()
    wind.title("Winner")
    f=open("winner.txt","r")
    win=f.read()
    f.close()
    lWin = ttk.Label(wind, text=win, font=FONT)
    lWin.grid(row=1, column=1,columnspan=2, padx=10, pady=10)
    f=open("score.txt","r")
    score=f.read()
    lScore = ttk.Label(wind, text="Player score is: "+score, font=FONT)
    lScore.grid(row=2, column=1,columnspan=2, padx=10, pady=10)
    button1 = ttk.Button(wind, text="Play Again", command=lambda: playagain())
    button1.grid(row=3, column=1, padx=10, pady=10)

    button2 = ttk.Button(wind, text="Exit",command=lambda: bore())
    button2.grid(row=3, column=2, padx=10, pady=10)

    def playagain():
        global result
        result=True
        wind.destroy()
    def bore():
        global result
        result=False
        wind.destroy()
  
    wind.mainloop()
    return result
