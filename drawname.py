from graphics import *
scrn = GraphWin("My Name", 300,100)
def N():
    l1 = Line(Point(5,5),Point(5,50))
    l2 = Line(Point(5,5),Point(50,50))
    l3 = Line(Point(50,5),Point(50,50))
    l1.draw(scrn)
    l2.draw(scrn)
    l3.draw(scrn)
def A():
    l4 = Line(Point(60,50),Point(85,5))
    l5 = Line(Point(70,30),Point(100,30))
    l6 = Line(Point(110,50),Point(85,5))
    l4.draw(scrn)
    l5.draw(scrn)
    l6.draw(scrn)
def T():
    l7 = Line(Point(110,5),Point(160,5))
    l8 = Line(Point(135,5),Point(135,50))
    l7.draw(scrn)
    l8.draw(scrn)
def E():
    l9 = Line(Point(170,5),Point(170,50))
    l11 = Line(Point(170,50),Point(200,50))
    l12 = Line(Point(170,30),Point(190,30))
    l10 = Line(Point(170,5),Point(200,5))
    l9.draw(scrn)
    l10.draw(scrn)
    l11.draw(scrn)
    l12.draw(scrn)
N()
A()
T()
E()
scrn.getMouse()
scrn.close()
