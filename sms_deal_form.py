from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import random
from mail import gmail
import pyodbc
import datetime
from datetime import date
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk
from tkinter import ttk
import cv2

mains=False
if mains==True:
    print("File one excuted when ran directly")
else:
    def take_id(idss,email,mains):
        s_id=idss
        print(idss)
        m=mains
        if m==True:
            print("File one excuted when ran directly")
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            # root.geometry('1350x700+0+0')
            root.title("Registration Form")
            root.configure(background="white")
            
            '''bg image'''
           # bgimg=ImageTk.PhotoImage(file="img/stores.jpeg")
            #bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)
            
            todays_date=date.today()
            now = todays_date.strftime("%m/%d/%y")
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')
        
        
        
            
            #defining function msg() using messagebox
            def msg():
                msg.flag=0
                error_msg=""
                if (e1.index("end") == 0):
                    error_msg="Product Name \n"
                    msg.flag+=1
                if(e2.index("end") == 0):
                    error_msg=error_msg+"Brand Name\n"
                    msg.flag+=1
                if(e3.index("end") == 0 ):
                    error_msg=error_msg+"MRP\n"
                    msg.flag+=1
                if(e4.index("end") == 0):
                    error_msg=error_msg+"Price\n"
                    msg.flag+=1
                if(e5.index("end") == 0):
                    error_msg=error_msg+"Quantity.\n"
                    msg.flag+=1
                if(e6.index("end") == 0):
                    error_msg=error_msg+"Volume\n"
                    msg.flag+=1
                if(e7.index("end") == 0):
                    error_msg=error_msg+"Expiry\n"
                    msg.flag+=1
                if(n.get()==""):
                    error_msg=error_msg+"Category"
                    msg.flag+=1
                if(click.flag2==False and click.pid==""):
                    error_msg=error_msg+"Product Image"
                    msg.flag+=1
                # if((-dob.get_date())<18):
                #     error_msg=error_msg+"age should be greater than 18\n"
                #     msg.flag+=1
                # if((date.today()-dob.get_date())>80):
                #     error_msg=error_msg+"age should be smaller than 80\n"
                #     msg.flag+=1
                if msg.flag!=0:
                    mb.showwarning('Missing details', "Enter the value of \n"+error_msg)
            
            
            def click():
                click.pid=str(random.randint(100000,999999))
                path=f"img/{click.pid}.jpg"
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                mb.showinfo("camera","c for capture, q for quit")
                while(result):
                    ret,frame = videoCaptureObject.read()
                    cv2.putText(frame, click.pid, (50,400), cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
                    cv2.imshow("text detection",frame)
                    if(cv2.waitKey(2)&0xFF==ord('c')):
                        cv2.imwrite(path,frame)
                        click.flag2=True
                        result = False
                    elif(cv2.waitKey(2)&0xFF==ord('q')):
                        click.flag2=True
                        result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
            click.pid=""
            click.flag2=False
            
            #exporting entered data
            def save():
                if(msg.flag==0):
                    pname=e1.get()
                    bname=e2.get()
                    mrp=e3.get()
                    price=e4.get()
                    qty=e5.get()
                    vol=e6.get()
                    exp=e7.get()
                    cat=n.get()
                    pic=click.pid
                    d_id=str(random.randint(100000,999999))
                    authentication='false'
                    print(d_id,cat,bname,pname,price,qty,authentication,mrp,exp,s_id,now,click.pid,vol)
                    mb.showinfo("Process","Please wait....")
                    user="StoreManagementSystem.SLA@gmail.com"
                    password="smspython"
                    to_addrs=email
                    subject="Applied for a deal"
                    text="Hello You are Applied a deal for \nCategory: "+cat+"\nProduct name: "+pname+"\nBrand name: "+bname+"\nprice:"+price+"\nThank you"
                    print(user,password)
                    gmail(user, password, to_addrs, subject, text)
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO deal VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(d_id,cat,bname,pname,price,qty,authentication,mrp,exp,s_id,now,click.pid,vol))
                    conn.commit()
                    print("Data saved successfully")
                    mb.showinfo("Information", "Data Saved successfully")
                    mb.showinfo("Information", "Informing admin about your deal")
                    print("Informing admin about your deal")
                    rid=str(random.randint(10000, 99999))
                    desc="New deal for"+pname+" of "+bname
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Requests VALUES(?,?,?,?)",(rid,d_id,desc,now))
                    conn.commit()
                    mb.showinfo("Information", "congrats your deal submitted")
            def saveinfo():
                msg()
                if(msg.flag==0):
                        save()
                        root.destroy()
                        from sms_supplier_page import take_idfromlogin
                        take_idfromlogin(ids=s_id,email_v=email,mains=True)
                        
                   
            def back():
                # root.destroy()
                 #import sms_admin_page
                  from sms_supplier_page import take_idfromlogin
                  take_idfromlogin(ids=idss,email_v=email,mains=False)
                  root.destroy()
                  take_idfromlogin(ids=idss,email_v=email,mains=True)
             
            # creating frames,labels and entry widgets
            app_width=700
            app_height=600
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=700,height=600)
            l1 = Label(frame1, text="DEAL HERE",font=("times new roman",20,"bold"),bg='white',fg='green')
            l1.place(x=240,y=30)
            
            l2 = Label(frame1, text="Product Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l2.place(x=90,y=80)
            e1 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e1.place(x=90,y=120,width=230)
            
            l3 = Label(frame1, text="Brand Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l3.place(x=400,y=80)
            e2 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e2.place(x=400,y=120,width=230)
            
            l4 = Label(frame1, text="MRP",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l4.place(x=90,y=170)
            e3 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e3.place(x=90,y=210,width=230)
            
            l7 = Label(frame1, text="Price",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l7.place(x=400,y=170)
            e4 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e4.place(x=400,y=210,width=230)
            
            l6 = Label(frame1, text="Quantity",  font=("times new roman",15,"bold"),bg='white',fg='gray')
            l6.place(x=90,y=260)
            e5 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e5.place(x=90,y=300,width=230)
            
            l5 = Label(frame1, text="Volume",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l5.place(x=400,y=260)
            e6 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e6.place(x=400,y=300,width=230)
            
            
            l8 = Label(frame1, text="Expiry in mm/yyyy",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l8.place(x=90,y=350)
            e7 = Entry(frame1,font=("times new roman",15),bg='lightgray')
            e7.place(x=90,y=390,width=230)
            
            l10 = Label(frame1, text="Category",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l10.place(x=400,y=350)
            
            n = StringVar()
            # monthchoosen.current(1) 
            customerName = StringVar()
            customerName.set("")
            customerName.set("Select Category")
            products=['Milk','Chips','Rice','Choclate','Cold Drink','Icecream','Kurkure', 'Water','Daal', 'Sugar', 'Salt', 'Biscuit',"medical",]
            customer_name_entry = AutocompleteCombobox(frame1,width=20, completevalues=products,textvariable = n)
            customer_name_entry.place(x=400,y=390,width=230)
            
            
            
            
            l9 = Label(frame1, text="Image of product",font=("times new roman",15,"bold"),bg='white',fg='gray')
            l9.place(x=90,y=430)
            b1 = Button(frame1, text='product image',width=10,command=click,bg='white',fg='gray',font=("times new roman",15,"bold"))
            b1.place(x=90,y=470)
            
            # l9 = Label(frame1, text="Image of expiry",font=("times new roman",15,"bold"),bg='white',fg='gray')
            # l9.place(x=400,y=430)
            # b2 = Button(frame1, text='Expiry image',width=10,command=saveinfo,bg='white',fg='gray',font=("times new roman",15,"bold"))
            # b2.place(x=400,y=470)
           
    
           
            # submit and cancel buttons
            b3 = Button(frame1, text='Submit',width=10,command=saveinfo,bg='green',fg='white',font=("times new roman",15,"bold"))
            b3.place(x=100,y=550)
            b4 = Button(frame1, text='Cancel',width=10,command=root.destroy,bg='maroon',fg='white',font=("times new roman",15,"bold"))
            b4.place(x=460,y=550)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650)


                
            
            
            root.mainloop()
        else:
            print("File deal imported but not excuted")
                    
                    
