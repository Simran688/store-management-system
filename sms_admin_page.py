import tkinter.messagebox as mb
from tkinter import *
import tkinter as tk


mains=False
if mains==True:
    print("File one excuted when ran directly")
else:
    def take_idfromlogin(ids,email_v,mains):
        take_idfromlogin.s_id=ids
        print(ids)
        m=mains
        if m==True:
            print("File one excuted when ran directly")

            #root = Tk()
            #app_width=400
            #app_height=400
            #x=(root.winfo_screenwidth()/2)-(app_width/2)
            #y=(root.winfo_screenheight()/2)-(app_height/2)
            #root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            #root.title("")
            #root.configure(background = "pink");
            
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("")
            root.configure(background = "white")

            #'''''bg image''''''
            #bgimg=ImageTk.PhotoImage(file="stores.jpg")
            #bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)

            app_width=700
            app_height=600
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=700,height=600)
            
            l1 = Label(frame1, text="WELCOME TO ADMIN PAGE",font=("times new roman",20,"bold"),bg='white',fg='green')
            l1.place(x=150,y=10)
            
            def request():
                from sms_request import take_id
                take_id(idss=ids,email=email_v,mains=False)
                root.destroy()
                take_id(idss=ids,email=email_v,mains=True)
            
            
            def employee():
                from employeedetail import take_id
                take_id(idss=ids,email=email_v,mains=False)
                root.destroy()
                take_id(idss=ids,email=email_v,mains=True)  
                
                
            def product():
                from productdetail import take_id
                take_id(idss=ids,email=email_v,mains=False)
                root.destroy()
                take_id(idss=ids,email=email_v,mains=True)  
            def back():
                 root.destroy()
                 import sms_signup_page
                
           # b1 = Button(frame1, text='Generate Report',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b1.place(x=220,y=40)
            b2 = Button(frame1, text='Add New Employee/deal',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=request)
            b2.place(x=220,y=110)
            b3 = Button(frame1, text='See members Details',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=employee)
            b3.place(x=220,y=180)
            b4 = Button(frame1, text='Products detils',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=product)
            b4.place(x=220,y=250)
            b5 = Button(frame1, text='See Sale',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            b5.place(x=220,y=320)
           # b6 = Button(frame1, text='Compare Sale',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b6.place(x=220,y=390)
           # b7 = Button(frame1, text='See Supplier Details',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
           # b7.place(x=220,y=460)
           # b8 = Button(frame1, text='See Stocks',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b8.place(x=220,y=530)
            b9 = Button(frame1, text='Send Message To Employees',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            b9.place(x=220,y=600)
            #Button(root, text='Generate Report',width=20,bg='red',fg='white').place(x=130,y=30)
           # Button(root, text='requests',width=20,bg='red',fg='black',command=request).place(x=130,y=70)
           # Button(root, text='See Employee Details',width=20,bg='red',fg='black').place(x=130,y=110)
           # Button(root, text='See Products',width=20,bg='red',fg='black').place(x=130,y=150)
           # Button(root, text='See Sale',width=20,bg='red',fg='black').place(x=130,y=190)
           # Button(root, text='Compare Sale',width=20,bg='red',fg='black').place(x=130,y=230)
           # Button(root, text='See Supplier Details',width=20,bg='red',fg='black').place(x=130,y=270)
           # Button(root, text='See Stocks',width=20,bg='red',fg='black').place(x=130,y=310)
           # Button(root, text='profile',width=25,bg='red',fg='black').place(x=110,y=350)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command= back)
            backbutton.place(x=1190,y=650)
            
            root.mainloop()
        else:
            print("File one ecuted when imported")
