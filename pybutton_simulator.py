import time

upgrade = 2

playerscore = 0

upgrade2 = 0

# def add_upgrade_sps(amount):
# global playerscore
# if playerscore > 149:
# global upgrade2
# upgrade2 += amount
# playerscore -= 150
# else:
# print("Not enough score")


def add_upgrade(amount):
    global playerscore
    if playerscore > 49:
        global upgrade
        upgrade += amount
        playerscore -= 50
    else:
        print("Not enough score")


def add_upgrade2(amount):
    global playerscore
    if playerscore > 149:
        global upgrade
        upgrade += amount
        playerscore -= 150
    else:
        print("Not enough score")


def add_upgrade3(amount):
    global playerscore
    if playerscore > 499:
        global upgrade
        upgrade += amount
        playerscore -= 500
    else:
        print("Not enough score")


def add_upgrade4(amount):
    global playerscore
    if playerscore > 1499:
        global upgrade
        upgrade += amount
        playerscore -= 1500
    else:
        print("Not enough score")


def add_score(score):
    global playerscore
    playerscore += score
    print(playerscore)


def add_sps(amount):
    global playerscore
    global upgrade2
    global upgrade
    time.sleep(1)
    add_score(upgrade)


from tkinter import *

tk = Tk()
btn = Button(tk, text="click me", command=lambda: add_score(upgrade))
btn.pack()

btn2 = Button(
    tk,
    text="Buy upgrade 1 costs 50, gives plus 2 score per click",
    command=lambda: add_upgrade(1),
)
btn2.pack()

btn3 = Button(
    tk,
    text="Buy upgrade 2 costs 150, gives plus 10 score per click",
    command=lambda: add_upgrade2(5),
)
btn3.pack()

btn4 = Button(
    tk,
    text="Buy upgrade 3 costs 500, gives plus 20 score per click",
    command=lambda: add_upgrade3(20),
)
btn4.pack()

btn5 = Button(
    tk,
    text="Buy upgrade 4 costs 1500, gives plus 50 score per click",
    command=lambda: add_upgrade4(50),
)
btn5.pack()

tk.mainloop()

# while True:
# add_sps(upgrade2)

from turtle import *

t = Pen()
