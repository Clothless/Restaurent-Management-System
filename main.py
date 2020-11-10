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

Drinks_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)


#=============================Variables==========================================================================================================================================================

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


DateOfOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostOfCakes = StringVar()
CostOfDrinks = StringVar()
ServiceCharge = StringVar()

text_input = StringVar()
operator = ""


E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_West_African_Cake = StringVar()
E_Tarte = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Cake = StringVar()
E_Queen_Park_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_School_Cake = StringVar()


E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

E_West_African_Cake.set("0")
E_Tarte.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Cake.set("0")
E_Queen_Park_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_School_Cake.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#===============================Functions============================================================================================================================================================

def iExit():
	iExit = tkinter.messagebox.askyesno("Exit System?", "Are You Sure You Want To Exit?")
	if iExit > 0:
		root.destroy()
		return


def Reset():
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostOfCakes.set("")
	CostOfDrinks.set("")
	ServiceCharge.set("")
	txt_Receipt.delete("1.0",END)
	E_Latta.set("0")
	E_Espresso.set("0")
	E_Iced_Latta.set("0")
	E_Vale_Coffee.set("0")
	E_Cappuccino.set("0")
	E_African_Coffee.set("0")
	E_American_Coffee.set("0")
	E_Iced_Cappuccino.set("0")
	E_West_African_Cake.set("0")
	E_Tarte.set("0")
	E_Lagos_Chocolate_Cake.set("0")
	E_Kilburn_Chocolate_Cake.set("0")
	E_Carlton_Hill_Cake.set("0")
	E_Queen_Park_Cake.set("0")
	E_Jonathan_YO_Cake.set("0")
	E_School_Cake.set("0")
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	var12.set(0)
	var13.set(0)
	var14.set(0)
	var15.set(0)
	var16.set(0)
	txt_West_African_Cake.configure(state = DISABLED)
	txt_Tarte.configure(state = DISABLED)
	txt_Lagos_Chocolate_Cake.configure(state = DISABLED)
	txt_Kilburn_Chocolate_Cake.configure(state = DISABLED)
	txt_Carlton_Hill_Cake.configure(state = DISABLED)
	txt_Queen_Park_Cake.configure(state = DISABLED)
	txt_Jonathan_YO_Cake.configure(state = DISABLED)
	txt_School_Cake.configure(state = DISABLED)
	txt_Latta.configure(state = DISABLED)
	txt_Espresso.configure(state = DISABLED)
	txt_Iced_Latta.configure(state = DISABLED)
	txt_Vale_Coffee.configure(state = DISABLED)
	txt_Cappuccino.configure(state = DISABLED)
	txt_African_Coffee.configure(state = DISABLED)
	txt_American_Coffee.configure(state = DISABLED)
	txt_Iced_Cappuccino.configure(state = DISABLED)


