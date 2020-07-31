from datetime import date, timedelta
from tkinter import *

root= Tk()
root.title("Age Calculator")
today = date.today()

def onclick():
	global label_out
	global label_day
	global label_age
	
	try:
		year_val= int(birthday_year.get())
		month_val = int(birthday_month.get())
		date_val = int(birthday_date.get())
		birthday = date(year_val, month_val, date_val)
		
		if birthday > today:
			label_out= Label(root, text = "Please enter correct date of birth")
			label_out.grid(row=5, column=0, columnspan=3)
		
		elif today == birthday:
			label_out = Label(root, text = "Happy birthday !! It's your birthday.")
			label_out.grid(row=7, column=0, columnspan = 3)
		else:
			week_day = birthday.weekday()
			wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
			age  = today.year - birthday.year
			birthday = birthday.replace(year = today.year)
			if today < birthday:
				rem_days = (birthday-today).days
				label_out = Label(root, text = str(rem_days) + " days remaining for your next birthday.")
				label_out.grid(row=7, column=0, columnspan = 3)
				
			else:
				birthday = birthday.replace(year = today.year+1)
				rem_days = (birthday-today).days			
				label_out = Label(root, text = str(rem_days) + " days remaining for your next birthday.")
				label_out.grid(row=7, column=0, columnspan = 3)
				
			label_day = Label(root, text = "You were born on " + wd[week_day])
			label_day.grid(row=6, column= 0, columnspan=4)
			label_age= Label(root, text="Your age is " + str(age) + " years.")
			label_age.grid(row=5, column=0, columnspan= 3)
				
	except:
		days = " Please enter date in correct format"
		label_out = Label(root, text = days)
		label_out.grid(row=5, column=0, columnspan=3)
	
def clr_btn():
	birthday = today
	eq1.set("")
	eq2.set("")
	eq3.set("")
	label_out.destroy()
	label_day.destroy()
	label_age.destroy()
	
label_day = Label(root)
label_age = Label(root)

heading= Label(root, text="Age and Birthday remaining days calculator")
heading.grid(row=0, column=0, columnspan=3)

label1= Label(root, text="Birth: Year")
label1.grid(row=1, column=0)

eq1= StringVar()
eq2= StringVar()
eq3= StringVar()

birthday_year = Entry(root, width=10, textvariable = eq1)
birthday_year.grid(row=2, column=0)

label2= Label(root, text="Month")
label2.grid(row=1, column=1)
birthday_month = Entry(root, width=5, textvariable = eq2)
birthday_month.grid(row=2,  column= 1)

label3= Label(root, text="Date")
label3.grid(row=1, column=2)
birthday_date= Entry(root, width=5, textvariable = eq3)
birthday_date.grid(row=2, column=2)

today_label = Label(root, text= "Today's date is : " + str(today))
today_label.grid(row=3, column=0, columnspan=3)

submit_btn= Button(root, text="Submit", command= onclick)
submit_btn.grid(row=4, column=2)

clr_btn= Button(root, text="Clear", command= clr_btn)
clr_btn.grid(row=4, column=0)

root.mainloop()