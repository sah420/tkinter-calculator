from tkinter import *

root = Tk()

# Display Box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	x = e.get()
	global x_num
	global math
	math = "addition"
	x_num = float(x)
	e.delete(0, END)

def button_sub():
	x = e.get()
	global x_num
	global math
	math = "subtraction"
	x_num = float(x)
	e.delete(0, END)

def button_mult():
	x = e.get()
	global x_num
	global math
	math = "multiplication"
	x_num = float(x)
	e.delete(0, END)

def button_div():
	x = e.get()
	global x_num
	global math
	math = "division"
	x_num = float(x)
	e.delete(0, END)

def button_equal():
	y = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, x_num + float(y))
	elif math == "subtraction":
		e.insert(0, x_num - float(y))
	elif math == "multiplication":
		e.insert(0, x_num * float(y))	
	elif math == "division":
		e.insert(0, x_num / float(y))


	

# Defining the Buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=94, pady=20, command=lambda: button_click(0))
buttonperiod = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
buttonaddition = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonsub = Button(root, text="—", padx=40, pady=20, command=button_sub)
buttonequal = Button(root, text="=", padx=40, pady=20, command=button_equal)
buttonmult = Button(root, text="x", padx=40, pady=20, command=button_mult)
buttondiv = Button(root, text="/", padx=40, pady=20, command=button_div)
buttonclear = Button(root, text="AC", padx=140, pady=20, command=button_clear)

#Placing the buttons
button1.grid(row=5 ,column=0)
button2.grid(row=5 ,column=1)
button3.grid(row=5 ,column=2)
button4.grid(row=4 ,column=0)
button5.grid(row=4 ,column=1)
button6.grid(row=4 ,column=2)
button7.grid(row=3 ,column=0)
button8.grid(row=3 ,column=1)
button9.grid(row=3 ,column=2)
button0.grid(row=6 ,column=0, columnspan=2)
buttonclear.grid(row=2, column=0, columnspan=3)
buttonmult.grid(row=2, column=3)
buttondiv.grid(row=3, column=3)
buttonaddition.grid(row=4, column=3)
buttonsub.grid(row=5, column=3)
buttonperiod.grid(row=6, column=2)
buttonequal.grid(row=6, column=3)



root.mainloop()