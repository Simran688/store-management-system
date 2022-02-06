from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
from datetime import date
import smtplib
import random
from mail import gmail
import pyodbc


root = Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
root.title("Registration Form")
root.configure(background="white")

#'''''bg image''''''
#bgimg=ImageTk.PhotoImage(file="sms.jpg")
#bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)
 

app_width=700
app_height=600
xcor=(root.winfo_screenwidth()/2)-(app_width/2)
ycor=(root.winfo_screenheight()/2)-(app_height/2)
frame1=Frame(root,bg="white")
frame1.place(x=xcor,y=ycor,width=700,height=600)



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')

email_var=StringVar()
otp_var=StringVar()
todays_date=date.today()
now = todays_date.strftime("%m/%d/%y")
user="StoreManagementSystem.SLA@gmail.com"
password="smspython"
to_addrs=email_var.get()



#defining function msg() using messagebox
def msg():
    msg.flag=0
    error_msg=""
    if (e1.index("end") == 0):
        error_msg="First name \n"
        msg.flag+=1
    if(e2.index("end") == 0):
        error_msg=error_msg+"Last name\n"
        msg.flag+=1
    if(e3.index("end") == 0 or e3.get().find('@gmail.com')<0):
        error_msg=error_msg+"email\n"
        msg.flag+=1
    if(var.get()==0):
        error_msg=error_msg+"gender\n"
        msg.flag+=1
    if(e4.index("end") == 0 or len(e4.get())<10 or len(e4.get())>10):
        error_msg=error_msg+"contact no.\n"
        msg.flag+=1
    if(e5.index("end") == 0):
        error_msg=error_msg+"address\n"
        msg.flag+=1
    if(svar.get()=="Select designation"):
        error_msg=error_msg+"designation\n"
        msg.flag+=1
    # if((-dob.get_date())<18):
    #     error_msg=error_msg+"age should be greater than 18\n"
    #     msg.flag+=1
    # if((date.today()-dob.get_date())>80):
    #     error_msg=error_msg+"age should be smaller than 80\n"
    #     msg.flag+=1
    if msg.flag!=0:
        mb.showwarning('Missing details', "Enter the value of \n"+error_msg)


def age():
    end_date = now - datetime.timedelta(days=int(dob.get()))
    converted_date.config(text=f"Date: {end_date.strftime('%m/%d/%Y')}")
def save():
    if(msg.flag==0):
        g = var.get()
        designation = svar.get()
        db = dob.get_date()
        d = db.strftime('%d/%m/%Y')
        if(g==1):
            gender ='male'
        else:
            gender ='female'
        fname=e1.get()
        lname=e2.get()
        phone=e4.get()
        email=e3.get()
        Address=e5.get()
        id=str(random.randint(100000,999999))
        idpassword=str(random.randint(10000,99999))
        print(id,fname,lname,d,gender,phone,email,Address,idpassword,designation,now)
        authentication='False'
        mb.showinfo("Process","Please wait....")
        if(designation=="Supplier"):
            #authentication='True'
            #user="StoreManagementSystem.SLA@gmail.com"
            #password="smspython"
            #to_addrs=email_var.get()
            #subject="Account details"
            # text="Hello "+fname+" Your UserId is your gmail Id and Password is "+idpassword+"\nThank you"
            # print(user,password)
            # gmail(user, password, to_addrs, subject, text)
            # cursor = conn.cursor()
            # cursor.execute("INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id,fname,lname,d,gender,phone,email,Address,idpassword,designation,authentication,now))
            # conn.commit()
            # print("Data saved successfully")
            # mb.showinfo("Information", "Data Saved successfully")
            authentication='True'
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id,fname,lname,d,gender,phone,email,Address,idpassword,designation,authentication,now))
            conn.commit()
            print("Data saved successfully")
            mb.showinfo("Information", "Data Saved successfully")
            user="StoreManagementSystem.SLA@gmail.com"
            password="smspython"
            to_addrs=email_var.get()
            subject="Account details"
            text="Hello "+fname+" Your UserId is your gmail Id and Password is "+idpassword+"\nThank you"
            print(user,password)
            gmail(user, password, to_addrs, subject, text)
            text="New Supplier added "+fname+"\nContact number- "+phone+"\nGmail id- "+to_addrs+"\n id- "+id+"."
            gmail(user, password, user, "New Supplier", text)
        elif(designation=="Admin"):
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id,fname,lname,d,gender,phone,email,Address,idpassword,designation,authentication,now))
            conn.commit()
            print("Data saved successfully")
            mb.showinfo("Information", "Data Saved successfully")
            mb.showinfo("Information", "Your Id and Password sending to Store management main email id")
            msgs="New Admin's detected\n email: "+email+"\npasswod:"+idpassword+"\nname: "+fname+"\nand ID: "+id
            gmail("StoreManagementSystem.SLA@gmail.com", "smspython", "StoreManagementSystem.SLA@gmail.com", "Request", msgs)
            rid=str(random.randint(10000, 99999))
            desc="new Admin"
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Requests VALUES(?,?,?,?)",(rid,id,desc,now))
            conn.commit()
            mb.showinfo('Success', 'Registration done successfully\nUserId and password will sent on email after authentication')
            print("Data sent to admin")
        else:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id,fname,lname,d,gender,phone,email,Address,idpassword,designation,authentication,now))
            conn.commit()
            print("Data saved successfully")
            mb.showinfo("Information", "Data Saved successfully")
            rid=str(random.randint(10000, 99999))
            desc="new employee"
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Requests VALUES(?,?,?,?)",(rid,id,desc,now))
            conn.commit()
            mb.showinfo('Success', 'Registration done successfully\nUserId and password will sent on email after authentication')
            print("Data sent to admin")
    

