#coding:utf-8

from tkinter import *


calculatrice = Tk()
calculatrice.minsize(400,200)

calcul_list = []


# Fonction liée à la saisie de chiffre
def fctBT1():
    affichage.insert(END,"1")
    aff_gal.insert(END,"1")
def fctBT2():
    affichage.insert(END,"2")
    aff_gal.insert(END,"2")
def fctBT3():
    affichage.insert(END,"3")
    aff_gal.insert(END,"3")

def fctBT4():
    affichage.insert(END,"4")
    aff_gal.insert(END,"4")

def fctBT5():
    affichage.insert(END,"5")
    aff_gal.insert(END,"5")

def fctBT6():
    affichage.insert(END,"6")
    aff_gal.insert(END,"6")

def fctBT7():
    affichage.insert(END,"7")
    aff_gal.insert(END,"7")

def fctBT8():
    affichage.insert(END,"8")
    aff_gal.insert(END,"8")

def fctBT9():
    affichage.insert(END,"9")
    aff_gal.insert(END,"9")

def fctBT0():
    affichage.insert(END,"0")
    aff_gal.insert(END,"0")

def fctBTpt():
    affichage.insert(END,".")
    aff_gal.insert(END,".")


# Fonction liée à la saisie clavier
def fctK1(event):
    affichage.insert(END,"1")
    aff_gal.insert(END,"1")
def fctK2(event):
    affichage.insert(END,"2")
    aff_gal.insert(END,"2")
def fctK3(event):
    affichage.insert(END,"3")
    aff_gal.insert(END,"3")

def fctK4(event):
    affichage.insert(END,"4")
    aff_gal.insert(END,"4")

def fctK5(event):
    affichage.insert(END,"5")
    aff_gal.insert(END,"5")

def fctK6(event):
    affichage.insert(END,"6")
    aff_gal.insert(END,"6")

def fctK7(event):
    affichage.insert(END,"7")
    aff_gal.insert(END,"7")

def fctK8(event):
    affichage.insert(END,"8")
    aff_gal.insert(END,"8")

def fctK9(event):
    affichage.insert(END,"9")
    aff_gal.insert(END,"9")

def fctK0(event):
    affichage.insert(END,"0")
    aff_gal.insert(END,"0")

def fctKpt(event):
    affichage.insert(END,".")
    aff_gal.insert(END,".")

# Fonction liée à la saisie du type d'opération
def fctBTadd():
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"+")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"+")
def fctBTsub():
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"-")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"-")
def fctBTmult():
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"*")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"*")
def fctBTdiv():
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"/")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"/")

# Fonction liée au clavier pour les opérations

def fctKadd(event):
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"+")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"+")
def fctKsub(event):
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"-")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"-")
def fctKmult(event):
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"*")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"*")
def fctKdiv(event):
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    affichage.insert(END,"/")
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    aff_gal.insert(END,"/")