def CostOfItem():
	#Store every item value in a variable
	Item1 = float(E_Latta.get())
	Item2 = float(E_Espresso.get())
	Item3 = float(E_Iced_Latta.get())
	Item4 = float(E_Vale_Coffee.get())
	Item5 = float(E_Cappuccino.get())
	Item6 = float(E_African_Coffee.get())
	Item7 = float(E_American_Coffee.get())
	Item8 = float(E_Iced_Cappuccino.get())
	Item9 = float(E_School_Cake.get())
	Item10 = float(E_Tarte.get())
	Item11 = float(E_Jonathan_YO_Cake.get())
	Item12 = float(E_West_African_Cake.get())
	Item13 = float(E_Lagos_Chocolate_Cake.get())
	Item14 = float(E_Kilburn_Chocolate_Cake.get())
	Item15 = float(E_Carlton_Hill_Cake.get())
	Item16 = float(E_Queen_Park_Cake.get())

	#Item(x) * Price of this item
	PriceOfDrinks = (Item1 * 1.2) + (Item2 * 1.2) + (Item3 * 1.2) + (Item4 * 1.2) + (Item5 * 1.2) + (Item6 * 1.2) + (Item7 * 1.2) + (Item8 * 1.2)
	PriceOfCakes =  (Item9 * 1.5) + (Item10 * 1.5) + (Item11 * 1.5) + (Item12 * 1.5) + (Item13 * 1.5) + (Item14 * 1.5) + (Item15 * 1.5) + (Item16 * 1.5)
	DrinksPrice = str("%.2f"%(PriceOfDrinks)), "$"
	CakesPrice = str("%.2f"%(PriceOfCakes)), "$"
	CostOfCakes.set(CakesPrice)
	CostOfDrinks.set(DrinksPrice)
	#Service charged is fixed
	SC = str("%.2f"%(1.59)), "$" #Service Charge = SC
	ServiceCharge.set(SC)
	#SubTotal is totalcost of items without tax
	SubTotalOfItems = str("%.2f"%(PriceOfCakes + PriceOfDrinks + 1.59)), "$"
	SubTotal.set(SubTotalOfItems)
	Tax = str("%.2f"%((PriceOfDrinks + PriceOfCakes + 1.59) * 0.15)), "$"
	PaidTax.set(Tax)
	#TotalCost is the total cost of every item + tax
	TT = ((PriceOfCakes + PriceOfDrinks + 1.59)*0.15)
	TC = str("%.2f"%(PriceOfDrinks + PriceOfCakes + 1.59 + TT)), "$"
	TotalCost.set(TC)
	#1.59 is Service Charge and it's a fixed price

def chkLatta():
	if (var1.get() == 1):
		txt_Latta.configure(state = NORMAL)
		txt_Latta.focus()
		txt_Latta.delete("0", END)
		E_Latta.set("")
	elif(var1.get() == 0):
		txt_Latta.configure(state = DISABLED)
		E_Latta.set("0")


def chkEspresso():
	if (var2.get() == 1):
		txt_Espresso.configure(state = NORMAL)
		txt_Espresso.focus()
		txt_Espresso.delete("0", END)
		E_Espresso.set("")
	elif(var2.get() == 0):
		txt_Espresso.configure(state = DISABLED)
		E_Espresso.set("0")


def chkIced_Latta():
	if (var3.get() == 1):
		txt_Iced_Latta.configure(state = NORMAL)
		txt_Iced_Latta.focus()
		txt_Iced_Latta.delete("0", END)
		E_Iced_Latta.set("")
	elif(var3.get() == 0):
		txt_Iced_Latta.configure(state = DISABLED)
		E_Iced_Latta.set("0")


def chkVale_Coffee():
	if (var4.get() == 1):
		txt_Vale_Coffee.configure(state = NORMAL)
		txt_Vale_Coffee.focus()
		txt_Vale_Coffee.delete("0", END)
		E_Vale_Coffee.set("")
	elif(var4.get() == 0):
		txt_Vale_Coffee.configure(state = DISABLED)
		E_Vale_Coffee.set("0")


def chkCappuccino():
	if (var5.get() == 1):
		txt_Cappuccino.configure(state = NORMAL)
		txt_Cappuccino.focus()
		txt_Cappuccino.delete("0", END)
		E_Cappuccino.set("")
	elif(var5.get() == 0):
		txt_Cappuccino.configure(state = DISABLED)
		E_Cappuccino.set("0")


def chkAfrican_Coffee():
	if (var6.get() == 1):
		txt_African_Coffee.configure(state = NORMAL)
		txt_African_Coffee.focus()
		txt_African_Coffee.delete("0", END)
		E_African_Coffee.set("")
	elif(var6.get() == 0):
		txt_African_Coffee.configure(state = DISABLED)
		E_African_Coffee.set("0")


def chkAmerican_Coffee():
	if (var7.get() == 1):
		txt_American_Coffee.configure(state = NORMAL)
		txt_American_Coffee.focus()
		txt_American_Coffee.delete("0", END)
		E_American_Coffee.set("")
	elif(var7.get() == 0):
		txt_American_Coffee.configure(state = DISABLED)
		E_American_Coffee.set("0")


