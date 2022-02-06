import smtplib
from tkinter import messagebox as mb

def gmail(user, password,to_addrs, subject, text):
    msg='Subject: {}\n\n{}'.format(subject, text)    
    print("Sending msg......",to_addrs,msg)
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(user, password)
    server.sendmail(user, to_addrs, msg)
    server.quit()
    mb.showinfo("showinfo", "Message Sent")