# Fonction lié à la validation du calcul
def calcul():
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    if calcul_list[1]=="+\n":
        resultat.set(float(calcul_list[0][0:-1])+float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="-\n":
        resultat.set(float(calcul_list[0][0:-1])-float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="*\n":
        resultat.set(float(calcul_list[0][0:-1])*float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="/\n":
        resultat.set(float(calcul_list[0][0:-1])/float(calcul_list[2][0:-1]))

def fctKEnter(event):
    calcul_list.append(affichage.get(0.0,END))
    affichage.delete(0.0,END)
    if calcul_list[1]=="+\n":
        resultat.set(float(calcul_list[0][0:-1])+float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="-\n":
        resultat.set(float(calcul_list[0][0:-1])-float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="*\n":
        resultat.set(float(calcul_list[0][0:-1])*float(calcul_list[2][0:-1]))
    elif calcul_list[1]=="/\n":
        resultat.set(float(calcul_list[0][0:-1])/float(calcul_list[2][0:-1]))

# Fonction réinitialiser
def cancel():
    calcul_list.clear()
    affichage.delete(0.0, END)
    resultat.set("")
    aff_gal.delete(0.0,END)

# Fonction réinitialiser au clavier
def fctKc(event):
    calcul_list.clear()
    affichage.delete(0.0, END)
    resultat.set("")
    aff_gal.delete(0.0,END)


# Affichage saisie
affichage = Text(calculatrice, width = 24, height=1)
affichage.grid(row=0,column=0, columnspan=2, padx=10, pady=10)

# Affichage globale de la saisie
aff_gal = Text(calculatrice, width = 24, height=1)
aff_gal.grid(row=5,column=0, columnspan=2, padx=10, pady=10)

# Saisie de chiffre
BT1 = Button(calculatrice, text="1", width=8, command=fctBT1)
BT1.grid(row=1, column=0, padx=10, pady=10)
calculatrice.bind("<Key-1>", fctK1)

BT2 = Button(calculatrice, text="2", width=8, command=fctBT2)
BT2.grid(row=1, column=1, padx=10, pady=10)
calculatrice.bind("<Key-2>", fctK2)

BT3 = Button(calculatrice, text="3", width=8, command=fctBT3)
BT3.grid(row=1, column=2, padx=10, pady=10)
calculatrice.bind("<Key-3>", fctK3)

BT4 = Button(calculatrice, text="4", width=8, command=fctBT4)
BT4.grid(row=2, column=0, padx=10, pady=10)
calculatrice.bind("<Key-4>", fctK4)

BT5 = Button(calculatrice, text="5", width=8, command=fctBT5)
BT5.grid(row=2, column=1, padx=10, pady=10)
calculatrice.bind("<Key-5>", fctK5)

BT6 = Button(calculatrice, text="6", width=8, command=fctBT6)
BT6.grid(row=2, column=2, padx=10, pady=10)
calculatrice.bind("<Key-6>", fctK6)

BT7 = Button(calculatrice, text="7", width=8, command=fctBT7)
BT7.grid(row=3, column=0, padx=10, pady=10)
calculatrice.bind("<Key-7>", fctK7)

BT8 = Button(calculatrice, text="8", width=8, command=fctBT8)
BT8.grid(row=3, column=1, padx=10, pady=10)
calculatrice.bind("<Key-8>", fctK8)

BT9 = Button(calculatrice, text="9", width=8, command=fctBT9)
BT9.grid(row=3, column=2, padx=10, pady=10)
calculatrice.bind("<Key-9>", fctK9)

BT0 = Button(calculatrice, text="0", width=8, command=fctBT0)
BT0.grid(row=4, column=0, padx=10, pady=10)
calculatrice.bind("<Key-0>", fctK0)

BTpt = Button(calculatrice, text=".", width=8, command=fctBTpt)
BTpt.grid(row=4, column=1, padx=10, pady=10)
calculatrice.bind("<Key-.>", fctKpt)


# Saisie d'opération
BTadd = Button(calculatrice, text="+", width=8, command=fctBTadd)
BTadd.grid(row=1, column=4, padx=10, pady=10)
calculatrice.bind("<Key-+>", fctKadd)

BTsub = Button(calculatrice, text="-", width=8, command=fctBTsub)
BTsub.grid(row=2, column=4, padx=10, pady=10)
calculatrice.bind("<Key-->", fctKsub)

BTmult = Button(calculatrice, text="*", width=8, command=fctBTmult)
BTmult.grid(row=3, column=4, padx=10, pady=10)
calculatrice.bind("<Key-*>", fctKmult)

BTdiv = Button(calculatrice, text="/", width=8, command=fctBTdiv)
BTdiv.grid(row=4, column=4, padx=10, pady=10)
calculatrice.bind("<Key-/>", fctKdiv)

# Valider le calcul
BTequal = Button(calculatrice, text=("="), width=8, command=calcul)
BTequal.grid(row=4, column=2, padx=10, pady=10)
calculatrice.bind("<Key-Return>", fctKEnter)


# Afficher le résultat
lb_equal = Label(calculatrice, text="=")
lb_equal.grid(row=0, column=3)
resultat = StringVar()
aff_resultat = Entry(calculatrice, textvariable=resultat)
aff_resultat.grid(row=0, column=4, padx=10, pady=10)

# Bouton réinitialiser
BTcancel = Button(calculatrice, text="C", bg="red" ,command=cancel)
BTcancel.grid(row=0, column=2)
calculatrice.bind("<Key-c>", fctKc)

calculatrice.mainloop()