def chkIced_Cappuccino():
	if (var8.get() == 1):
		txt_Iced_Cappuccino.configure(state = NORMAL)
		txt_Iced_Cappuccino.focus()
		txt_Iced_Cappuccino.delete("0", END)
		E_Iced_Cappuccino.set("")
	elif(var8.get() == 0):
		txt_Iced_Cappuccino.configure(state = DISABLED)
		E_Iced_Cappuccino.set("0")


def chkWest_African_Cake():
	if (var9.get() == 1):
		txt_West_African_Cake.configure(state = NORMAL)
		txt_West_African_Cake.focus()
		txt_West_African_Cake.delete("0", END)
		E_West_African_Cake.set("")
	elif(var9.get() == 0):
		txt_West_African_Cake.configure(state = DISABLED)
		E_West_African_Cake.set("0")


def chkTarte():
	if (var10.get() == 1):
		txt_Tarte.configure(state = NORMAL)
		txt_Tarte.focus()
		txt_Tarte.delete("0", END)
		E_Tarte.set("")
	elif(var10.get() == 0):
		txt_Tarte.configure(state = DISABLED)
		E_Tarte.set("0")


def chkLagos_Chocolate_Cake():
	if (var11.get() == 1):
		txt_Lagos_Chocolate_Cake.configure(state = NORMAL)
		txt_Lagos_Chocolate_Cake.focus()
		txt_Lagos_Chocolate_Cake.delete("0", END)
		E_Lagos_Chocolate_Cake.set("")
	elif(var11.get() == 0):
		txt_Lagos_Chocolate_Cake.configure(state = DISABLED)
		E_Lagos_Chocolate_Cake.set("0")
	

def chkKilburn_Chocolate_Cake():
	if (var12.get() == 1):
		txt_Kilburn_Chocolate_Cake.configure(state = NORMAL)
		txt_Kilburn_Chocolate_Cake.focus()
		txt_Kilburn_Chocolate_Cake.delete("0", END)
		E_Kilburn_Chocolate_Cake.set("")
	elif(var12.get() == 0):
		txt_Kilburn_Chocolate_Cake.configure(state = DISABLED)
		E_Kilburn_Chocolate_Cake.set("0")
	

def chkCarlton_Hill_Cake():
	if (var13.get() == 1):
		txt_Carlton_Hill_Cake.configure(state = NORMAL)
		txt_Carlton_Hill_Cake.focus()
		txt_Carlton_Hill_Cake.delete("0", END)
		E_Carlton_Hill_Cake.set("")
	elif(var13.get() == 0):
		txt_Carlton_Hill_Cake.configure(state = DISABLED)
		E_Carlton_Hill_Cake.set("0")
	

def chkQueen_Park_Cake():
	if (var14.get() == 1):
		txt_Queen_Park_Cake.configure(state = NORMAL)
		txt_Queen_Park_Cake.focus()
		txt_Queen_Park_Cake.delete("0", END)
		E_Queen_Park_Cake.set("")
	elif(var14.get() == 0):
		txt_Queen_Park_Cake.configure(state = DISABLED)
		E_Queen_Park_Cake.set("0")
	

def chkJonathan_YO_Cake():
	if (var15.get() == 1):
		txt_Jonathan_YO_Cake.configure(state = NORMAL)
		txt_Jonathan_YO_Cake.focus()
		txt_Jonathan_YO_Cake.delete("0", END)
		E_Jonathan_YO_Cake.set("")
	elif(var15.get() == 0):
		txt_Jonathan_YO_Cake.configure(state = DISABLED)
		E_Jonathan_YO_Cake.set("0")
	

def chkSchool_Cake():
	if (var16.get() == 1):
		txt_School_Cake.configure(state = NORMAL)
		txt_School_Cake.focus()
		txt_School_Cake.delete("0", END)
		E_School_Cake.set("")
	elif(var16.get() == 0):
		txt_School_Cake.configure(state = DISABLED)
		E_School_Cake.set("0")
	

