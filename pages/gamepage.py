import tkinter as tk
from tkinter import ttk
from random import choice

LARGEFONT = ("Verdana", 35)
FONT = ("Verdana", 15)

def gamePage():
    wind=tk.Tk()
    wind.title("GAME")
    label_player = ttk.Label(wind, text="", font=FONT)
    label_player.grid(row=0, column=2)
    label_computer = ttk.Label(wind, text="COMPUTER", font=FONT)
    label_computer.grid(row=0, column=6)
    name=readName()
    label_player.configure(text=name)

    click_rock = ttk.Button(wind, text="ROCK", command=lambda: update_choice("rock"))
    click_paper = ttk.Button(wind, text="PAPER", command=lambda: update_choice("paper"))
    click_scissor = ttk.Button(wind, text="SCISSOR", command=lambda: update_choice("scissor"))
    click_lizard = ttk.Button(wind, text="LIZARD", command=lambda: update_choice("lizard"))
    click_spock = ttk.Button(wind, text="SPOCK", command=lambda: update_choice("spock"))

    click_rock.grid(row=1, column=1)
    click_paper.grid(row=3, column=1)
    click_scissor.grid(row=5, column=1)
    click_lizard.grid(row=7, column=1)
    click_spock.grid(row=9, column=1)

    click_rock1 = ttk.Button(wind, text="ROCK")
    click_paper1 = ttk.Button(wind, text="PAPER")
    click_scissor1 = ttk.Button(wind, text="SCISSOR")
    click_lizard1 = ttk.Button(wind, text="LIZARD")
    click_spock1 = ttk.Button(wind, text="SPOCK")

    click_rock1.grid(row=1, column=8)
    click_paper1.grid(row=3, column=8)
    click_scissor1.grid(row=5, column=8)
    click_lizard1.grid(row=7, column=8)
    click_spock1.grid(row=9, column=8)

    img_player = ttk.Label(wind, text="Player", font=FONT)
    img_comp = ttk.Label(wind, text="Computer", font=FONT)

    img_player.grid(row=5, column=2)
    img_comp.grid(row=5, column=6)

    label_sc = ttk.Label(wind, text="PLAYER SCORE:")
    label_sc.grid(row=11, column=1)
    label_CO = ttk.Label(wind, text="COMPUTER SCORE:")
    label_CO.grid(row=11, column=5)

    score_comp = ttk.Label(wind, text=0, font=FONT)
    score_player = ttk.Label(wind, text=0, font=FONT)

    score_comp.grid(row=11, column=6)
    score_player.grid(row=11, column=2)

    msg = ttk.Label(wind, font=FONT)
    msg.grid(row=14, column=4)

    def update_one(y):
        img_comp['text'] = y

    def update_two(x):
        img_player['text'] = x

    def update_msg(a):
        msg.configure(text=a)

    def update_Cscore():
        final = int(score_comp['text'])
        final += 1
        score_comp["text"] = str(final)
        if final == 3:
            f=open("winner.txt","w")
            f.write("Computer Win!")
            f.close()
            nextW()


    def update_Pscore():
        final = int(score_player['text'])
        final += 1
        score_player["text"] = str(final)
        if final == 3:
            f=open("winner.txt","w")
            f.write("Player Win!")
            f.close()
            nextW()

    def nextW():
        f=open("score.txt","w")
        f.write(score_player["text"])
        f.close()
        score_comp["text"] = 0
        score_player["text"] = 0
        wind.destroy()
        

    def winner(p, c):
        if p == c:
            update_msg("This round is drawn")
        elif p == "rock":
            if c == "paper":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            elif c == "scissor":
                update_msg("Player wins this round!!!")
                update_Pscore()
            elif c == "lizard":
                update_msg("Player wins this round!!!")
                update_Pscore()
            else:
                update_msg("Computer wins this round!!!")
                update_Cscore()

        elif p == "paper":
            if c == "scissor":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            elif c == "rock":
                update_msg("Player wins this round!!!")
                update_Pscore()
            elif c == "lizard":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            else:
                update_msg("Player wins this round!!!")
                update_Pscore()

        elif p == "scissor":
            if c == "rock":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            elif c == "paper":
                update_msg("Player wins this round!!!")
                update_Pscore()
            elif c == "lizard":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            else:
                update_msg("Player wins this round!!!")
                update_Pscore()

        elif p == "lizard":
            if c == "rock":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            elif c == "paper":
                update_msg("Player wins this round!!!")
                update_Pscore()
            elif c == "scissor":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            else:
                update_msg("Player wins this round!!!")
                update_Pscore()

        elif p == "spock":
            if c == "rock":
                update_msg("Player wins this round!!!")
                update_Pscore()
            if c == "paper":
                update_msg("Computer wins this round!!!")
                update_Cscore()
            if c == "scissor":
                update_msg("Player wins this round!!!")
                update_Pscore()
            else:
                update_msg("Computer wins this round!!!")
                update_Cscore()
        else:
            pass

    select = ["rock", "paper", "scissor", "lizard", "spock"]

    

    def update_choice(a):
        choice_comp = choice(select)
        if choice_comp == "rock":
            update_one("ROCK")
        elif choice_comp == "scissor":
            update_one("SCISSOR")
        elif choice_comp == "paper":
            update_one("PAPER")
        elif choice_comp == "lizard":
            update_one("LIZARD")
        else:
            update_one("SPOCK")

        if a == "rock":
            update_two("ROCK")
        elif a == "scissor":
            update_two("SCISSOR")
        elif a == "paper":
            update_two("PAPER")
        elif a == "lizard":
            update_two("LIZARD")
        else:
            update_two("SPOCK")

        winner(a, choice_comp)

    wind.mainloop()
    return

def readName():
    name=""
    f=open("name.txt","r")
    name=f.read()
    f.close()
    return name
