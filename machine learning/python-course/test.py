
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
import turtle as tk,sys
 
a=input("input your number of disc ")
a=int(a)
class Disc(tk.Turtle):
    def __init__(self, n):
        tk.Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/a, 0, 1-n/a)
        self.st()
        self.speed(0)
class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    tk.onkey(None,"space")
    tk.clear()
    try:
        hanoi(a, t1, t2, t3)
        tk.write("press STOP button to exit",
              align="center", font=("Courier", 16, "bold"))
    except tk.Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3
    tk.ht(); tk.penup(); tk.goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(a,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    tk.write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    tk.onkey(play, "space")
    tk.listen()
    tk.mainloop()
    tk.clear()
    tk.bye()
    return "EVENTLOOP"

if __name__=="__main__":
    main()
  
    
    

