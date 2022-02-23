from graphics import *
import time
def DrawCircle():
    windw = GraphWin("A Circle", 500,500)
    windw.setBackground("midnight blue")
    x = 500
    y = 250
    while x>0:
        p = Point(x,y)
        c = Circle(p,x)
        c.draw(windw)
        x-=5
        c.setFill("light blue")
        '''time.sleep(.05)
        c.undraw()'''
    windw.getMouse()
    windw.close()

DrawCircle()
