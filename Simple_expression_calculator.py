from tkinter import *
root = Tk()
root.title("Calculator")


expression =""
def button_click(num): 
    global expression
    expression = expression + num
    equation.set(expression) 
    
def button_equal():
	global expression
	try: 
		total = str(eval(expression))
		equation.set(total)
		expression = "" 
	except:
		equation.set("Error")

def button_clear():
	global expression
	expression= ""
	equation.set("")

def button_bck():
	global expression
	eq.delete(len(expression)-1, END)
	expression = expression[:-1]

equation = StringVar()
eq= Entry(root, textvariable= equation)
eq.grid(row=0, column=0, columnspan=3)

button_1 = Button(root, text="1", padx=50, pady=40, command= lambda: button_click("1"))
button_1.grid(row=3, column=0)

button_2 = Button(root, text="2", padx=50, pady=40, command= lambda:  button_click("2"))
button_2.grid(row=3, column=1)

button_3 = Button(root, text="3", padx=50, pady=40, command= lambda: button_click("3"))
button_3.grid(row=3, column=2)

button_4 = Button(root, text="4", padx=50, pady=40, command= lambda: button_click("4"))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", padx=50, pady=40, command= lambda: button_click("5"))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", padx=50, pady=40, command= lambda: button_click("6"))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", padx=50, pady=40, command= lambda: button_click("7"))
button_7.grid(row=1, column=0)

button_8 = Button(root, text="8", padx=50, pady=40, command= lambda: button_click("8"))
button_8.grid(row=1, column=1)

button_9 = Button(root, text="9", padx=50, pady=40, command= lambda: button_click("9"))
button_9.grid(row=1, column=2)

button_0  = Button(root, text="0", padx=50, pady=40, command= lambda: button_click("0"))
button_0.grid(row=4, column=0)

button_brac1= Button(root, text="(", padx=53, pady=40, command= lambda: button_click("("))
button_brac1.grid(row=5, column=2)

button_brac2= Button(root, text=")", padx=50, pady=40, command= lambda: button_click(")"))
button_brac2.grid(row=5, column=3)

button_add= Button(root, text="+", padx=50, pady=40,  command= lambda:  button_click("+"))
button_add.grid(row=1, column=3)

button_sub= Button(root, text="-", padx=55, pady=40,  command= lambda:  button_click("-"))
button_sub.grid(row=2, column=3)

button_div= Button(root, text="/", padx=50, pady=40,  command= lambda:  button_click("/"))
button_div.grid(row=3, column=3)

button_mul= Button(root, text="*", padx=50, pady=40,  command= lambda:  button_click("*"))
button_mul.grid(row=4, column=3)

button_equal= Button(root, text="=", padx=138, pady=40, command= button_equal)
button_equal.grid(row=4, column=1, columnspan=2)

button_clear= Button(root, text="Clear", padx=20, pady=40, command= button_clear)
button_clear.grid(row=5, column=1)

button_bck = Button(root, text="<--", padx=40, pady=40, command= button_bck)
button_bck.grid(row=5, column=0)

root.mainloop()