#! /usr/bin/env python3

from tkinter import * 

fenetre = Tk()

# label = Label(fenetre, text="Hello World")
# label.pack()
# # bouton de sortie
# bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
# bouton.pack()
def recupere():
    showinfo("Alerte", entree.get())

value = StringVar()
entree = Entry(fenetre, textvariable=value.get(), width=30)

 # 
# bouton = Button(fenetre, text="Valider", command=recupere)
# bouton.pack()

entree.grid(row=0, columnspan=7, sticky=W+E+N+S)
Button(fenetre, text='Rad', borderwidth=1).grid(row=1, column=1, sticky=W+E+N+S)
Button(fenetre, text='...', borderwidth=1).grid(row=1, column=2, sticky=W+E+N+S)
Button(fenetre, text='x!', borderwidth=1).grid(row=1, column=3, sticky=W+E+N+S)
Button(fenetre, text='(', borderwidth=1).grid(row=1, column=4, sticky=W+E+N+S)
Button(fenetre, text=')', borderwidth=1).grid(row=1, column=5, sticky=W+E+N+S)
Button(fenetre, text='%', borderwidth=1).grid(row=1, column=6, sticky=W+E+N+S)
Button(fenetre, text='AC', borderwidth=1, fg="red").grid(row=1, column=7, sticky=W+E+N+S)

Button(fenetre, text='Inv', borderwidth=1).grid(row=2, column=1, sticky=W+E+N+S)
Button(fenetre, text='sin', borderwidth=1).grid(row=2, column=2, sticky=W+E+N+S)
Button(fenetre, text='ln', borderwidth=1).grid(row=2, column=3, sticky=W+E+N+S)
Button(fenetre, text='7', borderwidth=1, fg="green", command=value.add("7")).grid(row=2, column=4, sticky=W+E+N+S) 
Button(fenetre, text='8', borderwidth=1, fg="green").grid(row=2, column=5, sticky=W+E+N+S) 
Button(fenetre, text='9', borderwidth=1, fg="green").grid(row=2, column=6, sticky=W+E+N+S) 
Button(fenetre, text='/', borderwidth=1).grid(row=2, column=7, sticky=W+E+N+S) 

Button(fenetre, text='pi', borderwidth=1).grid(row=3, column=1, sticky=W+E+N+S) 
Button(fenetre, text='cos', borderwidth=1).grid(row=3, column=2, sticky=W+E+N+S) 
Button(fenetre, text='log', borderwidth=1).grid(row=3, column=3, sticky=W+E+N+S) 
Button(fenetre, text='4', borderwidth=1, fg="green").grid(row=3, column=4, sticky=W+E+N+S)
Button(fenetre, text='5', borderwidth=1, fg="green").grid(row=3, column=5, sticky=W+E+N+S) 
Button(fenetre, text='6', borderwidth=1, fg="green").grid(row=3, column=6, sticky=W+E+N+S) 
Button(fenetre, text='x', borderwidth=1).grid(row=3, column=7, sticky=W+E+N+S) 

Button(fenetre, text='e', borderwidth=1).grid(row=4, column=1, sticky=W+E+N+S) 
Button(fenetre, text='tan', borderwidth=1).grid(row=4, column=2, sticky=W+E+N+S) 
Button(fenetre, text='racine', borderwidth=1).grid(row=4, column=3, sticky=W+E+N+S) 
Button(fenetre, text='1', borderwidth=1, fg="green").grid(row=4, column=4, sticky=W+E+N+S) 
Button(fenetre, text='2', borderwidth=1, fg="green").grid(row=4, column=5, sticky=W+E+N+S) 
Button(fenetre, text='3', borderwidth=1, fg="green").grid(row=4, column=6, sticky=W+E+N+S) 
Button(fenetre, text='-', borderwidth=1).grid(row=4, column=7, sticky=W+E+N+S) 

Button(fenetre, text='Ans', borderwidth=1).grid(row=5, column=1, sticky=W+E+N+S) 
Button(fenetre, text='EXP', borderwidth=1).grid(row=5, column=2, sticky=W+E+N+S) 
Button(fenetre, text='Xy', borderwidth=1).grid(row=5, column=3, sticky=W+E+N+S)
Button(fenetre, text='0', borderwidth=1, fg="green").grid(row=5, column=4, sticky=W+E+N+S)
Button(fenetre, text='.', borderwidth=1).grid(row=5, column=5, sticky=W+E+N+S)
Button(fenetre, text='=', borderwidth=1).grid(row=5, column=6, sticky=W+E+N+S) 
Button(fenetre, text='+', borderwidth=1).grid(row=5, column=7, sticky=W+E+N+S) 

fenetre.mainloop()