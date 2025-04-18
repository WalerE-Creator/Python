from tkinter import *

tk = Tk()

import turtle

screen = turtle.Screen()
t = turtle.Turtle()
s = screen

door_opened = False

pendown = True


def on_c():
    screen_clear()


def on_a():
    t.left(5)


def on_d():
    t.right(5)


def on_w():
    t.forward(10)


def on_s():
    t.back(10)


def penup():
    global pendown
    if pendown == True:
        t.penup()
        pendown = False
    else:
        t.pendown()
        pendown = True


def main():
    s.onkey(on_c, 'c')
    s.onkey(on_a, 'a')
    s.onkey(on_d, 'd')
    s.onkey(on_w, 'w')
    s.onkey(on_s, 's')
    s.onkey(penup, 'p')
    s.listen()
    s.mainloop()


def screen_clear():
    t.clear()


print("Press c to clear the screen.")
print("Press p to put the pen up or down.")

btn1 = Button(tk, text=("Clear screen"), command=lambda: screen_clear())
btn1.pack()

btn2 = Button(tk, text=("Pen up/down"), command=lambda: penup())
btn2.pack()

if __name__ == "__main__":
    main()