def Receipt():
	txt_Receipt.delete("1.0", END)
	x = random.randint(10903, 609235)
	randomRef = str(x)
	Receipt_Ref.set("Bill" + randomRef)
	txt_Receipt.insert(END, "Receipt Ref:\t\t\t" + Receipt_Ref.get() + "\t" + DateOfOrder.get() + "\n")
	txt_Receipt.insert(END, "Item:\t\t\t" + "Cost of item\n")
	if (E_Latta.get() != "0"):
		txt_Receipt.insert(END, "Latta:\t\t\t" + E_Latta.get() + "\n")
	if (E_Espresso.get() != "0"):
		txt_Receipt.insert(END, "Espresso:\t\t\t" + E_Espresso.get() + "\n")
	if (E_Iced_Latta.get() != "0"):
		txt_Receipt.insert(END, "Iced Latta:\t\t\t" + E_Iced_Latta.get() + "\n")
	if (E_Vale_Coffee.get() != "0"):
		txt_Receipt.insert(END, "Vale Coffee:\t\t\t" + E_Vale_Coffee.get() + "\n")
	if (E_Cappuccino.get() != "0"):
		txt_Receipt.insert(END, "Cappuccino:\t\t\t" + E_Cappuccino.get() + "\n")
	if (E_African_Coffee.get() != "0"):
		txt_Receipt.insert(END, "African Coffee:\t\t\t" + E_African_Coffee.get() + "\n")
	if (E_American_Coffee.get() != "0"):
		txt_Receipt.insert(END, "American Coffee:\t\t\t" + E_American_Coffee.get() + "\n")
	if (E_Iced_Cappuccino.get() != "0"):
		txt_Receipt.insert(END, "Iced Cappuccino:\t\t\t" + E_Iced_Cappuccino.get() + "\n")
	if (E_West_African_Cake.get() != "0"):
		txt_Receipt.insert(END, "West African Cake:\t\t\t" + E_West_African_Cake.get() + "\n")
	if (E_Lagos_Chocolate_Cake.get() != "0"):
		txt_Receipt.insert(END, "Lagos Chocolate Cake:\t\t\t" + E_Lagos_Chocolate_Cake.get() + "\n")
	if (E_Kilburn_Chocolate_Cake.get() != "0"):
		txt_Receipt.insert(END, "Kilburn Chocolate Cake:\t\t\t" + E_Kilburn_Chocolate_Cake.get() + "\n")
	if (E_Carlton_Hill_Cake.get() != "0"):
		txt_Receipt.insert(END, "Carlton Hill Cake:\t\t\t" + E_Carlton_Hill_Cake.get() + "\n")
	if (E_Queen_Park_Cake.get() != "0"):
		txt_Receipt.insert(END, "Queen Park Cake:\t\t\t" + E_Queen_Park_Cake.get() + "\n")
	if (E_Jonathan_YO_Cake.get() != "0"):
		txt_Receipt.insert(END, "Jonathan YO Cake:\t\t\t" + E_Jonathan_YO_Cake.get() + "\n")
	if (E_School_Cake.get() != "0"):
		txt_Receipt.insert(END, "School Cake:\t\t\t" + E_School_Cake.get() + "\n")
	txt_Receipt.insert(END, "\n\n" + "Tax:\t\t\t" + txt_Paid_Tax.get() + "\n")
	txt_Receipt.insert(END, "Sub Total:\t\t\t" + txt_SubTotal.get() + "\n")
	txt_Receipt.insert(END, "Total:\t\t\t" + txt_TotalCost.get() + "\n")


def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)


def btnClear():
	global operator
	operator = ""
	text_input.set("")


def btnEquals():
	global operator
	sumup = str(eval(operator))
	text_input.set(sumup)
	operator = ""


#=================================================================================================================================================================================================


#===============================Cakes============================================================================================================================================================

West_African_Cake = Checkbutton(Cake_F, text="West African Cake", variable = var9, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkWest_African_Cake,).grid(row = 0, sticky = W)

Tarte = Checkbutton(Cake_F, text="Tarte", variable = var10, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkTarte,).grid(row = 1, sticky = W)

Lagos_Chocolate_Cake = Checkbutton(Cake_F, text="Lagos Chocolate Cake", variable = var11, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkLagos_Chocolate_Cake,).grid(row = 2, sticky = W)

