# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox as mb
# from tkcalendar import DateEntry
# import datetime
# from PIL import Image,ImageTk
from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
from PIL import ImageTk
import pyodbc
from tkinter import ttk
import tkinter as tk
from mail import gmail
import datetime
from datetime import date
from turtle import textinput
import smtplib
import random
from tkinter import simpledialog



mains=False
if mains==True:
    print("File one excuted when ran directly")
else:
    def take_id(idss,email,mains):
        take_id.s_id=idss
        print(idss)
        m=mains
        if m==True:
            
            root = Tk()
            root.title("Store Management System")
            root.state('zoomed')
            
            #bg=ImageTk.PhotoImage(file="stores.jpg")
            #label_bg=Label(root,image=bg)
            #label_bg.place(x=0,y=0,relwidth=1,relheight=1)
            global name,dob,contact,emailid,address,em,p
            name_label=tk.StringVar()
            email_label=tk.StringVar()
            contact_label=tk.StringVar()
            dob_label=tk.StringVar()
            doj_label=tk.StringVar()
            address_label=tk.StringVar()
            gender_label=tk.StringVar()
            desig_label=tk.StringVar()
            password_label=tk.StringVar()
            otp_var=StringVar()
            
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')
            cur = conn.cursor()   
            cur.execute("SELECT id,f_name,phone,gender,dob,doj,password,address,designation,Email FROM members where id=?",(idss))
            row=cur.fetchall()
            for dt in row:
                #title_tabel.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8])) 
                print(row)
                name_label.set(row[0][1]) 
                contact_label.set(row[0][2])
                gender_label.set(row[0][3])
                dob_label.set(row[0][4])
                doj_label.set(row[0][5])
                password_label.set(row[0][6])
                address_label.set(row[0][7])
                desig_label.set(row[0][8])
                email_label.set(row[0][9])
                global em
                em=row[0][9]
                print(em)
                p=row[0][6]
            
            
            
            app_width=700
            app_height=500
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame2=Frame(root,bg="white")
            frame2.place(x=xcor,y=ycor,width=700,height=500)
            
            l1 = Label(frame2, text="NAME",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l1.place(x=90,y=30)
            e1 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=name_label)
            e1.place(x=90,y=60,width=200)
            
            l2 = Label(frame2, text="CONTACT NO",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l2.place(x=400,y=30)
            e2 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=contact_label)
            e2.place(x=400,y=60,width=200)
            
            l3 = Label(frame2, text="Email",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l3.place(x=90,y=100)
            e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=email_label)
            e3.place(x=90,y=130,width=200)
            
            l4 = Label(frame2, text="PASSWORD",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l4.place(x=400,y=100)
            e4 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=password_label)
            e4.place(x=400,y=130,width=200)
            
            l5 = Label(frame2, text="Address",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l5.place(x=90,y=240)
            e5 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=address_label)
            e5.place(x=90,y=270,width=200)
            
            l6 = Label(frame2, text="Gender",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l6.place(x=400,y=240)
            e7 = Entry(frame2,font=("times new roman",15),bg='lightgray',state='disabled',textvariable=gender_label)
            e7.place(x=400,y=270,width=200)
            #var = IntVar()
            #r1 = Radiobutton(frame2, text="Male", variable=var, value=1, font=("times new roman",15))
            #r1.place(x=400,y=270)
            #r2 = Radiobutton(frame2, text="Female", variable=var, value=2, font=("times new roman",15))
            #r2.place(x=500,y=270)
            
            l7 = Label(frame2, text="DOB",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l7.place(x=90,y=170)
            e8 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=dob_label)
            e8.place(x=90,y=200,width=200)
            #dob = DateEntry(frame2,  bg='lightgray',date_pattern='dd/mm/Y', font=("times new roman",15))
            #dob.place(x=90,y=200,width=200)
            
            l8 = Label(frame2, text="Select designation",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l8.place(x=90,y=310)
            e6 = Entry(frame2,font=("times new roman",15),bg='lightgray',state='disabled',textvariable=desig_label)
            e6.place(x=90,y=340,width=230)
            #svar = StringVar()
            #svar.set("Select designation")
            #option = ("Admin", "Employee", "Supplier")
            #o = OptionMenu(frame2,svar, *option)
            #o.config(font=("times new roman",15),bg='lightgray')
            #o.place(x=90,y=340,width=230)
            
            l9 = Label(frame2, text="DOJ",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l9.place(x=400,y=170)
            e7 = Entry(frame2,font=("times new roman",15),bg='lightgray',state='disabled',textvariable=doj_label)
            e7.place(x=400,y=200,width=200)
            #dob = DateEntry(frame2,  bg='lightgray',date_pattern='dd/mm/Y', font=("times new roman",15))
            #dob.place(x=400,y=200,width=200)
            
            
            def send_otp():
                    user="StoreManagementSystem.SLA@gmail.com"
                    password="smspython"
                    global em
                    to_addrs=em
                    send_otp.otp=str(random.randint(1000,9999))
                    subject="OTP"
                    text="Your otp for Store Management is "+send_otp.otp
                    gmail(user, password, to_addrs, subject, text)
                    print(send_otp.otp)
                    #otp_v = textinput("opt_v", "Please enter your otp:")
                    otp_v = simpledialog.askstring("Input", "enter your opt?",
                                parent=root)
                    if(send_otp.otp==otp_v):
                        save()
                    else:
                        mb.showinfo("eroor","enter corrext otp",parent=root)
                    
                    
            
            def update():
                 mb.showinfo("Success","do you wana update",parent=root)
                 name=name_label.get()
                 dob=dob_label.get()
                 contact=contact_label.get()
                 emailid=email_label.get()
                 address=address_label.get() 
                 passwrd=password_label.get()
                 print(name,email,address,dob,passwrd)
                 global em
                 if(emailid!=em):
                     mb.showinfo("wait","sending otp to old email id",parent=root)
                     send_otp()
                     mb.showinfo("wait","sending otp to new email id",parent=root)
                     user="StoreManagementSystem.SLA@gmail.com"
                     password="smspython"
                     #global em
                     to_addrs=emailid
                     send_otp.otp=str(random.randint(1000,9999))
                     subject="OTP"
                     text="Your otp for Store Management is "+send_otp.otp
                     gmail(user, password, to_addrs, subject, text)
                     print(send_otp.otp)
                    #otp_v = textinput("opt_v", "Please enter your otp:")
                     otp_v = simpledialog.askstring("Input", "enter your opt?",
                                parent=root)
                     if(send_otp.otp==otp_v):
                         save()
                     else:
                        mb.showinfo("eroor","enter corrext otp",parent=root)
                     
                     
                     
                 elif(passwrd!=p):
                     mb.showinfo("wait","sending otp to your email id",parent=root)
                     send_otp()
                     
                     
                 else:
                     save()
                     
                    
                     
                     
                     
            def save():
                 name=name_label.get()
                 dob=dob_label.get()
                 contact=contact_label.get()
                 emailid=email_label.get()
                 address=address_label.get() 
                 passwrd=password_label.get()
                 print(name,email,address,dob,passwrd)
               
                 conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=SIMRAN;'
                     'Database=sm_db;'
                     'Trusted_Connection=yes;')
                 cursor = conn.cursor()
                 cursor.execute("UPDATE members SET f_name= ?,dob = ?,Address=?,password=?,phone=?,Email=? WHERE id = ?",(name,dob,address,passwrd,contact,emailid,idss))
                 conn.commit()
                 print("Data updated successfully")
                 mb.showinfo("Success","confirmation to admin",parent=root)
                 user="StoreManagementSystem.SLA@gmail.com"
                 password="smspython"
                 to_addrs=str(emailid)
                 subject="details updated"
                 text="Your "+idss+"name"+name+"succesfully updated profile information "
                 gmail(user, password, to_addrs, subject, text)
               
                 
            def back():
                 #root.destroy()
                 #import sms_employee_page    
                  from sms_employee_page import take_idfromlogin
                  take_idfromlogin(ids=idss,email_v=email,mains=False)
                  root.destroy()
                  take_idfromlogin(ids=idss,email_v=email,mains=True)    
            
            b1 = Button(frame2, text='UPDATE',width=10,bg='green',fg='white',font=("times new roman",15,"bold"),command=update)
            b1.place(x=150,y=400)
            #b2 = Button(frame2, text='Reject',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"))
            #b2.place(x=400,y=400)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650) 
            
            
            root.mainloop()