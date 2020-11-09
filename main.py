from tkinter import *
import random
import time
import datetime
import tkinter.messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg="Cadet Blue", bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 60, 'bold'), text="Restaurant Management System", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)


ReceiptCal_F = Frame(root, bg="Powder Blue", bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)


MenuFrame = Frame(root, bg="Cadet Blue", bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame, bg="Cadet Blue", bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg="Cadet Blue", bd=10)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame, bg="Cadet Blue", bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(MenuFrame, bg="Cadet Blue", bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()



Latta = Checkbutton(Drinks_F, text="Latta", variable = var1, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 0, sticky = W)
Espresso = Checkbutton(Drinks_F, text="Espresso", variable = var2, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 1, sticky = W)
Iced_Latta = Checkbutton(Drinks_F, text="Iced Latta", variable = var3, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 2, sticky = W)
Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable = var4, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 3, sticky = W)
Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable = var5, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 4, sticky = W)
African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable = var6, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 5, sticky = W)
American_coffee = Checkbutton(Drinks_F, text="American coffee", variable = var7, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 6, sticky = W)
Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable = var8, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 7, sticky = W)

root.mainloop()

