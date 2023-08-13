from tkinter import*#tkinter is a package or module
from tkinter import messagebox as mb
import pymysql
import re
import json

win =Tk()#Tk() is a predefined class
def Login():
	#messagebox.showinfo('showinfo',"welcome to home page")
	conobj=pymysql.connect(host="localhost",user="root",password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use MCQPORTAL')
	x=username.get() 
	y=Password.get() 
	curobj.execute('select username,New_password from Register')
	record=curobj.fetchall()
	#print("table record=",record)
	for u,p in record:
		if u==x and p==y:
			mb.showinfo('showinfo',"welcome to home page")
			guiWindow=Tk()
			guiWindow.title("JITHON Sujit-Quiz portal")
			guiWindow.geometry("450x450")
			class myQuiz:  
				def init(self):
					self.quesNumber = 0 
					self.displayTitle()
					self.displayQuestion()
					self.optSelected = IntVar()
					self.options = self.radioButtons()
					self.displayOptions()
					self.buttons()
					self.dataSize = len(question)
					x=  len(question)
					self.rightAnswer = 0

				def displayResult(self):
					wrongCount = self.dataSize - self.rightAnswer
					rightAnswer = f"Correct: {self.rightAnswer}"
					wrongAnswer = f"Wrong: {wrongCount}"
					the_score = int(self.rightAnswer / self.dataSize * 100)
					the_result = f"Score: {the_score}%"
					mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")
				def checkAnswer(self, quesNumber):
						if self.optSelected.get() == answer[quesNumber]:
							return True

				def nextButton(self):
					if self.checkAnswer(self.quesNumber):
						self.rightAnswer += 1
					self.quesNumber += 1
					if self.quesNumber == self.dataSize:
						self.displayResult()
						guiWindow.destroy()
					else:
						self.displayQuestion()
						self.displayOptions()


				def buttons(self):
					next_button = Button(  guiWindow,  text = "Next",  command = self.nextButton,  width = 10,  bg = "blue",  fg = "white",  font = ("ariel", 16, "bold")  )
					next_button.place(x = 350, y = 380)
					quit_button = Button(  guiWindow,  text = "Quit",  command = guiWindow.destroy,  width = 10,bg = "red",  fg = "white",  font = ("ariel", 16, " bold")  )
					quit_button.place(x = 500, y = 380)

				def displayOptions(self):
					val = 0
					self.optSelected.set(0)
					for opt in opts[self.quesNumber]:
						self.options[val]['text'] = opt
						val += 1

				def displayQuestion(self):
					quesNumber = Label(  guiWindow,  text = question[self.quesNumber],  width = 60,  font = ('ariel', 16, 'bold'),  anchor = 'w'  )
					quesNumber.place(x = 70, y = 100)

				def displayTitle(self):
					myTitle = Label(  guiWindow,  text = "JITHON Quiz Portal",width = 50,  bg = "red",  fg = "white",  font = ("ariel", 20, "bold")  )
					myTitle.place(x = 0, y = 2)

				def radioButtons(self):
					qList = []
					y_pos = 150
					while len(qList) < 4:
						radio_button = Radiobutton(  guiWindow,  text = " ",  variable = self.optSelected,  value = len(qList) + 1,  font = ("ariel", 14)  )
						qList.append(radio_button)
						radio_button.place(x = 100, y = y_pos)
						y_pos += 40
					return qList
			with open('data.json') as json_file:
				data = json.load(json_file) 
			question = (data['ques']) 
			opts = (data['choices']) 
			answer = (data[ 'ans']) 
			quiz = myQuiz()
			guiWindow.mainloop()
	#print(x," ",y)	 
	curobj.close() 
	conobj.close()
def Exit():
	win.destroy()
def New():
	mb.showinfo('showinfo',"welcome to registration page")
	def Submit(): 
		conobj=pymysql.connect(host="localhost",user="root",password='',port=3306)
		curobj=conobj.cursor() 
		curobj.execute('use MCQPORTAL;') 
		UN=username.get()
		EM=Email.get()
		GE=str(var.get())
		if int(GE)==0:
			GE="male"
		else:
			GE="female"
		NP=New_password.get()
		CNP=Confirm_pass.get()
		print(UN,EM,GE,NP,CNP)
		#checkNP="^[a-zA-Z0-9]{8}$"
		if len(NP)>=8 and len(NP)<=16:
			if re.findall(checkNP,NP):
					curobj.execute('insert into Register values("' +UN+'","' +EM+'","' +GE+'","' +NP+'","' +CNP+'");')
		
			conobj.commit()
			curobj.close() 
			conobj.close()
		else:
			mb.showinfo("password length between 8 to 16")

		a1=username.get()
		b1=Email.get()
		c1=var.get()
		d1=New_password.get()
		e1=Confirm_pass.get()
	def Reset():
		username.delete(0,END)
		Email.delete(0,END)
		New_password.delete(0,END)
		Confirm_pass.delete(0,END)
		
	win1=Tk()
	win.title("registration page")
	win1.geometry('450x450')
	Label(win1,text="please register here",font=('bold',25),bg="yellow",fg="red",width="25",height="2").place(x=100,y=50)
	l1=Label(win1,text="Enter reg no./user Id",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=105,y=150)
	username=Entry(win1,font=('bold',18),bg="pink",fg="black")
	username.place(x=365 ,y=150)

	l2=Label(win1,text="Enter emailid",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=105,y=200)
	Email=Entry(win1,font=('bold',18),bg="pink",fg="black")
	Email.place(x=365,y=200)
	#var=StringVar()
	l3=Label(win1,text="Select Gender",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=105,y=250)
	#Gender=Entry(win1,font=('bold',18),bg="pink",fg="black")
	#Gender.place(x=350,y=250)

	var=IntVar()
	r1=Radiobutton(win1,value=0,variable=var,text="M")
	r1.place(x=365,y=250)
	r2=Radiobutton(win1,value=1,variable=var,text="F")
	r2.place(x=425,y=250)

	l4=Label(win1,text="Set new password",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=105,y=300)
	New_password=Entry(win1,font=('bold',18),bg="pink",fg="black",show="*")
	New_password.place(x=365,y=300)

	l5=Label(win1,text="confirm password",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=105,y=350)
	Confirm_pass=Entry(win1,font=('bold',18),bg="pink",fg="black",show="*")
	Confirm_pass.place(x=365,y=350)

	Submit=Button(win1,text="SUBMIT",font=('bold',12),bg="blue",fg="white",height="1",width="10",command=Submit).place(x=150,y=400)

	Reset=Button(win1,text="RESET",font=('bold',12),bg="blue",fg="white",height="1",width="10",command=Reset).place(x=350,y=400)

	win1.mainloop()
win.title("LOGIN PAGE")
win.geometry("450x300")
win.maxsize(height=550,width=650)
win.minsize(height=550,width=650)

Label(win,text="please login here",font=('bold',25),bg="yellow",fg="red",width="25",height="2").place(x=100,y=50)

l1=Label(win,text="Enter reg no./user Id",font=('bold',18),bg="blue",fg="white",width="18",height="1",border="1").place(x=100,y=150)
username=Entry(win,font=('bold',18),bg="pink",fg="black")
username.place(x=365,y=150)

l2=Label(win,text="Enter password",font=('bold',18),bg="blue",fg="white",width="18",height="1").place(x=100,y=200)
Password=Entry(win,font=('bold',18),bg="pink",fg="black",show="*")
Password.place(x=365,y=200)

login=Button(win,text="LOGIN",font=('bold',12),bg="blue",fg="white",height="1",width="10",command=Login).place(x=250,y=250)

Exit=Button(win,text="EXIT",font=('bold',12),bg="red",fg="white",height="1",width="10",command=Exit).place(x=400,y=250)

new_user=Button(win,text="New user",font=('bold',12),bg="yellow",fg="black",height="1",width="10",command=New).place(x=325,y=300)

win.mainloop()#to display a window,win is a object