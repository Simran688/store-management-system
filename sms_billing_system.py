from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
import time
import pyodbc
#import tk
import tkinter.messagebox as mb  
from tkinter.messagebox import askyesno, askquestion
from ttkwidgets.autocomplete import AutocompleteCombobox
import datetime
from datetime import date

# mains=False
# if mains==True:
#     print("File one excuted when ran directly")
# else:
#     def take_id(idss,email,mains):
#         take_id.s_id=idss
#         print(idss)
#         m=mains
#         if m==True:
            
            
            
mains=False
if mains==True:
    print("File one excuted when ran directly")
else:
    def take_id(idss,email,mains):
        take_id.s_id=idss
        print(idss)
        m=mains
        if m==True:            
            print("File one excuted when ran directly")
            root = Tk()
            root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
            root.title("Store Management System")
            root.state('zoomed')
            
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')
            
            itemName = StringVar()
            itemRate = IntVar()
            itemQuantity = IntVar()
            itemVolume=StringVar()
            totalPrice=IntVar()
            menuCategory = StringVar()
            menuCategory2=StringVar()
            todays_date=date.today()
            now = todays_date.strftime("%m/%d/%y")
            global order_S,item_id
            order_S=0
            item_id=0
            
            
            
            def showall():
                for i in menu_tabel.get_children():
                    menu_tabel.delete(i)
                cur=conn.cursor()
                cur.execute('SELECT deal.brand_name,deal.product_name,sale.s_price,deal.vol,deal.category,sale.d_id FROM sale INNER JOIN deal ON deal.d_id=sale.d_id and Avail>0;')
                row=cur.fetchall()
                sno=0
                for dt in row:
                    sno+=1
                    menu_tabel.insert("",'end',iid=sno,values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],sno))
            
            def show():
                for i in menu_tabel.get_children():
                    menu_tabel.delete(i)
                cur=conn.cursor()
                cur.execute('SELECT deal.brand_name,deal.product_name,sale.s_price,deal.vol,deal.category,sale.d_id FROM sale INNER JOIN deal ON deal.d_id=sale.d_id and Avail>0 where   deal.category=? or deal.product_name=?',(str(menuCategory.get()),str(menuCategory2.get())))
                menuCategory2.set("")
                menuCategory.set("")
                row=cur.fetchall()
                sno=0
                for dt in row:
                    sno=1+sno
                    menu_tabel.insert("",'end',iid=sno,values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],sno))
                            
            
            
            def totalamt():
                length=len(order_tabel.get_children())
                totalamount=0
                for i in range(1,length+1):
                    td=order_tabel.item(i)
                    print(td)
                    rid=td["values"]
                    totalamount+=rid[5]
                totalPrice.set(totalamount)
            
            
            def select_item(b):
                values=menu_tabel.item(menu_tabel.selection())
                print(values)
                rid=values["values"]
                print(rid)
                itemName.set(rid[0]+" "+rid[1])
                itemRate.set(rid[2])
                itemQuantity.set("1")
                itemVolume.set(rid[3])
                global item_id
                item_id=rid[5]
                print(item_id)
            
            def select_item_order(b):
                values=order_tabel.item(order_tabel.selection())
                print(values)
                rid=values["values"]
                
                itemName.set(rid[1])
                itemRate.set(rid[3])
                itemQuantity.set(str(rid[4]))
                itemVolume.set(rid[2])
                global item_id
                item_id=rid[6]
            
            def additem():
                length=len(order_tabel.get_children())
                print(length)
                d_id=""
                global order_S,item_id
                if length:
                    for i in range(1,length+1):
                        td=order_tabel.item(i)
                        print(td)
                        rid=td["values"]
                        print(rid[1]+" "+str(item_name.get()))
                        if rid[1]==str(item_name.get()):
                            mb.showerror("error",f"Already in order list\nAt Serial number {rid[0]}",parent=root)
                            break
                    else:
                        #mb.showerror("error","not match",parent=root)
                        price=itemRate.get()*int(itemQuantity.get())
                        print(price)
                        order_S=1+order_S
                        order_tabel.insert("",'end',iid=order_S,values=(order_S,itemName.get(),itemVolume.get(),itemRate.get(),itemQuantity.get(),price,item_id))
                        totalamt()
                            
                else:
                    price=itemRate.get()*int(itemQuantity.get())
                    print(price)
                    order_S=1+order_S
                    order_tabel.insert("",'end',iid=order_S,values=(order_S,itemName.get(),itemVolume.get(),itemRate.get(),itemQuantity.get(),price,item_id))
                    totalamt()
                    #mb.showinfo("Success",order_tabel.size(),parent=root)
            
            
            def removeitem():
                length=len(order_tabel.get_children())
                print(length)
                global item_id
                item_id=0
                found=1
                if length:
                    for i in range(1,length+1):
                        td=order_tabel.item(i)
                        print(td)
                        rid=td["values"]
                        print(rid[1]+" "+str(item_name.get()))
                        if rid[1]==str(item_name.get()):
                            answer = askyesno(title='Confirmation',message=f"Are you sure to remove item {rid[1]}")
                            found=0
                            if answer:
                                #select=order_tabel.focus()
                                order_tabel.item(i, text="",values=(rid[0],"Item removed","0","0","0","0","0"))
                                totalamt()
                                break
                    if found:
                        mb.showerror("error","Item found not in order list",parent=root)
                else:
                    mb.showerror("error","Add items first",parent=root)
                        
            
            
            
            def updateitem():
                length=len(order_tabel.get_children())
                print(length)
                found=1
                global item_id
                if length:
                    for i in range(1,length+1):
                        td=order_tabel.item(i)
                        print(td)
                        rid=td["values"]
                        print(rid[1]+" "+str(item_name.get()))
                        if rid[1]==str(item_name.get()):
                            #mb.showerror("error","Item found in order list",parent=root)
                            found=0
                            #select=order_tabel.focus()
                            price=itemRate.get()*int(itemQuantity.get())
                            order_tabel.item(i, text="",values=(rid[0],itemName.get(),itemVolume.get(),itemRate.get(),itemQuantity.get(),price,item_id))
                            mb.showinfo("Success",f"{rid[1]} Updated",parent=root)
                            totalamt()
                            break
                    if found:
                        mb.showerror("error","Item found not in order list",parent=root)
                else:
                    mb.showerror("error","Add items first",parent=root)
            
            
            def Cancel():
                global order_S
                order_S=0
                for i in order_tabel.get_children():
                    order_tabel.delete(i)
                    
                    
            
            def back():
                #root.destroy()
                #import sms_employee_page    
                 from sms_employee_page import take_idfromlogin
                 take_idfromlogin(ids=idss,email_v=email,mains=False)
                 root.destroy()
                 take_idfromlogin(ids=idss,email_v=email,mains=True)        
                    
            
            
            def bill_button_operation(): 
                ans = tmsg.askquestion("Generate Bill", "Are You Sure to Generate Bill?")
                if ans=="yes":
                    bill = Toplevel()
                    bill.title("Bill")
                    bill.geometry("670x500+300+100")
                    bill_text_area = Text(bill, font=("arial", 12))
                    order_frame1 = Frame(bill, bd=8, bg="white", relief=GROOVE)
                    order_frame1.pack(expand=True ,fill="both",side=LEFT)
                    
                    order_title_label1 = Label(order_frame1, text="Customer Bill", 
                                font=("times new roman", 20, "bold"),bg = "white", fg="black")
                    order_title_label1.pack(side=TOP,fill="x")
                    
                    order_tabel_frame1 = Frame(order_frame1)
                    order_tabel_frame1.place(x=0,y=40,height=350,width=652)
                    
            
                    scrollbar_order_x = Scrollbar(order_tabel_frame1,orient=HORIZONTAL)
                    scrollbar_order_y = Scrollbar(order_tabel_frame1,orient=VERTICAL)
            
                    order_tabel1 = ttk.Treeview(order_tabel_frame1,
                        columns =("S.No","name","Volume","rate","quantity","price","category","d_id"),xscrollcommand=scrollbar_order_x.set,
                        yscrollcommand=scrollbar_order_y.set)
                    order_tabel1.heading("S.No",text="S.No")
                    order_tabel1.heading("name",text="Name")
                    order_tabel1.heading("rate",text="Rate")
                    order_tabel1.heading("quantity",text="Quantity")
                    order_tabel1.heading("price",text="Price")
                    order_tabel1.heading("Volume",text="Volume")
                    order_tabel1["displaycolumns"]=("S.No","name", "Volume","rate","quantity","price")
                    order_tabel1["show"] = "headings"
                    order_tabel1.column("S.No",width=60,anchor='center', stretch=NO)
                    order_tabel1.column("Volume",width=100,anchor='center', stretch=NO)
                    order_tabel1.column("rate",width=100,anchor='center', stretch=NO)
                    order_tabel1.column("quantity",width=100,anchor='center', stretch=NO)
                    order_tabel1.column("price",width=100,anchor='center', stretch=NO)
                    order_tabel1.column("d_id",width=100,anchor='center', stretch=NO)
                    scrollbar_order_x.pack(side=BOTTOM,fill=X)
                    scrollbar_order_y.pack(side=RIGHT,fill=Y)
                    scrollbar_order_x.configure(command=order_tabel1.xview)
                    scrollbar_order_y.configure(command=order_tabel1.yview)
            
                    order_tabel1.pack(fill=BOTH,expand=1)
                    
                    totbill=StringVar()
                    
                    length=len(order_tabel.get_children())
                    print(length)
                    sno=0
                    for i in range(1,length+1):
                        td=order_tabel.item(i)
                        print(td)
                        rid=td["values"]
                        print("table")
                        print(rid)
                        print("table over")
                        sno+=1
                        order_tabel1.insert("",'end',iid=sno,values=(sno,rid[1],rid[2],rid[3],rid[4],rid[5],rid[6]))
                    totbill.set(totalPrice.get())
                    
                    
                    
                    
                    
                    order_tabel_frame2 = Frame(order_frame1)
                    order_tabel_frame2.place(x=0,y=400,height=300,width=652)
                    
                    item_name_label = Label(order_tabel_frame2 , text="Discount", 
                                font=("arial", 12, "bold"), fg="black")
                    item_name_label.grid(row=0,column=0)
            
                    item_name = Entry(order_tabel_frame2 , font="arial 12",state=DISABLED, width=20)
                    item_name.grid(row=0,column=1,padx=10)
                    
                    item_name_label1 = Label(order_tabel_frame2 , text="Total Discount", 
                                font=("arial", 12, "bold"), fg="black")
                    item_name_label1.grid(row=0,column=2)
            
                    item_name1 = Entry(order_tabel_frame2 , font="arial 12",state=DISABLED, width=20)
                    item_name1.grid(row=0,column=3,padx=10)
                    
                    item_name_label2 = Label(order_tabel_frame2 , text="Extra Discount", 
                                font=("arial", 12, "bold"), fg="black")
                    item_name_label2.grid(row=1,column=0,pady=20)
            
                    item_name2 = Entry(order_tabel_frame2 , font="arial 12",state=DISABLED, width=20)
                    item_name2.grid(row=1,column=1,padx=10)
                    
                    item_name_label3 = Label(order_tabel_frame2 , text="Total Bill", 
                                font=("arial", 12, "bold"), fg="black")
                    item_name_label3.grid(row=1,column=2)
            
                    item_name3 = Entry(order_tabel_frame2 , font="arial 12",state=DISABLED, width=20,textvariable=totbill)
                    item_name3.grid(row=1,column=3,padx=10)
            
            
            
            
            
            
            
            def bill():
                length=len(order_tabel.get_children())
                print(length)
                flag=0
                global order_S,item_id
                text="| S.No. |   Name       |  Volume  |  Rate  |  Quantity  |  Price  |\n"
                # if item_id:
                if length:
                    if totalPrice:
                        for i in range(1,length+1):
                            td=order_tabel.item(i)
                            rid=td["values"]
                            cur=conn.cursor()
                            cur.execute('SELECT Avail FROM sale where d_id=?',(rid[6]))
                            row=cur.fetchone()
                            
                            if row[0]<rid[4]:
                                answer=askyesno(title='Conformation',message=f"we have only {row[0]} items of {rid[1]} in our stock\n do you want to continue with {row[0]}")
                                if answer:
                                    price=itemRate.get()*row[0]
                                    rid[4]=row[0]
                                    order_tabel.item(i, text="",values=(rid[0],itemName.get(),itemVolume.get(),itemRate.get(),row[0],price,item_id))
                                    text=text+("| "+str(rid[0])+"  |  "+str(rid[1])+"  |  "+str(rid[2])+"  |  "+str(rid[3])+"  |        "+str(rid[4])+"       |  "+str(rid[5])+"  |\n")  
                                    totalamt()
                                else:
                                    order_tabel.item(i, text="",values=(rid[0],"Item Removed","0","0","0","0",rid[6]))
                                    rid[4]=0
                                    totalamt()
                            else:
                                text=text+("| "+str(rid[0])+"  |  "+str(rid[1])+"  |  "+str(rid[2])+"  |  "+str(rid[3])+"  |        "+str(rid[4])+"       |  "+str(rid[5])+"  |\n")  
                
                        text=text+"\nTotal Bill :  "+str(totalPrice.get())
                        answer = askyesno(title='Success',message=text+"\n\nPrint")
                        if answer:
                            for i in range(1,length+1):
                                td=order_tabel.item(i)
                                rid=td["values"]
                                cursor = conn.cursor()
                                cursor.execute("update sale set Avail=Avail-?,date=? where d_id=?",(rid[4],now,rid[6]))
                                conn.commit()
                            bill_button_operation()
                            for i in order_tabel.get_children():
                                order_tabel.delete(i)
                            order_S=0
                            
                        print(text)
                    else:
                        mb.showerror("error","Add items first",parent=root)
                else:
                    mb.showerror("error","Add items first",parent=root)
                # else:
                #     mb.showerror("error","refresh the table and continue")
            
            
            
            style_button = ttk.Style()
            style_button.configure("TButton",font = ("arial",10,"bold"),background="palegreen")
            
            title_frame = Frame(root, bd=8, bg="red", relief=GROOVE)
            title_frame.pack(side=TOP, fill="x")
            
            title_label = Label(title_frame, text="Store Billing", 
                                font=("times new roman", 20, "bold"),bg = "red", fg="white", pady=5)
            title_label.pack()
            
            customer_frame = LabelFrame(root,text="Customer Details",font=("times new roman", 15, "bold"),
                                        bd=8, bg="lightblue", relief=GROOVE)
            customer_frame.pack(side=TOP, fill="x")
            
            customer_name_label = Label(customer_frame, text="Name", 
                                font=("arial", 15, "bold"),bg = "lightblue", fg="blue")
            customer_name_label.grid(row = 0, column = 0)
            
            customerName = StringVar()
            customerName.set("")
            customer_name_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,
                                            textvariable=customerName)
            customer_name_entry.grid(row = 0, column=1,padx=50)
            
            customer_contact_label = Label(customer_frame, text="Contact", 
                                font=("arial", 15, "bold"),bg = "lightblue", fg="blue")
            customer_contact_label.grid(row = 0, column = 2)
            
            customerContact = StringVar()
            customerContact.set("")
            customer_contact_entry = Entry(customer_frame,width=20,font="arial 15",bd=5,
                                            textvariable=customerContact)
            customer_contact_entry.grid(row = 0, column=3,padx=50)
            
            # menu_frame = Frame(root,bd=8, bg="palegreen", relief=GROOVE)
            # menu_frame.place(x=0,y=125,height=585,width=680)
            
            menu_frame = Frame(root,bd=8, bg="palegreen", relief=GROOVE)
            menu_frame.pack(side=LEFT ,fill="both",expand=True)
            
            menu_label = Label(menu_frame, text="Menu", 
                                font=("times new roman", 20, "bold"),bg = "palegreen", fg="red", pady=0)
            menu_label.pack(side=TOP,fill="x")
            
            menu_category_frame = Frame(menu_frame,bg="palegreen",pady=10)
            menu_category_frame.pack(fill="x")
            
            
            
            
            
            
            
            combo_lable = Label(menu_category_frame,text="Search by Category", 
                                font=("times new roman", 11, "bold"),bg = "palegreen", fg="blue")
            combo_lable.grid(row=0,column=0,padx=20)
            
            
            combo_lable = Label(menu_category_frame,text="Search by Brand Name", 
                                font=("times new roman", 11, "bold"),bg = "palegreen", fg="blue")
            combo_lable.grid(row=0,column=1,padx=20)
            
            cur=conn.cursor()
            cur.execute('SELECT deal.category FROM sale INNER JOIN deal ON deal.d_id=sale.d_id and Avail>0;')
            row=cur.fetchall()
            cat=[]
            for dt in row:
                cat.append(dt[0].capitalize())
            cat=list(tuple(set(cat)))
            menuCategory.set("")
            combo_menu = AutocompleteCombobox(menu_category_frame,width=20, completevalues=cat,textvariable = menuCategory)
            combo_menu.grid(row=1,column=0,padx=20)
            
            cur=conn.cursor()
            cur.execute('SELECT deal.product_name FROM sale INNER JOIN deal ON deal.d_id=sale.d_id and Avail>0;')
            row=cur.fetchall()
            cat2=[]
            for dt in row:
                cat2.append(dt[0].capitalize())
            cat2=list(tuple(set(cat2)))
            menuCategory2.set("")
            combo_menu2 = AutocompleteCombobox(menu_category_frame,width=20, completevalues=cat2,textvariable = menuCategory2)
            combo_menu2.grid(row=1,column=1,padx=20)
            
            
            
            
            
            show_button = ttk.Button(menu_category_frame, text="Show",width=10,command=show)
            show_button.grid(row=1,column=2,padx=20)
            
            show_all_button = ttk.Button(menu_category_frame, text="Show All",
                                    width=10,command=showall)
            show_all_button.grid(row=1,column=3,padx=20)
            
            menu_tabel_frame = Frame(menu_frame)
            menu_tabel_frame.pack(fill=BOTH,expand=1)
            
            scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
            scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)
            
            style = ttk.Style()
            style.configure("Treeview.Heading",font=("arial",13, "bold"))
            style.configure("Treeview",font=("arial",12),rowheight=25)
            
            menu_tabel = ttk.Treeview(menu_tabel_frame,style = "Treeview",
                        columns =("brand_name","name","price","volume","Category","d_id","s.no"),xscrollcommand=scrollbar_menu_x.set,yscrollcommand=scrollbar_menu_y.set)
            
            menu_tabel.heading("name",text="Name")
            menu_tabel.heading("brand_name",text="brand Name")
            menu_tabel.heading("price",text="Price")
            menu_tabel.heading("volume",text="volume")
            menu_tabel.heading("Category",text="Category")
            menu_tabel["displaycolumns"]=("brand_name","name", "price","volume","Category")
            menu_tabel["show"] = "headings"
            menu_tabel.column("price",width=10,anchor='center')
            menu_tabel.column("volume",width=10,anchor='center')
            menu_tabel.column("name",width=20,anchor='center')
            menu_tabel.column("brand_name",width=20,anchor='center')
            menu_tabel.column("Category",width=20,anchor='center')
            menu_tabel.column("d_id",width=20,anchor='center')
            menu_tabel.column("s.no",width=20,anchor='center')
            menu_tabel.bind('<ButtonRelease-1>',select_item)
            
            
            scrollbar_menu_x.pack(side=BOTTOM,fill=X)
            scrollbar_menu_y.pack(side=RIGHT,fill=Y)
            
            scrollbar_menu_x.configure(command=menu_tabel.xview)
            scrollbar_menu_y.configure(command=menu_tabel.yview)
            
            menu_tabel.pack(fill=BOTH,expand=1)
            
            
            
            
            
            
            
            
            # item_frame = Frame(root,bd=8, bg="palegreen", relief=GROOVE)
            # item_frame.place(x=680,y=125,height=230,width=680)
            item_frame = Frame(root,bd=8, bg="palegreen", relief=GROOVE)
            item_frame.pack(side=LEFT ,fill="both",expand=True)
            
            item_title_label = Label(item_frame, text="Item", 
                                font=("times new roman", 20, "bold"),bg = "palegreen", fg="red")
            item_title_label.pack(side=TOP,fill="x")
            
            item_frame2 = Frame(item_frame, bg="palegreen")
            item_frame2.pack(fill=X)
            
            item_name_label = Label(item_frame2, text="Name", 
                                font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            item_name_label.grid(row=0,column=0)
            
            itemCategory = StringVar()
            itemCategory.set("")
            
            
            item_name = Entry(item_frame2, font="arial 12",textvariable=itemName,state=DISABLED, width=25)
            item_name.grid(row=0,column=1,padx=10)
            
            item_rate_label = Label(item_frame2, text="Price", 
                                font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            item_rate_label.grid(row=0,column=2,padx=40)
            
            
            item_rate = Entry(item_frame2, font="arial 12",textvariable=itemRate,state=DISABLED, width=10)
            item_rate.grid(row=0,column=3,padx=10)
            
            item_quantity_label = Label(item_frame2, text="Quantity", 
                                font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            item_quantity_label.grid(row=1,column=0,padx=30,pady=15)
            
            
            item_quantity = Spinbox(item_frame2,textvariable=itemQuantity,from_ = 0,to_ = 150,width=19,font="arial 12" )
            item_quantity.grid(row = 1, column=1)
            
            
            
            item_Volume_label = Label(item_frame2, text="volume", 
                                font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            item_Volume_label.grid(row=1,column=2,padx=40)
            
            
            item_Volume = Entry(item_frame2, font="arial 12",textvariable=itemVolume,state=DISABLED, width=10)
            item_Volume.grid(row=1,column=3)
            
            
            item_frame3 = Frame(item_frame, bg="palegreen")
            item_frame3.pack(fill=X)
            
            add_button = ttk.Button(item_frame3, text="Add Item",command=additem)
            add_button.grid(row=0,column=0,padx=40,pady=30)
            
            remove_button = ttk.Button(item_frame3, text="Remove Item",command=removeitem)
            remove_button.grid(row=0,column=1,padx=40,pady=30)
            
            update_button = ttk.Button(item_frame3, text="Update Quantity",command=updateitem)
            update_button.grid(row=0,column=2,padx=40,pady=30)
            
            # clear_button = ttk.Button(item_frame3, text="Clear")
            # clear_button.grid(row=0,column=3,padx=40,pady=30)
            
            # order_frame = Frame(root,bd=8, bg="palegreen", relief=GROOVE)
            # order_frame.place(x=680,y=335,height=370,width=680)
            
            order_frame = Frame(item_frame, bd=8, bg="palegreen", relief=GROOVE)
            order_frame.pack(expand=True ,fill="both",side=LEFT)
            
            order_title_label = Label(order_frame, text="Your Order", 
                                font=("times new roman", 20, "bold"),bg = "palegreen", fg="red")
            order_title_label.pack(side=TOP,fill="x")
            
            order_tabel_frame = Frame(order_frame)
            order_tabel_frame.place(x=0,y=40,height=260,width=680)
            
            scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
            scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)
            
            order_tabel = ttk.Treeview(order_tabel_frame,
                        columns =("S.No","name","Volume","rate","quantity","price","category","d_id"),xscrollcommand=scrollbar_order_x.set,
                        yscrollcommand=scrollbar_order_y.set)
            order_tabel.heading("S.No",text="S.No")
            order_tabel.heading("name",text="Name")
            order_tabel.heading("rate",text="Rate")
            order_tabel.heading("quantity",text="Quantity")
            order_tabel.heading("price",text="Price")
            order_tabel.heading("Volume",text="Volume")
            order_tabel["displaycolumns"]=("S.No","name", "Volume","rate","quantity","price")
            order_tabel["show"] = "headings"
            order_tabel.column("S.No",width=60,anchor='center', stretch=NO)
            order_tabel.column("Volume",width=100,anchor='center', stretch=NO)
            order_tabel.column("rate",width=100,anchor='center', stretch=NO)
            order_tabel.column("quantity",width=100,anchor='center', stretch=NO)
            order_tabel.column("price",width=100,anchor='center', stretch=NO)
            order_tabel.column("d_id",width=100,anchor='center', stretch=NO)
            order_tabel.bind('<ButtonRelease-1>',select_item_order)
            
            scrollbar_order_x.pack(side=BOTTOM,fill=X)
            scrollbar_order_y.pack(side=RIGHT,fill=Y)
            
            scrollbar_order_x.configure(command=order_tabel.xview)
            scrollbar_order_y.configure(command=order_tabel.yview)
            
            order_tabel.pack(fill=BOTH,expand=1)
            
            
            
            
            
            
            
            
            
            
            
            #discount_label = Label(order_frame, text="Discount",
             #                   font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            #discount_label.place(x=20,y=250)
            
            #discountPrice = StringVar()
            #discountPrice.set("")
            #discount_entry = Entry(order_frame, font="arial 12",textvariable=discountPrice, width=8)
            #discount_entry.place(x=120,y=250)
            
            #totaldiscount_label = Label(order_frame, text="Total Discount",
            #                    font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            # totaldiscount_label.place(x=230,y=250)
            
            # totaldiscountPrice = StringVar()
            # totaldiscountPrice.set("")
            # totaldiscount_entry = Entry(order_frame, font="arial 12",textvariable=discountPrice, width=8)
            # totaldiscount_entry.place(x=360,y=250)
            
            # extradiscount_label = Label(order_frame, text="Extra Discount",
            #                     font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            # extradiscount_label.place(x=470,y=250)
            
            # extradiscountPrice = StringVar()
            # extradiscountPrice.set("")
            # extradiscount_entry = Entry(order_frame, font="arial 12",textvariable=discountPrice, width=8)
            # extradiscount_entry.place(x=600,y=250)
            
            
            
            
            
            total_price_label = Label(order_frame, text="Total Amount", 
                                font=("arial", 12, "bold"),bg = "palegreen", fg="blue")
            total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=10)
            
            totalPrice = StringVar()
            totalPrice.set("")
            total_price_entry = Entry(order_frame, font="arial 12",textvariable=totalPrice,state=DISABLED, 
                                        width=10)
            total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=10)
            
            bill_button = ttk.Button(order_frame, text="Bill",width=8,command=bill)
            bill_button.pack(side=LEFT,anchor=S,padx=130,pady=10)
            
            cancel_button = ttk.Button(order_frame, text="Cancel Order",command=Cancel)
            cancel_button.pack(side=LEFT,anchor=SE,padx=30,pady=10)
            
            showall()
            
            
                 
                 
            backbutton = Button(root, text='Back',width=7,bg='lightsalmon1',fg='black',font=("times new roman",15,"bold"),bd=3,relief=RIDGE,activeforeground="black",activebackground="lightsalmon1",command=back)
            backbutton.place(x=1190,y=80)  
                 
                 
                 
                 
                 
                              
            
            root.mainloop()