Kilburn_Chocolate_Cake = Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable = var12, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkKilburn_Chocolate_Cake,).grid(row = 3, sticky = W)

Carlton_Hill_Cake = Checkbutton(Cake_F, text="Carlton Hill Cake", variable = var13, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkCarlton_Hill_Cake,).grid(row = 4, sticky = W)

Queen_Park_Cake = Checkbutton(Cake_F, text="Queen Park Cake", variable = var14, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkQueen_Park_Cake,).grid(row = 5, sticky = W)

Jonathan_YO_Cake = Checkbutton(Cake_F, text="Jonathan YO Cake", variable = var15, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkJonathan_YO_Cake,).grid(row = 6, sticky = W)

School_Cake = Checkbutton(Cake_F, text="School Cake", variable = var16, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkSchool_Cake,).grid(row = 7, sticky = W)

#===============================Entry box for cakes================================================================================================================================================

txt_West_African_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_West_African_Cake)
txt_West_African_Cake.grid(row = 0, column = 1)

txt_Tarte = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Tarte)
txt_Tarte.grid(row = 1, column = 1)

txt_Lagos_Chocolate_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Lagos_Chocolate_Cake)
txt_Lagos_Chocolate_Cake.grid(row = 2, column = 1)

txt_Kilburn_Chocolate_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Kilburn_Chocolate_Cake)
txt_Kilburn_Chocolate_Cake.grid(row = 3, column = 1)

txt_Carlton_Hill_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Carlton_Hill_Cake)
txt_Carlton_Hill_Cake.grid(row = 4, column = 1)

txt_Queen_Park_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Queen_Park_Cake)
txt_Queen_Park_Cake.grid(row = 5, column = 1)

txt_Jonathan_YO_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Jonathan_YO_Cake)
txt_Jonathan_YO_Cake.grid(row = 6, column = 1)

txt_School_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_School_Cake)
txt_School_Cake.grid(row = 7, column = 1)

#====================================================================================================================================================================================================


#================================Drinks==============================================================================================================================================================

Latta = Checkbutton(Drinks_F, text="Latta", variable = var1, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue', command = chkLatta).grid(row = 0, sticky = W)

Espresso = Checkbutton(Drinks_F, text="Espresso", variable = var2, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkEspresso).grid(row = 1, sticky = W)

Iced_Latta = Checkbutton(Drinks_F, text="Iced Latta", variable = var3, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkIced_Latta).grid(row = 2, sticky = W)

Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable = var4, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkVale_Coffee).grid(row = 3, sticky = W)

Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable = var5, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkCappuccino).grid(row = 4, sticky = W)

African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable = var6, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkAfrican_Coffee).grid(row = 5, sticky = W)

American_Coffee = Checkbutton(Drinks_F, text="American Coffee", variable = var7, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkAmerican_Coffee).grid(row = 6, sticky = W)

Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable = var8, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue", command = chkIced_Cappuccino).grid(row = 7, sticky = W)

#================================Entry box for drinks================================================================================================================================================

txt_Latta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Latta)
txt_Latta.grid(row = 0, column = 1)

txt_Espresso = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Espresso)
txt_Espresso.grid(row = 1, column = 1)

txt_Iced_Latta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Iced_Latta)
txt_Iced_Latta.grid(row = 2, column = 1)

txt_Vale_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Vale_Coffee)
txt_Vale_Coffee.grid(row = 3, column = 1)

txt_Cappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Cappuccino)
txt_Cappuccino.grid(row = 4, column = 1)

txt_African_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_African_Coffee)
txt_African_Coffee.grid(row = 5, column = 1)

txt_American_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_American_Coffee)
txt_American_Coffee.grid(row = 6, column = 1)

txt_Iced_Cappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED, textvariable = E_Iced_Cappuccino)
txt_Iced_Cappuccino.grid(row = 7, column = 1)

#==================================Total Cost================================================================================================================================================================

lblCostOfDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text="Cost Of Drinks\n", bg='Powder Blue', fg='Black')
lblCostOfDrinks.grid(row=0, column=0, sticky = W)