def send_otp():
    msg()
    if(msg.flag==0):
        user="StoreManagementSystem.SLA@gmail.com"
        password="smspython"
        to_addrs=email_var.get()
        send_otp.otp=str(random.randint(1000,9999))
        subject="OTP"
        text="Your otp for Store Management is "+send_otp.otp
        gmail(user, password, to_addrs, subject, text)
        b2["text"] = "Resend"
        b1["state"] = "normal"

def saveinfo():
    msg()
    if(msg.flag==0):
        print(send_otp.otp,otp_var.get())
        if(otp_var.get()==""):
            mb.showwarning('Missing details', 'enter OTP')
        elif(send_otp.otp==otp_var.get()):
            save()
            root.destroy()
            import sms_signup_page
        else:
            mb.showwarning('wrong details', 'wrong OTP')
    

# creating labels and entry widgets
l1 = Label(frame1, text="REGISTER YOURSELF HERE",font=("times new roman",20,"bold"),bg='white',fg='green')
l1.place(x=240,y=30)
l2 = Label(frame1, text="First Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
l2.place(x=90,y=80)
e1 = Entry(frame1,font=("times new roman",15),bg='lightgray')
e1.place(x=90,y=120,width=230)
l3 = Label(frame1, text="Last Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
l3.place(x=400,y=80)
e2 = Entry(frame1,font=("times new roman",15),bg='lightgray')
e2.place(x=400,y=120,width=230)
l4 = Label(frame1, text="Email",font=("times new roman",15,"bold"),bg='white',fg='gray')
l4.place(x=90,y=170)
e3 = Entry(frame1,font=("times new roman",15),textvariable = email_var,bg='lightgray')
e3.place(x=90,y=210,width=230)
l5 = Label(frame1, text="DOB",font=("times new roman",15,"bold"),bg='white',fg='gray')
l5.place(x=400,y=270)

# dateEntry -Date selection entry with drop-down calendar
dob = DateEntry(frame1,  bg='lightgray',date_pattern='dd/mm/Y', font=("times new roman",15))
dob.place(x=400,y=310,width=230)

l6 = Label(frame1, text="Gender",  font=("times new roman",15,"bold"),bg='white',fg='gray')
l6.place(x=90,y=270)

# radiobuttons
var = IntVar()
r1 = Radiobutton(frame1, text="Male", variable=var, value=1, font=("times new roman",15),bg='lightgray')
r1.place(x=90,y=300)
r2 = Radiobutton(frame1, text="Female", variable=var, value=2, font=("times new roman",15),bg='lightgray')
r2.place(x=200,y=300)

l7 = Label(frame1, text="Contact no.",font=("times new roman",15,"bold"),bg='white',fg='gray')
l7.place(x=400,y=170)
e4 = Entry(frame1,font=("times new roman",15),bg='lightgray')
e4.place(x=400,y=210,width=230)
l8 = Label(frame1, text="Address",font=("times new roman",15,"bold"),bg='white',fg='gray')
l8.place(x=90,y=370)
e5 = Entry(frame1,font=("times new roman",15),bg='lightgray')
e5.place(x=90,y=410,width=230)
l9 = Label(frame1, text="OTP",font=("times new roman",15,"bold"),bg='white',fg='gray')
l9.place(x=90,y=460)
e6 = Entry(frame1,font=("times new roman",15),textvariable = otp_var,bg='lightgray')
e6.place(x=90,y=490,width=230)
l10 = Label(frame1, text="Select designation",font=("times new roman",15,"bold"),bg='white',fg='gray')
l10.place(x=400,y=370)









#l1 = Label(root, text="Registration form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
#l1.place(x=70,y=20)
#l2 = Label(root, text="First Name",width=20,font=("times",12,"bold"),bg='grey')
#l2.place(x=70,y=90)
#e1 = Entry(root,width=30,bd=2)
#e1.place(x=240,y=90)
#l3 = Label(root, text="Last Name",width=20,font=("times",12,"bold"),bg='grey')
#l3.place(x=70,y=140)
#e2 = Entry(root,width=30,bd=2)
#e2.place(x=240,y=140)
#l4 = Label(root, text="Email",width=20,font=("times",12,"bold"),bg='grey')
#l4.place(x=70,y=190)
#e3 = Entry(root,textvariable = email_var, width=30, bd=2)
#e3.place(x=240,y=190)
#l5 = Label(root, text="DOB",width=20,font=("times",12,"bold"),bg='grey')
#l5.place(x=70,y=240)

# dateEntry -Date selection entry with drop-down calendar

#dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd-mm-Y', borderwidth=3,selectmode = 'day',
 #           year = todays_date.year-18, month = 5,
  #          day = 22)
#dob.place(x=240,y=240)

#l6 = Label(root, text="Gender", width=20, font=("times",12,"bold"),bg='grey')
#l6.place(x=70,y=290)

# radiobuttons
#var = IntVar()
#r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
#r1.place(x=235,y=290)
#r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='grey')
#r2.place(x=315,y=290)

#l7 = Label(root, text="Contact no.",width=20,font=("times",12,"bold"),bg='grey')
#l7.place(x=70,y=340)
#e4 = Entry(root,width=30,bd=2)
#e4.place(x=240,y=340)
#l8 = Label(root, text="Address",width=20,font=("times",12,"bold"),bg='grey')
#l8.place(x=70,y=390)
#e5 = Entry(root,width=30,bd=2)
#e5.place(x=240,y=390)


#l10 = Label(root, text="Select designation",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
#l10.place(x=70,y=440)
#l9 = Label(root, text="OTP",width=20,font=("times",12,"bold"),bg='grey')
#l9.place(x=70,y=540)
#e6 = Entry(root,textvariable = otp_var,width=30,bd=2)
#e6.place(x=240,y=540)

# create a dropdown menu with the OptionMenu widget
#svar = StringVar()
#svar.set("Select designation")
#option = ("Admin", "Employee", "Supplier")
#o = OptionMenu(root,svar, *option)
#o.config(font=("times",11),bd=3)
#o.place(x=240,y=440,width=190)



svar = StringVar()
svar.set("Select designation")
option = ("Admin", "Employee", "Supplier")
o = OptionMenu(frame1,svar, *option)
o.config(font=("times new roman",15),bg='lightgray')
o.place(x=400,y=400,width=230)



def back():
  root.destroy()
  import sms_signup_page
                 



# submit and cancel buttons


b1 = Button(frame1, text='Submit',width=10,command= saveinfo,bg='green',fg='white',font=("times new roman",15,"bold"),state="disabled")
b1.place(x=100,y=550)
b2 = Button(frame1, text='Verify',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"),command=send_otp)
b2.place(x=280,y=550)
b3 = Button(frame1, text='Cancel',width=10,command=back,bg='maroon',fg='white',font=("times new roman",15,"bold"))
b3.place(x=460,y=550)
#b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"),state="disabled")
#b1.place(x=40,y=580)
#b2 = Button(root, text='Verify',width=15,bg='orange',fg='white',font=("times",12,"bold"),command=send_otp)
#b2.place(x=190,y=490)
#b3 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
#b3.place(x=340,y=580)

root.mainloop()

