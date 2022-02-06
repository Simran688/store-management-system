from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
from PIL import Image,ImageTk


root = Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
root.title("Store Management System")
root.configure(background="white")

#'''''bg image''''''
bgimg=ImageTk.PhotoImage(file="images/stores.jpg")
bg=Label(root,image=bgimg).place(x=0,y=0,relwidth=1,relheight=1)

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

title_tabel.heading("id",text="Id")
title_tabel.heading("name",text="Name")
title_tabel.heading("description",text="Description")
title_tabel.heading("date",text="Date")
title_tabel["displaycolumns"]=("id","name", "description","date")
title_tabel["show"] = "headings"
title_tabel.column("date",width=100,anchor='center', stretch=NO)


scrollbar_order_x.pack(side=BOTTOM,fill=X)
scrollbar_order_y.pack(side=RIGHT,fill=Y)

scrollbar_order_x.configure(command=title_tabel.xview)
scrollbar_order_y.configure(command=title_tabel.yview)

title_tabel.pack(fill=BOTH,expand=1)

app_width=700
app_height=240
xcor=(root.winfo_screenwidth()/2)-(app_width/2)
ycor=(root.winfo_screenheight()/2)-(app_height/2)
frame2=Frame(root,bg="white")
frame2.place(x=xcor,y=ycor,width=700,height=430)

l1 = Label(frame2, text="Id",font=("times new roman",15,"bold"),bg='white',fg='gray')
l1.place(x=90,y=30)
e1 = Entry(frame2,font=("times new roman",15),bg='lightgray')
e1.place(x=90,y=60,width=200)

l2 = Label(frame2, text="Name",font=("times new roman",15,"bold"),bg='white',fg='gray')
l2.place(x=400,y=30)
e2 = Entry(frame2,font=("times new roman",15),bg='lightgray')
e2.place(x=400,y=60,width=200)

l3 = Label(frame2, text="Email",font=("times new roman",15,"bold"),bg='white',fg='gray')
l3.place(x=90,y=100)
e3 = Entry(frame2,font=("times new roman",15),bg='lightgray')
e3.place(x=90,y=130,width=200)

l4 = Label(frame2, text="Contact No.",font=("times new roman",15,"bold"),bg='white',fg='gray')
l4.place(x=400,y=100)
e4 = Entry(frame2,font=("times new roman",15),bg='lightgray')
e4.place(x=400,y=130,width=200)

l5 = Label(frame2, text="Address",font=("times new roman",15,"bold"),bg='white',fg='gray')
l5.place(x=90,y=240)
e5 = Entry(frame2,font=("times new roman",15),bg='lightgray')
e5.place(x=90,y=270,width=200)

l6 = Label(frame2, text="Gender",font=("times new roman",15,"bold"),bg='white',fg='gray')
l6.place(x=400,y=240)
var = IntVar()
r1 = Radiobutton(frame2, text="Male", variable=var, value=1, font=("times new roman",15))
r1.place(x=400,y=270)
r2 = Radiobutton(frame2, text="Female", variable=var, value=2, font=("times new roman",15))
r2.place(x=500,y=270)

l7 = Label(frame2, text="DOB",font=("times new roman",15,"bold"),bg='white',fg='gray')
l7.place(x=90,y=170)
dob = DateEntry(frame2,  bg='lightgray',date_pattern='dd/mm/Y', font=("times new roman",15))
dob.place(x=90,y=200,width=200)

l8 = Label(frame2, text="Select designation",font=("times new roman",15,"bold"),bg='white',fg='gray')
l8.place(x=90,y=310)
svar = StringVar()
svar.set("Select designation")
option = ("Admin", "Employee", "Supplier")
o = OptionMenu(frame2,svar, *option)
o.config(font=("times new roman",15),bg='lightgray')
o.place(x=90,y=340,width=230)

l9 = Label(frame2, text="DOJ",font=("times new roman",15,"bold"),bg='white',fg='gray')
l9.place(x=400,y=170)
dob = DateEntry(frame2,  bg='lightgray',date_pattern='dd/mm/Y', font=("times new roman",15))
dob.place(x=400,y=200,width=200)

b1 = Button(frame2, text='Allow',width=10,bg='green',fg='white',font=("times new roman",15,"bold"))
b1.place(x=150,y=400)
b2 = Button(frame2, text='Reject',width=10,bg='orange',fg='white',font=("times new roman",15,"bold"))
b2.place(x=400,y=400)

root.mainloop()