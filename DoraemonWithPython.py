from turtle import *

import turtle

def myGoto(x,y):  #Defining goto() function 
    penup()
    goto(x,y)
    pendown()

def eyes():    #Funtion for the outline of the eyes
    fillcolor("#ffffff")
    begin_fill()
    
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60<=i <90:
            a = a-0.05
            left(3)
            forward(a)
        else:
            a = a+0.05
            left(3)
            forward(a)

    
    end_fill()
        
def hair():  #Total six hair
    
    myGoto(-32, 135)  #First
    seth(165)
    forward(60)
    
    myGoto(-32, 125)  #Second
    seth(180)
    forward(60)

    myGoto(-32, 105)  #Third
    seth(200)
    forward(60)
    
    myGoto(37, 135)  #Fourth
    seth(15)
    fd(60)
    
    myGoto(37, 115)  #Fifth
    seth(-13)
    forward(60)

    myGoto(37, 95)  #Sixth
    seth(-15)
    forward(60)
def mouth():  #Function for mouth
    myGoto(5, 148)
    seth(270)
    forward(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)

def neck():  #Function for neck
    fillcolor("#e70010")
    begin_fill()
    seth(0)
    forward(200)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    forward(207)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    end_fill()

def nose():  #Function for nose
    myGoto(-10, 158)
    seth(315)
    fillcolor("#e70010")
    begin_fill()
    circle(20)
    end_fill()

def eyeColor():  #Function for the color of the eyes
    seth(0)
    myGoto(-20, 195)
    fillcolor("#000000")
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    myGoto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    myGoto(-17, 200)
    seth(0)
    fillcolor("#ffffff")
    begin_fill()
    circle(5)
    end_fill()
    myGoto(0,0)
    
def face():
    forward(183)
    left(45)
    fillcolor("#ffffff")
    begin_fill()
    circle(120, 100)
    seth(180)
    forward(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()

    myGoto(63.56, 218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    forward(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    forward(64)
    
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor("#00a0de")
    begin_fill()
    circle(150, 280)
    end_fill()

#To create mountians

def mountain():
    myGoto(-300, 200)
    color("green")
    begin_fill()
    for i in range(3):
        
        forward(200)
        right(120)    
    end_fill()

    myGoto(-450, 200)
    color("green")
    begin_fill()
    for i in range(3):
        forward(200)
        right(120) 
    end_fill()

    myGoto(300, 200)
    color("green")
    begin_fill()
    for i in range(3):
        forward(200)
        right(120)    
    end_fill()

    myGoto(470, 200)
    color("grey")
    begin_fill()
    for i in range(3):
        forward(200)
        right(120)    
    end_fill()

    myGoto(640, 200)
    color("green")
    begin_fill()
    for i in range(3):
        forward(200)
        right(120)    
    end_fill()



    
def Doraemon():
    head()
    neck()
    face()
    nose()
    mouth()
    hair()
    eyeColor()
    
    
#Position of lower body
    
    myGoto(0,0)
    seth(0)
    penup()
    circle(150,50)
    pendown()
    seth(30)
    forward(40)
    seth(70)
    circle(-30, 270)

    fillcolor("#00a0de")
    begin_fill()
    seth(230)
    forward(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    seth(180)
    forward(70)
    seth(90)
    circle(30, 180)
    seth(180)
    forward(70)

    seth(100)    #Pocket of doraemon
    circle(-1000, 9)
    seth(-86)
    circle(1000, 2)
    seth(230)
    forward(40)

    circle(-30, 230)
    seth(45)
    forward(81)
    seth(0)
    forward(203)
    circle(5,90)
    forward(10)
    circle(5,90)
    forward(7)
    seth(40)
    circle(150, 10)
    seth(30)
    forward(40)
    end_fill()

    seth(70)
    fillcolor("#ffffff")
    begin_fill()
    circle(-30)
    end_fill()

    myGoto(103.74, -182.59)
    seth(0)
    fillcolor("#ffffff")
    begin_fill()
    forward(15)
    circle(-15, 180)
    forward(90)
    circle(-15, 180)
    forward(10)
    end_fill()

    myGoto(-96.26, -182.59)
    seth(180)
    fillcolor("#ffffff")
    begin_fill()
    forward(15)
    circle(15, 180)
    forward(90)
    circle(15,180)
    forward(10)
    end_fill()

    myGoto(-103.42, 15.09)
    seth(0)
    forward(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    myGoto(5, -40)
    seth(0)
    forward(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    forward(70)

    myGoto(-103.42, 15.09)
    forward(90)
    seth(70)
    fillcolor("#ffd200")
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor("#ffd200")
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()

    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    forward(15)
    dot(10)

    myGoto(0,150)
    
    mountain()

   
"""import random    
    
x = random.randint(0,255)
y = random.randint(0,255)
z = random.randint(0,255)"""


if __name__ == '__main__':
    screensize(500, 300)
    turtle.Screen().bgcolor("skyblue")   
    screen = Screen()
    screen.setup(width = 1.0, height = 1.0)
    pensize(3)
    speed(0)
    Doraemon()
    myGoto(100, -300)
    write ("Doraemon")
    mainloop()

    
    
    
