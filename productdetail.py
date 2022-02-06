# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:43:25 2021

@author: Simran-pc
"""


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
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("Store Management System")
            root.configure(background="white")
            
            
            
            app_width=1000
            app_height=750
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=1000,height=550)
                        
                        
            title_frame = Label(frame1, text="PRODUCTS DETAILS", 
            font=("times new roman", 20, "bold"),bg = "white", fg="gray")
            title_frame.pack(side=TOP,fill="x")
                            
            title_tabel_frame = Frame(frame1)
            title_tabel_frame.place(x=0,y=60,height=500,width=1000)
                            
            scrollbar_order_x = Scrollbar(title_tabel_frame ,orient=HORIZONTAL)
            scrollbar_order_y = Scrollbar(title_tabel_frame ,orient=VERTICAL)
                            
            title_tabel = ttk.Treeview(title_tabel_frame,
            columns =("id","name","stock","category","brand","price","volume","expiry","dod"),xscrollcommand=scrollbar_order_x.set,
                        yscrollcommand=scrollbar_order_y.set)
                            
            title_tabel.heading("id",text="Id")
            title_tabel.heading("name",text="Name")
            title_tabel.heading("stock",text="stock")
            title_tabel.heading("category",text="category")
            title_tabel.heading("brand",text="brand")
            title_tabel.heading("price",text="price")
            title_tabel.heading("volume",text="volume")
            title_tabel.heading("expiry",text="expiry")
            title_tabel.heading("dod",text="dod")
            title_tabel["displaycolumns"]= ("id","name","stock","category","brand","price","volume","expiry","dod")
            title_tabel["show"] = "headings"
            
            title_tabel.column("id",width=111,anchor='center', stretch=NO)
            title_tabel.column("name",width=111,anchor='center', stretch=NO)
            title_tabel.column("stock",width=111,anchor='center', stretch=NO)
            title_tabel.column("category",width=111,anchor='center', stretch=NO)
            title_tabel.column("brand",width=111,anchor='center', stretch=NO)
            title_tabel.column("price",width=111,anchor='center', stretch=YES)
            title_tabel.column("volume",width=111,anchor='center', stretch=NO)
            title_tabel.column("expiry",width=111,anchor='center', stretch=NO)
            title_tabel.column("dod",width=111,anchor='center', stretch=NO)
            #title_tabel.bind('<ButtonRelease-1>',select_item)
                            
                            
            scrollbar_order_x.pack(side=BOTTOM,fill=X)
            scrollbar_order_y.pack(side=RIGHT,fill=Y)
                            
            scrollbar_order_x.configure(command=title_tabel.xview)
            scrollbar_order_y.configure(command=title_tabel.yview)
                            
            title_tabel.pack(fill=BOTH,expand=1)
            
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=SIMRAN;'
                                  'Database=sm_db;'
                                  'Trusted_Connection=yes;')
            cur=conn.cursor()
            #cur.execute("select id,(f_name+' '+l_name) as name,dob,gender,phone,Email,designation,password,doj  from members where  authenticated=?",("True"))
            cur.execute("SELECT sale.d_id,deal.product_name,sale.Avail,deal.category,deal.brand_name,sale.s_price,deal.vol,deal.expiry,sale.date FROM sale INNER JOIN deal ON sale.d_id=deal.d_id;")
            row=cur.fetchall()
            for dt in row:
                title_tabel.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8]))   
                
                
                
            def back():
                #root.destroy()
                 #import sms_admin_page
                  from sms_admin_page import take_idfromlogin
                  take_idfromlogin(ids=idss,email_v=email,mains=False)
                  root.destroy()
                  take_idfromlogin(ids=idss,email_v=email,mains=True)
            
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650)   
            #b1 = Button(root, text='USER',width=10,bg='green',fg='white',font=("times new roman",15,"bold"))
            #b1.place(x=600,y=550)    
            root.mainloop()
                        
            