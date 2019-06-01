#! /usr/bin/env python3

from tkinter import * 
import math
#Tk class is used to create a root window. 
fenetre = Tk()

value = StringVar()
plus = StringVar()
minus = StringVar()
entree = Entry(fenetre, textvariable=value, width=30)
calcul = Entry(fenetre, textvariable=plus, width=30)

def zero():
     entree.insert(END,"0")
def one():
    entree.insert(END,"1")
def two():
    entree.insert(END,"2")
def three():
    entree.insert(END,"3")
def four():
    entree.insert(END,"4")
def five():
    entree.insert(END,"5")
def six():
    entree.insert(END,"6")
def seven():
    entree.insert(END,"7")
def eight():
    entree.insert(END,"8")
def nine():
    entree.insert(END,"9")
def plus():
    find()
    entree.insert(END,"+")
def minus():
    find()
    entree.insert(END,"-")
def time():
    find()
    entree.insert(END,"*")
def divide():
    find()
    entree.insert(END,"/")
def equal():
    find()
def sinus():
    val = "sin("+value.get()+")"
    entree.delete(0, END)
    entree.insert(END,val)
    # valueL = value.get()
    # valueI = int(float(valueL))
    # res = math.sin(valueI)
    # entree.delete(0, END)
    # entree.insert(END,res)
def square():
    find()
    val = value.get()+"²"
    entree.delete(0, END)
    entree.insert(END,val)
def tang():
    valueL = value.get()
    valueI = int(float(valueL))
    res = math.tan(valueI)
    entree.delete(0, END)
    entree.insert(END,res)
def cos():
    valueL = value.get()
    valueI = int(float(valueL))
    res = math.cos(valueI)
    entree.delete(0, END)
    entree.insert(END,res)
def delete():
    entree.delete(0, END)
def modulo():
    find()
    entree.insert(END,"%")
def find():
    v = value.get()
    omu = v.find("*")
    op = v.find("+")
    om = v.find("-")
    od = v.find("/")
    sqr = v.find("²")
    mod = v.find("%")
    if sqr != -1:
        tab = v.split("²")
        nb1 = int(tab[0])
        # nb2 = int(tab[1])
        res = nb1 * nb1
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres)
    elif omu != -1:
        tab = v.split("*")
        nb1 = int(tab[0])
        nb2 = int(tab[1])
        res = nb1 * nb2
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres)
    elif op != -1:
        tab = v.split("+")
        nb1 = int(tab[0])
        nb2 = int(tab[1])
        res = nb1 + nb2
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres)  
    elif om != -1:
        tab = v.split("-")
        nb1 = int(tab[0])
        nb2 = int(tab[1])
        res = nb1 - nb2
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres) 
    elif od != -1:
        tab = v.split("/")
        nb1 = int(tab[0])
        nb2 = int(tab[1])
        res = nb1 / nb2
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres) 
    elif mod != -1:
        tab = v.split("%")
        nb1 = int(tab[0])
        nb2 = int(tab[1])
        res = nb1 % nb2
        strres = str(res)
        calcul.delete(0, END)
        calcul.insert(0, res)
        entree.delete(0, END)
        entree.insert(0, strres)
entree.grid(row=0, columnspan=7, sticky=W+E+N+S)
Button(fenetre, text='Rad', borderwidth=1).grid(row=1, column=1, sticky=W+E+N+S)
Button(fenetre, text='...', borderwidth=1).grid(row=1, column=2, sticky=W+E+N+S)
Button(fenetre, text='x!', borderwidth=1).grid(row=1, column=3, sticky=W+E+N+S)
Button(fenetre, text='(', borderwidth=1).grid(row=1, column=4, sticky=W+E+N+S)
Button(fenetre, text=')', borderwidth=1).grid(row=1, column=5, sticky=W+E+N+S)
Button(fenetre, text='%', borderwidth=1, command=modulo).grid(row=1, column=6, sticky=W+E+N+S)
Button(fenetre, text='AC', borderwidth=1, fg="red", command=delete).grid(row=1, column=7, sticky=W+E+N+S)

Button(fenetre, text='Inv', borderwidth=1).grid(row=2, column=1, sticky=W+E+N+S)
Button(fenetre, text='sin', borderwidth=1, command=sinus).grid(row=2, column=2, sticky=W+E+N+S)
Button(fenetre, text='ln', borderwidth=1).grid(row=2, column=3, sticky=W+E+N+S)
Button(fenetre, text='7', borderwidth=1, fg="green", command=seven).grid(row=2, column=4, sticky=W+E+N+S) 
Button(fenetre, text='8', borderwidth=1, fg="green", command=eight).grid(row=2, column=5, sticky=W+E+N+S) 
Button(fenetre, text='9', borderwidth=1, fg="green", command=nine).grid(row=2, column=6, sticky=W+E+N+S) 
Button(fenetre, text='/', borderwidth=1, command=divide).grid(row=2, column=7, sticky=W+E+N+S) 

Button(fenetre, text='pi', borderwidth=1).grid(row=3, column=1, sticky=W+E+N+S) 
Button(fenetre, text='cos', borderwidth=1).grid(row=3, column=2, sticky=W+E+N+S) 
Button(fenetre, text='log', borderwidth=1).grid(row=3, column=3, sticky=W+E+N+S) 
Button(fenetre, text='4', borderwidth=1, fg="green", command=four).grid(row=3, column=4, sticky=W+E+N+S)
Button(fenetre, text='5', borderwidth=1, fg="green", command=five).grid(row=3, column=5, sticky=W+E+N+S) 
Button(fenetre, text='6', borderwidth=1, fg="green", command=six).grid(row=3, column=6, sticky=W+E+N+S) 
Button(fenetre, text='*', borderwidth=1, command=time).grid(row=3, column=7, sticky=W+E+N+S) 

Button(fenetre, text='e', borderwidth=1).grid(row=4, column=1, sticky=W+E+N+S) 
Button(fenetre, text='tan', borderwidth=1).grid(row=4, column=2, sticky=W+E+N+S) 
Button(fenetre, text='sqr', borderwidth=1).grid(row=4, column=3, sticky=W+E+N+S) 
Button(fenetre, text='1', borderwidth=1, fg="green", command=one).grid(row=4, column=4, sticky=W+E+N+S) 
Button(fenetre, text='2', borderwidth=1, fg="green", command=two).grid(row=4, column=5, sticky=W+E+N+S) 
Button(fenetre, text='3', borderwidth=1, fg="green", command=three).grid(row=4, column=6, sticky=W+E+N+S) 
Button(fenetre, text='-', borderwidth=1, command=minus).grid(row=4, column=7, sticky=W+E+N+S) 

Button(fenetre, text='Ans', borderwidth=1).grid(row=5, column=1, sticky=W+E+N+S) 
# Button(fenetre, text='EXP', borderwidth=1, command=EXP).grid(row=5, column=2, sticky=W+E+N+S) 
Button(fenetre, text='²', borderwidth=1, command=square).grid(row=5, column=3, sticky=W+E+N+S)
Button(fenetre, text='0', borderwidth=1, fg="green", command=zero).grid(row=5, column=4, sticky=W+E+N+S)
Button(fenetre, text='.', borderwidth=1).grid(row=5, column=5, sticky=W+E+N+S)
Button(fenetre, text='=', borderwidth=1, command=equal).grid(row=5, column=6, sticky=W+E+N+S) 
Button(fenetre, text='+', borderwidth=1, command=plus).grid(row=5, column=7, sticky=W+E+N+S) 

fenetre.mainloop()