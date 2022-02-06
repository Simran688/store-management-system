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
            #root = Tk()
            #app_width=400
            #app_height=400
            #x=(root.winfo_screenwidth()/2)-(app_width/2)
            #y=(root.winfo_screenheight()/2)-(app_height/2)
            #root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            #root.title("Supplier")
            #root.configure(background = "pink");
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("")
            root.configure(background = "white")

            #'''''bg image''''''
            #bgimg=ImageTk.PhotoImage(file="sms.jpg")
            #bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)

            app_width=700
            app_height=450
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=700,height=450)
            s_id=StringVar()
             
            l1 = Label(frame1, text="WELCOME TO SUPPLIER PAGE",font=("times new roman",20,"bold"),bg='white',fg='green')
            l1.place(x=150,y=20)
            
            def deal():
                from sms_deal_form import take_id
                take_id(idss=ids,email=email_v,mains=False)
                root.destroy()
                take_id(idss=ids,email=email_v,mains=True)
            def back():
                 root.destroy()
                 import sms_signup_page
                 
            def profile():
                from sms_profilesup import take_id
                take_id(idss=ids,email=email_v,mains=False)
                root.destroy()
                take_id(idss=ids,email=email_v,mains=True)         
                
            #b1=Button(root, text='New deal',command=deal, width=20, bg='red', fg='white').place(x=130,y=60)
            #Button(root, text='renew deal', width=20, bg='red', fg='black').place(x=130,y=100)
            #Button(root, text='profile',width=20,bg='red',fg='black').place(x=130,y=140)
            # Button(root, text='See All Products According To Brand',width=30,bg='red',fg='black').place(x=100,y=180)
            # Button(root, text='Send Feedbacs To Employee',width=25,bg='red',fg='black').place(x=110,y=220)
            b1 = Button(frame1, text='profile',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=profile)
            b1.place(x=220,y=100)
            b2 = Button(frame1, text='Add Products',width=20,bg='green',fg='white',font=("times new roman",15,"bold"),command=deal)
            b2.place(x=220,y=150)
            #b3 = Button(frame1, text='Update Prices',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b3.place(x=220,y=180)
            #b4 = Button(frame1, text='See All Products According To Brand',width=30,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b4.place(x=170,y=250)
            #b5 = Button(frame1, text='Send Feedbacs To Employees',width=20,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b5.place(x=220,y=320)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650)

            root.mainloop()
        else:
            print("File one ecuted when imported")


