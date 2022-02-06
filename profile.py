# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:39:48 2021

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
#        print(s_id)
        m=mains
        if m==True:
            print("File one excuted when ran directly")
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("Store Management System")
            root.configure(background="white")
            
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')
                
            
            global btn
            global idd
            global email_l
            global pasid
            global did
            global price
            global stock
            global sid
            global ct,brand
            btn="empty"
            id_label=tk.StringVar()
            name_label=tk.StringVar()
            email_label=tk.StringVar()
            contact_label=tk.StringVar()
            dob_label=tk.StringVar()
            doj_label=tk.StringVar()
            address_label=tk.StringVar()
            gender_label=tk.StringVar()
            desig_label=tk.StringVar()
            idd=tk.IntVar()
            did=tk.IntVar()
            pasid=tk.StringVar()
            product_label=tk.StringVar()
            brand_label=tk.StringVar()
            supplier_label=tk.StringVar()
            category_label=tk.StringVar()
            expiry_label=tk.StringVar()
            volume_label=tk.StringVar()
            quantity_label=tk.StringVar()
            price_label=tk.StringVar()
            mrp_label=tk.StringVar()
            stock=tk.StringVar()
            price=tk.IntVar()
            sid=tk.IntVar()
            todays_date=date.today()
            now = todays_date.strftime("%m/%d/%y")
            
            #user="StoreManagementSystem.SLA@gmail.com"
            #password="smspython"
            #to_addrs=str(email_label)
            
            
            
            #a=idd
            #print("a is",a)
            
            def selection():
                pass
                   # i = title_tabel.focus()
                    #for a in i:
                        #print("selected item is ",i(values))
                    #print(title_tabel.item(i)) 
                     #print(title_tabel.item(i))
                     
            def select_item(b):
                values=title_tabel.item(title_tabel.selection())
                print(values)
                rid=values["values"]
                if(btn=="user"):
                    cur=conn.cursor()
                    cur.execute("Select * from members where id=(SELECT id FROM Requests where r_id=?)",(rid[0]))
                    row=cur.fetchall()
                    print(row)
                    print(row[0][0])
                    global pasid
                    pasid=row[0][8]
                    print("pass is",pasid)
                   # print(type(row))
                    #r1 = tuple(row)
                    #print(r1[0])
                    #print(type(r1))
                    #print(r1(len))
                    #e1.setText(row[0][0])
                    #e2.setText(row[0][1])
                    #e3.setText(row[0][1])
                    id_label.set(row[0][0])
                    name_label.set(row[0][1])
                    email_label.set(row[0][6])
                    global email_l
                    email_l=row[0][6]
                    contact_label.set(row[0][5])
                    dob_label.set(row[0][3])
                    doj_label.set(row[0][11])
                    address_label.set(row[0][7])
                    gender_label.set(row[0][4])
                    desig_label.set(row[0][9])
                    global idd
                    idd=row[0][0]
                    print(idd)
                    
                    
             
                
                    
                    
           
        
                elif(btn=="deal"):
                    cur=conn.cursor()
                    cur.execute("Select * from deal where d_id=(SELECT id FROM Requests where r_id=?)",(rid[0]))
                    row=cur.fetchall()
                    print(row)
                    print(row[0][0])
                    global did
                    did=row[0][0]
                    category_label.set(row[0][1])
                    brand_label.set(row[0][2])
                    global ct
                    ct=row[0][1]
                    global brand
                    brand =row[0][2]
                    supplier_label.set(row[0][9])
                    product_label.set(row[0][3])
                    mrp_label.set(row[0][7])
                    price_label.set(row[0][4])
                    quantity_label.set(row[0][5])
                    volume_label.set(row[0][12])
                    expiry_label.set(row[0][8])
                    global stock
                    stock=row[0][5]
                    global price
                    price=row[0][4]
                    print(price)
                    a=(price*0.10)
                    print(a)
                    price=(a+price)
                    #price=str(price)
                    #print("added price is "+price)
                    price=int(price)
                    global sid
                    sid = row[0][9]
                    
                else:
                    print("btn problem",btn)
            
                    
            def remove_item():
                 #selected_items = self.treeview.selection()
                 values=title_tabel.selection()
                 for i in values:          
                        title_tabel.delete(values)        
                
            def reject():
                conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=SIMRAN;'
                     'Database=sm_db;'
                     'Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute("DELETE from Requests WHERE id = ?",(idd))
                cursor.execute("DELETE from members WHERE id = ?",(idd))
                conn.commit()
                remove_item()
                print("remove succesfully")
                
            def cancel():
                conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=SIMRAN;'
                     'Database=sm_db;'
                     'Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute("DELETE from Requests WHERE id = ?",(did))
                cursor.execute("DELETE from deal WHERE id = ?",(did))
                conn.commit()
                remove_item()
                print("remove succesfully")
                
               
                
            def adddeal():
                conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=SIMRAN;'
                     'Database=sm_db;'
                     'Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute("UPDATE deal SET deal = ? WHERE id = ?",("True",did))
                conn.commit()
                print("Data updated successfully")
                cursor.execute("INSERT INTO sale VALUES(?,?,?,?)",(did,stock,price,now))
                conn.commit()
                print("Data saved successfully in sale")
                print(sid)
                cur=conn.cursor()
                cur.execute("select Email from members where id = ?",(sid))
                row=cur.fetchone()
                conn.commit()
                print(row)
                add=row[0]
                
                user="StoreManagementSystem.SLA@gmail.com"
                password="smspython"
                to_addrs=str(add)
                
                   
                subject="Verification for dael  By Store"
                text="Your deal for "+str(ct)+str(brand)+"at price"+str(price)+"is accepted by Store Management"
                gmail(user, password, to_addrs, subject, text)
                cursor = conn.cursor()
                cursor.execute("DELETE from Requests WHERE id = ?",(did))
                conn.commit()
                remove_item()
                
                
                
            def allow():
                print("yo id is",idd) 
                conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=SIMRAN;'
                     'Database=sm_db;'
                     'Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute("UPDATE members SET authenticated = ? WHERE id = ?",("True",idd))
                conn.commit()
                print("Data updated successfully")
                mb.showinfo("Success","member will get a mail about his id, password soon",parent=root)
                
                #print(user,password,to_addrs)
                idn=str(idd)
                p=str(pasid)
                
        
                user="StoreManagementSystem.SLA@gmail.com"
                password="smspython"
                to_addrs=str(email_l)
                
                   
                subject="your Are Verified By Store"
                text="Your id for Store Management is "+idn+"password is"+p
                gmail(user, password, to_addrs, subject, text)
                cursor = conn.cursor()
                cursor.execute("DELETE from Requests WHERE id = ?",(idd))
                conn.commit()
                remove_item()
                
                    
                # for item in title_tabel.selection():
                #      it=title_tabel.item(item,"text") 
                #      print(it)
        
            # b3 = Button(root, text='print',width=10,bg='green',fg='white',font=("times new roman",15,"bold"),command=on_tree_selection)
            # b3.place(x=600,y=230)
            
            
            '''bg image'''
            #bgimg=ImageTk.PhotoImage(file="img/stores.jpeg")
            #bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)
            
            app_width=700
            app_height=760
            xcor=(root.winfo_screenwidth()/2)-(app_width/2)
            ycor=(root.winfo_screenheight()/2)-(app_height/2)
            frame1=Frame(root,bg="white")
            frame1.place(x=xcor,y=ycor,width=700,height=250)
            
            
            title_frame = Label(frame1, text="Requests", 
                                    font=("times new roman", 20, "bold"),bg = "white", fg="gray")
            title_frame.pack(side=TOP,fill="x")
                
            title_tabel_frame = Frame(frame1)
            title_tabel_frame.place(x=0,y=40,height=200,width=700)
                
            scrollbar_order_x = Scrollbar(title_tabel_frame ,orient=HORIZONTAL)
            scrollbar_order_y = Scrollbar(title_tabel_frame ,orient=VERTICAL)
                
            title_tabel = ttk.Treeview(title_tabel_frame,
            columns =("id","name","description","date"),xscrollcommand=scrollbar_order_x.set,
            yscrollcommand=scrollbar_order_y.set)
                
            title_tabel.heading("id",text="Request Id")
            title_tabel.heading("name",text="Name")
            title_tabel.heading("description",text="Description")
            title_tabel.heading("date",text="Date")
            title_tabel["displaycolumns"]=("id","name", "description","date")
            title_tabel["show"] = "headings"
            title_tabel.column("date",width=150,anchor='center', stretch=NO)
            title_tabel.column("id",width=100,anchor='center', stretch=NO)
            title_tabel.column("name",width=150,anchor='center', stretch=NO)
            title_tabel.column("description",width=300,anchor='center', stretch=NO)
            title_tabel.bind('<ButtonRelease-1>',select_item)
                
                
            scrollbar_order_x.pack(side=BOTTOM,fill=X)
            scrollbar_order_y.pack(side=RIGHT,fill=Y)
                
            scrollbar_order_x.configure(command=title_tabel.xview)
            scrollbar_order_y.configure(command=title_tabel.yview)
                
            title_tabel.pack(fill=BOTH,expand=1)
            
            
            
            def DEALS():
                for i in title_tabel.get_children():
                    title_tabel.delete(i)
                global btn
                btn="deal"
                print("deal")
                app_width=700
                app_height=240
                xcor=(root.winfo_screenwidth()/2)-(app_width/2)
                ycor=(root.winfo_screenheight()/2)-(app_height/2)
                frame2=Frame(root,bg="white")
                frame2.place(x=xcor,y=ycor,width=700,height=450)
                
                l1 = Label(frame2, text="Category",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l1.place(x=90,y=30)
                e1 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=category_label,justify='center')
                e1.place(x=90,y=60,width=200)
                
                l2 = Label(frame2, text="Supplier ID",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l2.place(x=400,y=30)
                e2 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=supplier_label,justify='center')
                e2.place(x=400,y=60,width=200)
                
                l3 = Label(frame2, text="Brand Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l3.place(x=90,y=100)
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=brand_label,justify='center')
                e3.place(x=90,y=130,width=200)
                
                l4 = Label(frame2, text="Product Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l4.place(x=400,y=100)
                e4 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=product_label,justify='center')
                e4.place(x=400,y=130,width=200)
                
                l7 = Label(frame2, text="MRP",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l7.place(x=90,y=170)
                dob = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=mrp_label,justify='center')
                dob.place(x=90,y=200,width=200)
                
                l9 = Label(frame2, text="Price",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l9.place(x=400,y=170)
                doj = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=price_label,justify='center')
                doj.place(x=400,y=200,width=200)
                
                l5 = Label(frame2, text="Quantity",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l5.place(x=90,y=240)
                e5 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=quantity_label,justify='center')
                e5.place(x=90,y=270,width=200)
                
                l6 = Label(frame2, text="Volume",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l6.place(x=400,y=240)
                var = IntVar()
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=volume_label,justify='center')
                e3.place(x=400,y=270,width=200)
                
                
                
                l8 = Label(frame2, text="Expiry",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l8.place(x=90,y=310)
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=expiry_label,justify='center')
                e3.place(x=90,y=340,width=200)
                
                
                
                b1 = Button(frame2, text='Allow',width=10,bg='green',fg='white',font=("times new roman",15,"bold"),command=adddeal)
                b1.place(x=150,y=400)
                b2 = Button(frame2, text='Reject',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"),command=cancel)
                b2.place(x=400,y=400)
                
                
                cur=conn.cursor()
                cur.execute("SELECT Requests.r_id,(members.f_name+' '+members.l_name) as name ,Requests.description,Requests.date FROM Requests,deal,members where Requests.id=deal.d_id and deal.id=members.id;")
                row=cur.fetchall()
                for dt in row:
                    title_tabel.insert("",'end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3]))
                
                
            
            def USERS():
                
                for i in title_tabel.get_children():
                    title_tabel.delete(i)
                global btn
                btn="user"
                print("user")
                app_width=700
                app_height=240
                xcor=(root.winfo_screenwidth()/2)-(app_width/2)
                ycor=(root.winfo_screenheight()/2)-(app_height/2)
                frame2=Frame(root,bg="white")
                frame2.place(x=xcor,y=ycor,width=700,height=450)
                
                l1 = Label(frame2, text="Id",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l1.place(x=90,y=30)
                e1 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable = id_label,justify='center')
                e1.place(x=90,y=60,width=200)
                
                l2 = Label(frame2, text="Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l2.place(x=400,y=30)
                e2 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable = name_label,justify='center')
                e2.place(x=400,y=60,width=200)
                
                l3 = Label(frame2, text="Email",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l3.place(x=90,y=100)
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable = email_label,justify='center')
                e3.place(x=90,y=130,width=200)
                
                l4 = Label(frame2, text="Contact No.",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l4.place(x=400,y=100)
                e4 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable = contact_label,justify='center')
                e4.place(x=400,y=130,width=200)
                
                l5 = Label(frame2, text="Address",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l5.place(x=90,y=240)
                e5 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=address_label,justify='center')
                e5.place(x=90,y=270,width=200)
                
                l6 = Label(frame2, text="Gender",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l6.place(x=400,y=240)
                var = IntVar()
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=gender_label,justify='center')
                e3.place(x=400,y=270,width=200)
                
                l7 = Label(frame2, text="DOB",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l7.place(x=90,y=170)
                dob = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=dob_label,justify='center')
                dob.place(x=90,y=200,width=200)
                
                l8 = Label(frame2, text="Designation",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l8.place(x=90,y=310)
                e3 = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=desig_label,justify='center')
                e3.place(x=90,y=340,width=200)
                
                l9 = Label(frame2, text="DOJ",font=("times new roman",15,"bold"),bg='white',fg='gray')
                l9.place(x=400,y=170)
                doj = Entry(frame2,font=("times new roman",15),bg='lightgray',textvariable=doj_label,justify='center')
                doj.place(x=400,y=200,width=200)
                
                b1 = Button(frame2, text='Allow',width=10,bg='green',fg='white',font=("times new roman",15,"bold"),command=allow)
                b1.place(x=150,y=400)
                b2 = Button(frame2, text='Reject',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"),command=reject)
                b2.place(x=400,y=400)
                
                
                
                cur=conn.cursor()
                cur.execute("SELECT Requests.r_id,(members.f_name+' '+members.l_name) as name,Requests.description,Requests.date FROM Requests INNER JOIN members ON Requests.id=members.id;")
                row=cur.fetchall()
                for dt in row:
                    title_tabel.insert("",'end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3]))
               
                
                
            def back():
                # root.destroy()
                 #import sms_admin_page
                  from sms_admin_page import take_idfromlogin
                  take_idfromlogin(ids=idss,email_v=email,mains=False)
                  root.destroy()
                  take_idfromlogin(ids=idss,email_v=email,mains=True)
            
            
            b1 = Button(root, text='USER',width=10,bg='green',fg='white',font=("times new roman",15,"bold"),command=USERS)
            b1.place(x=600,y=10)
            b2 = Button(root, text='DEALS',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"),command=DEALS)
            b2.place(x=800,y=10)
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=650)
            
            root.mainloop()
        else:
            print("File one ecuted when imported")