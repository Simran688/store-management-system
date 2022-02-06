import tkinter.messagebox as mb  
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import pyodbc

root = Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
root.title(" store management system")
root.configure(background = "white")
loginid_var=StringVar()
password_var=StringVar()

#'''''bg image''''''
bgimg=ImageTk.PhotoImage(file="sms.jpg")
bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)
loginid=loginid_var.get()
password=password_var.get()


def Signup():
    root.destroy()
    import sms_Registration_form



def Login():
    loginid=str(loginid_var.get())
    password=str(password_var.get())
    if(loginid_var.get()=="" or password_var.get()==""):
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
         conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SIMRAN;'
                      'Database=sm_db;'
                      'Trusted_Connection=yes;')
         cur=conn.cursor()
         cur.execute("select Email,password,designation,f_name,authenticated,id from members where Email=? and password=?",(loginid,password))
         row=cur.fetchone()
         if(row):
                print(row)
                result=row[2].strip()
                auth=row[4].strip()
                ids=str(row[5]).strip()
                if(auth=="True" or auth=="true"):
                    if(row==None):
                        mb.showerror("Error","Invalid Username and password",parent=root)
                    elif( result == "Admin"):
                        mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
                        from sms_admin_page import take_idfromlogin
                        take_idfromlogin(ids=ids,email_v=loginid,mains=False)
                        root.destroy()
                        take_idfromlogin(ids=ids,email_v=loginid,mains=True)
                    elif( result=="Employee"):
                        #mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
                        #root.destroy()
                        #import sms_employee_page
                        mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
                        from sms_employee_page import take_idfromlogin
                        take_idfromlogin(ids=ids,email_v=loginid,mains=False)
                        root.destroy()
                        take_idfromlogin(ids=ids,email_v=loginid,mains=True)
                        
                    elif(result=="Supplier"):
                        mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
                        from sms_supplier_page import take_idfromlogin
                        take_idfromlogin(ids=ids,email_v=loginid,mains=False)
                        root.destroy()
                        take_idfromlogin(ids=ids,email_v=loginid,mains=True)
                    else:
                        print("Somthing went wrong",row[2].strip(),type(row[2]))
                else:
                    mb.showerror("error",f"Access Denied {row[3].strip()}\ncontact admin",parent=root)
         else: 
                mb.showerror("error",f"Please enter correct details",parent=root)
            
        # conn = pyodbc.connect('Driver={SQL Server};'
        #               'Server=SIMRAN;'
        #               'Database=sm_db;'
        #               'Trusted_Connection=yes;')
        # cur=conn.cursor()
        # cur.execute("select Email,password,designation,f_name,authenticated,id from members where Email=? and password=?",(loginid,password))
        # row=cur.fetchone()
        # print(row)
        # result=row[2].strip()
        # auth=row[4].strip()
        # ids=str(row[5]).strip()
        # if(auth=="True" or auth=="true"):
        #     if(row==None):
        #         mb.showerror("Error","Invalid Username and password",parent=root)
        #     elif( result == "Admin"):
        #             mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
        #             from sms_admin_page import take_idfromlogin
        #             take_idfromlogin(ids=ids,email_v=loginid,mains=False)
        #             root.destroy()
        #             take_idfromlogin(ids=ids,email_v=loginid,mains=True)
        #     elif( result=="Employee"):
        #             mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
        #             root.destroy()
        #             import sms_employee_page
        #              # mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
        #              # from  sms_employee_page import take_idfromlogin
        #              # take_idfromlogin(ids=ids,email_v=loginid,mains=False)
        #              # root.destroy()
        #              # take_idfromlogin(ids=ids,email_v=loginid,mains=True)
        #     elif(result=="Supplier"):
        #             mb.showinfo("Success",f"Welcome {row[3].strip()}",parent=root)
        #             from sms_supplier_page import take_idfromlogin
        #             take_idfromlogin(ids=ids,email_v=loginid,mains=False)
        #             root.destroy()
        #             take_idfromlogin(ids=ids,email_v=loginid,mains=True)
        #     else:
        #             print("Somthing went wrong",row[2].strip(),type(row[2]))
        # else:
        #         mb.showerror("error",f"Access Denied {row[3].strip()}\ncontact admin",parent=root)
def reset():
    loginid_var.set("")
    password_var.set("")            
   

app_width=400
app_height=400
xcor=(root.winfo_screenwidth()/2)-(app_width/2)
ycor=(root.winfo_screenheight()/2)-(app_height/2)
frame1=Frame(root,bg="white")
frame1.place(x=xcor,y=ycor,width=400,height=400)


l1 = Label(frame1, text="WELCOME TO STORE",font=("times new roman",18,"bold"),bg='white',fg='green')
l1.place(x=65,y=22)
label_90 = Label(frame1, text="Login with your details:",bg='white',fg='red', width=30,font=("bold", 15))
label_90.place(x=30,y=55)

#l1 = Label(frame1, text="WELCOME TO STORE",font=("times new roman",18,"bold"),bg='white',fg='green')
#l1.place(x=15,y=22)
#label_90 = Label(frame1, text="Login with your details:",bg='white',fg='red', width=30,font=("bold", 15))
#label_90.place(x=15,y=70)  
 
label_0 = Label(frame1, text="Loginid:",bg='white',fg='gray', width=10,font=("bold", 15))
label_0.place(x=50,y=100)
entry_0 = Entry(frame1,textvariable = loginid_var,bg='lightgray' )
entry_0.place(x=200,y=100)
label_1 = Label(frame1, text="Password:",bg='white',fg='gray', width=10,font=("bold", 15))
label_1.place(x=50,y=200)
entry_1 = Entry(frame1,textvariable = password_var,bg='lightgray' )
entry_1.place(x=200,y=200)
Button(frame1, text='Reset',width=10,bg='brown',fg='white',command=reset).place(x=120,y=300)
Button(frame1, text='Signup',width=10,bg='brown',fg='white', command=Signup).place(x=200,y=300)
Button(frame1, text='login',width=10,bg='brown',fg='white', command=Login).place(x=160,y=270)

root.mainloop()