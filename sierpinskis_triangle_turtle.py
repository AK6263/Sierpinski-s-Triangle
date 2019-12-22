# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:32:39 2019

@author: Abhay Kshirsagar
"""
from turtle import *
from math import *
def find_leaf(t,xc,yc,l):
    # To find the coordinates of children nodes
    x_new = []
    y_new = []
    t.goto(xc,yc)
    k = l/sqrt(3)
    for i in range(3):
        t.forward(k)
        a,b = t.pos()
        x_new.append(round(a,3))
        y_new.append(round(b,3))
        t.back(k)
        t.rt(120)
    return x_new,y_new

def new_leaf(t,x,y,n,l):
    """Takes old leaves (parent nodes) x and y and finds
daughter leaves(children nodes) of the parents(i.e x and y)"""
    xnl = []
    ynl=[]
    q = 3**n
    for i in range(q):
        a , b = find_leaf(t,x[i],y[i],l)
        xnl.extend(a)
        ynl.extend(b)
    return xnl,ynl # New X and Y lists

def make_tree(t,x,y,l,lev):
    t.up()
    x_new = [0.0]
    y_new = [0.0]
    n=0
    while n < lev:
        l /= 2
        x.append(x_new)
        y.append(y_new)
        x_new,y_new = new_leaf(t,x_new,y_new,n,l)
        n+=1

def main(x,y,l,level):
    a = Turtle()
    a.speed(0)
    tracer(False)
    mode("logo")
    Screen().bgcolor('black')
    a.color('black')
    make_tree(a,x,y,l,level)
    triangles(a,x,y,length)
    
def triangles(t,x,y,l): # Drawing Triangles
    tracer(True);t.speed(0)
    t.goto(0,0)
    t.fd(l/sqrt(3))
    t.left(30)
    t.down()
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    for i in range(3):
        t.left(120)
        t.fd(l)
    t.end_fill()
    t.up()
    t.rt(30)
    t.back(l/sqrt(3))
    t.fillcolor("#000000")
    for i,j in zip(x,y):
        l *= 0.5
        for m,n in zip(i,j):
            l1 = l/sqrt(3)
            t.goto(m,n)
            t.rt(60)
            t.forward(l1)
            t.left(30)
            t.down()
            t.begin_fill()
            for j in range(3):
                t.left(120)
                t.forward(l)
            t.end_fill()
            t.up()
            t.rt(30)
            t.back(l1)
            t.left(60)

if __name__ == '__main__':
    x = []
    y = []
    length =int(input("Enter the length of the side of the sierpinski's triangle"))
    level=int(input("Enter the number of levels "))
    main(x,y,length,level)
    mainloop()

