import tkinter.messagebox as mb
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk


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
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("")
            root.configure(background = "white")
                        
            #'''''bg image''''''
            bgimg=ImageTk.PhotoImage(file="sms.jpg")
            bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)
            
            app_width=700
            app_height=550
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=700,height=550)
            l1 = Label(frame1, text="WELCOME TO EMPLOYEE PAGE",font=("times new roman",20,"bold"),bg='white',fg='green')
            l1.place(x=150,y=10)
            def billing():
                 #root.destroy()
                 #import sms_billing_system
                  from sms_billing_system import take_id
                  take_id(idss=ids,email=email_v,mains=False)
                  root.destroy()
                  take_id(idss=ids,email=email_v,mains=True)
            
            def supllier():
                        #root.destroy()
                       # import supllier_d
                        from supllier_d import take_id
                        take_id(idss=ids,email=email_v,mains=False)
                        root.destroy()
                        take_id(idss=ids,email=email_v,mains=True)
                        
            def profile():
                        #root.destroy()
                       # import supllier_d
                        from sms_profile import take_id
                        take_id(idss=ids,email=email_v,mains=False)
                        root.destroy()
                        take_id(idss=ids,email=email_v,mains=True)             
            def back():
                  root.destroy()
                  import sms_signup_page                
            
            
            b1 = Button(frame1, text='Change Profile Details',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=profile)
            b1.place(x=220,y=110)
            b2 = Button(frame1, text='Billing Desk',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=billing)
            b2.place(x=220,y=180)
            b3 = Button(frame1, text='Supplier Details',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=supllier)
            b3.place(x=220,y=250)
            #b4 = Button(frame1, text='Dashboard',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b4.place(x=220,y=250)
            #b5 = Button(frame1, text='View Super Sale Offer',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b5.place(x=220,y=320)
            #b6 = Button(frame1, text='Scan Products',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b6.place(x=220,y=390)
            #b7 = Button(frame1, text='Seen FeedBack To Admin ',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b7.place(x=220,y=460)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650)
            
            
            root.mainloop()