txt_Cost_of_drinks = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = CostOfDrinks, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_Cost_of_drinks.grid(row=0, column=1)



lblCostOfCakes = Label(Cost_F, font=('arial', 14, 'bold'), text="Cost Of Cakes\n", bg='Powder Blue', fg='Black')
lblCostOfCakes.grid(row=1, column=0, sticky = W)

txt_Cost_of_Cakes = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = CostOfCakes, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_Cost_of_Cakes.grid(row=1, column=1)



lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text="Service Charge\n", bg='Powder Blue', fg='Black')
lblServiceCharge.grid(row=2, column=0, sticky = W)

txt_Service_Charge = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = ServiceCharge, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_Service_Charge.grid(row=2, column=1)

#==================================Payment Information=======================================================================================================================================================

lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text="Paid Tax\n", bg='Powder Blue', fg='Black')
lblPaidTax.grid(row=0, column=2, sticky = W)

txt_Paid_Tax = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = PaidTax, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_Paid_Tax.grid(row=0, column=3)



lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text="Sub Total\n", bg='Powder Blue', fg='Black')
lblSubTotal.grid(row=1, column=2, sticky = W)

txt_SubTotal = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = SubTotal, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_SubTotal.grid(row=1, column=3)



lblToatalCost = Label(Cost_F, font=('arial', 14, 'bold'), text="Total Cost\n", bg='Powder Blue', fg='Black')
lblToatalCost.grid(row=2, column=2, sticky = W)

txt_TotalCost = Entry(Cost_F, font=('arial', 14, 'bold'), textvariable = TotalCost, bg = 'white', bd = 7, insertwidth = 2, justify = RIGHT)
txt_TotalCost.grid(row=2, column=3)

#==================================Receipt===================================================================================================================================================================

txt_Receipt = Text(Receipt_F, width = 46, height = 12, bg = 'white', bd = 4, font=('arial', 12, 'bold'))
txt_Receipt.grid(row=0, column=0)

#============================================================================================================================================================================================================

btn_Total = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Total", bg = "Powder Blue", command = CostOfItem).grid(row=0, column=0)
btn_Receipt = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Receipt", bg = "Powder Blue", command = Receipt).grid(row=0, column=1)
btn_Reset = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Reset", bg = "Powder Blue", command = Reset).grid(row=0, column=2)
btn_Exit = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Exit", bg = "Powder Blue", command = iExit).grid(row=0, column=3)

#==================================Calculator Display=========================================================================================================================================================

txt_Display = Entry(Cal_F, width = 45, bg = 'white', bd = 4, font=('arial', 12, 'bold'), justify = RIGHT)
txt_Display.grid(row=0, column=0, columnspan = 4, pady = 1)
txt_Display.insert(0, "0")

#==================================Calculator Buttons=========================================================================================================================================================

btn7 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "7", bg = "Powder Blue", command = lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "8", bg = "Powder Blue", command = lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "9", bg = "Powder Blue", command = lambda:btnClick(9)).grid(row=2, column=2)
btnAdd = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "+", bg = "Powder Blue", command = lambda:btnClick("+")).grid(row=2, column=3)
btn4 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "4", bg = "Powder Blue", command = lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "5", bg = "Powder Blue", command = lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "6", bg = "Powder Blue", command = lambda:btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "-", bg = "Powder Blue", command = lambda:btnClick("-")).grid(row=3, column=3)
btn1 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "1", bg = "Powder Blue", command = lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "2", bg = "Powder Blue", command = lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "3", bg = "Powder Blue", command = lambda:btnClick(3)).grid(row=4, column=2)
btnMult = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "*", bg = "Powder Blue", command = lambda:btnClick("*")).grid(row=4, column=3)
btn0 = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "0", bg = "Powder Blue", command = lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "C", bg = "Powder Blue", command = btnClear).grid(row=5, column=1)
btnEqual = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "=", bg = "Powder Blue", command = btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "/", bg = "Powder Blue", command = lambda:btnClick("/")).grid(row=5, column=3)




root.mainloop()

