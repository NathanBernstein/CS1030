'''
Nate Bernstein
Graphics
Feb 28
CS1030
'''

from graphics import *
import time
scrn = GraphWin("AnimatedEmoji", 500,500)
x = 10
y = 10
def outline():
    r1 = Rectangle(Point(x,y+50),Point(x+10,y+100))
    r2 = Rectangle(Point(x+10,y+30),Point(x+20,y+50))
    r3 = Rectangle(Point(x+20,y+20),Point(x+30,y+30))
    r4 = Rectangle(Point(x+30,y+10),Point(x+50,y+20))
    r5 = Rectangle(Point(x+140,y+50),Point(x+150,y+100))
    r6 = Rectangle(Point(x+130,y+30),Point(x+140,y+50))
    r7 = Rectangle(Point(x+120,y+20),Point(x+130,y+30))
    r8 = Rectangle(Point(x+100,y+10),Point(x+120,y+20))
    r9 = Rectangle(Point(x+50,y),Point(x+100,y+10))
    r10 = Rectangle(Point(x+50,y+140),Point(x+100,y+150))
    r11 = Rectangle(Point(x+10,y+100),Point(x+20,y+120))
    r12 = Rectangle(Point(x+20,y+120),Point(x+30,y+130))
    r13 = Rectangle(Point(x+30,y+130),Point(x+50,y+140))
    r14 = Rectangle(Point(x+100,y+130),Point(x+120,y+140))
    r15 = Rectangle(Point(x+120,y+120),Point(x+130,y+130))
    r16 = Rectangle(Point(x+130,y+100),Point(x+140,y+120))
    r1.draw(scrn)
    r2.draw(scrn)
    r3.draw(scrn)
    r4.draw(scrn)
    r5.draw(scrn)
    r6.draw(scrn)
    r7.draw(scrn)
    r8.draw(scrn)
    r9.draw(scrn)
    r10.draw(scrn)
    r11.draw(scrn)
    r12.draw(scrn)
    r13.draw(scrn)
    r14.draw(scrn)
    r15.draw(scrn)
    r16.draw(scrn)
    r1.setFill("Black")
    r2.setFill("Black")
    r3.setFill("Black")
    r4.setFill("Black")
    r5.setFill("Black")
    r6.setFill("Black")
    r7.setFill("Black")
    r8.setFill("Black")
    r9.setFill("Black")
    r10.setFill("Black")
    r11.setFill("Black")
    r12.setFill("Black")
    r13.setFill("Black")
    r14.setFill("Black")
    r15.setFill("Black")
    r16.setFill("Black")

def glasses():
    r17 = Rectangle(Point(x+20,y+40),Point(x+130,y+60))
    r18 = Rectangle(Point(x+20,y+60),Point(x+70,y+70))
    r19 = Rectangle(Point(x+80,y+60),Point(x+130,y+70))
    r20 = Rectangle(Point(x+30,y+70),Point(x+60,y+80))
    r21 = Rectangle(Point(x+90,y+70),Point(x+120,y+80))
    r17.draw(scrn)
    r18.draw(scrn)
    r19.draw(scrn)
    r20.draw(scrn)
    r21.draw(scrn)
    r17.setFill("Black")
    r18.setFill("Black")
    r19.setFill("Black")
    r20.setFill("Black")
    r21.setFill("Black")

def eyes():
    a = 0
    b = 0
    r22 = Rectangle(Point(a+x+40,b+y+50),Point(a+x+60,b+y+60))
    r23 = Rectangle(Point(a+x+50,b+y+50),Point(a+x+60,b+y+60))
    r24 = Rectangle(Point(a+x+50,b+y+60),Point(a+x+60,b+y+70))
    r25 = Rectangle(Point(a+x+100,b+y+50),Point(a+x+120,b+y+60))
    r26 = Rectangle(Point(a+x+110,b+y+50),Point(a+x+120,b+y+60))
    r27 = Rectangle(Point(a+x+110,b+y+60),Point(a+x+120,b+y+70))
    r32 = Rectangle(Point(a+x+40,b+y+100),Point(a+x+50,b+y+110))
    r33 = Rectangle(Point(a+x+50,b+y+110),Point(a+x+90,b+y+120))
    r32.draw(scrn)
    r33.draw(scrn)
    r32.setFill("Black")
    r33.setFill("Black")
    r22.draw(scrn)
    r23.draw(scrn)
    r24.draw(scrn)
    r25.draw(scrn)
    r26.draw(scrn)
    r27.draw(scrn)
    r22.setFill("White")
    r23.setFill("White")
    r24.setFill("White")
    r25.setFill("White")
    r26.setFill("White")
    r27.setFill("White")
    time.sleep(.75)
    r24.undraw()
    time.sleep(.1)
    r23.undraw()
    r22.undraw()
    time.sleep(.8)
    r22.draw(scrn)
    r23.draw(scrn)
    r24.draw(scrn)
    r32.undraw()
    r33.undraw()
    time.sleep(1)

def mouth():
    c=0
    while (c < 7):
        a = 0
        b = 0
        r28 = Rectangle(Point(a+x+40,b+y+100),Point(a+x+50,b+y+110))
        r29 = Rectangle(Point(a+x+50,b+y+110),Point(a+x+90,b+y+120))
        r28.draw(scrn)
        r29.draw(scrn)
        r28.setFill("Black")
        r29.setFill("Black")
        time.sleep(.5)
        r28.undraw()
        r29.undraw()
        a+=10
        r30 = Rectangle(Point(a+x+40,b+y+100),Point(a+x+50,b+y+110))
        r31 = Rectangle(Point(a+x+50,b+y+110),Point(a+x+90,b+y+120))
        r30.draw(scrn)
        r31.draw(scrn)
        r30.setFill("Black")
        r31.setFill("Black")
        time.sleep(.5)
        r30.undraw()
        r31.undraw()
        c+=1
    r28.draw(scrn)
    r29.draw(scrn)
def colorCircle():
    i = 0
    while (i<75):
        c1 = Circle(Point(75+x,75+y),i)
        c1.draw(scrn)
        c1.setFill("Light Blue")
        i+=1
        time.sleep(.05)

colorCircle()
outline()
glasses()
eyes()
mouth()


scrn.getMouse()
scrn.close()
