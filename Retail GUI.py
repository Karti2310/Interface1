import ctypes
import sys
import pymysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from prettytable import PrettyTable
import webbrowser
from playsound import playsound
import string
import datetime
import pyglet
import smtplib
import time
from datetime import date
from gtts import gTTS
from email.message import EmailMessage
from tabulate import tabulate
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from time import strftime
import os 
import warnings
from tkvideo import tkvideo
import random
import tkinter as tk
from tkinter import ttk
import vlc

class Login :

    def purchasebill(self):

        root.withdraw()

        root2= Toplevel(root)
        root2.geometry('1366x768')
        root2.title('New Purchase Bill')
        root2.resizable(0,0)
        root2.configure(bg='whitesmoke')
        root2.state('zoomed')

        def close():
             if messagebox.askokcancel("EXIT", "Do you wish to cancel Data Entry ?"):
                root2.destroy()
                root.deiconify()
                player.stop()
        root2.protocol("WM_DELETE_WINDOW", close)

        #VALIDATION FUNCTIONS
        def callback1(char):
            return char.isdigit()

        def callback2(char2):
            return char2.isalpha()

        #PREVENT WINDOW CLOSING
        def donothing():
            pass

        entry1 = Label(root2,text="Purchase Bills", font=('Algerian',28), bg='whitesmoke', fg='purple').place(x=500,y=10)

        entry2= Label(root2,text='Invoice Number', font=('Times New Roman',18), bg='whitesmoke', fg='blue').place(x=60,y=80)
        entry3= Label(root2,text='Supplier Name', font=('Times New Roman',18), bg='whitesmoke', fg='blue').place(x=60,y=180)
        entry4= Label(root2,text='Whole-Saler Address', font=('Times New Roman',18), bg='whitesmoke', fg='blue').place(x=60,y=280)
        entry5= Label(root2,text='Date of Purchase', font=('Times New Roman',18), bg='whitesmoke', fg='blue').place(x=60,y=380)
        entry6= Label(root2,text='Net Purchase Price', font=('Times New Roman',18), bg='whitesmoke', fg='blue').place(x=60,y=480)
        
        reg1 = root2.register(callback1)
        entry7= Entry(root2,font=('Time New Roman',12),bg='sky blue',bd=0, validate ="key", validatecommand =(reg1, '%S'))
        entry7.place(x=60,y=130, height=30, width=300)

        reg2 = root2.register(callback2)
        entry8= Entry(root2,font=('Time New Roman',12),bg='sky blue',bd=0, validate ="key", validatecommand =(reg2, '%S'))
        entry8.place(x=60,y=230, height=30, width=300)

        entry9= Entry(root2,font=('Time New Roman',12),bg='sky blue',bd=0)
        entry9.place(x=60,y=330, height=30, width=300)

        def DOB():

            def get_value():
                global trvldt
                trvldt= cal.get_date()
                root2.deiconify()
                self.dopdate.config(text = trvldt)
                root1.destroy()
            root2.withdraw()
            root1 = Toplevel(root2)
            root1.title("Select Date of Purchase")
            root1.config(bg='LightCyan2')
            root1.overrideredirect(1)
            cal = DateEntry(root1, width=40, borderwidth=2,background = 'light salmon',foregorund = 'khaki', 
                            selectbackground = 'orange', normalbackground = 'lavender', disabledbackground ='tan1')
            cal.pack(padx=20, pady=20)
            Button(root1,width=20,text="Confirm Date",bg='gold2', activebackground ='bisque2', command = get_value).pack(padx=20,pady=20)
            root1.protocol("WM_DELETE_WINDOW",donothing)
            root1.mainloop()
        
        
        toggle_btn=Button(root2, text='Select Date of Purchase',bg='gold',fg='purple',bd=0,command=DOB)
        toggle_btn.place(x=230,y=384)

        self.dopdate=Label(root2,text = "Date not selected",font=('Times New Roman',15),fg="black",bg="sky blue")
        self.dopdate.place(x=60,y=430)

        reg3 = root2.register(callback1)
        entry11= Entry(root2,font=('Time New Roman',12),bg='sky blue',bd=0, validate ="key", validatecommand =(reg3, '%S'))
        entry11.place(x=60,y=530, height=30, width=300)

        def datasubmit():
            if report['state'] == 'normal':
                report['state'] = 'disabled'
            clearbtn['state'] = 'disabled'
            try :
                con = pymysql.connect(host='localhost',user='root',password='Yash@2310', database='retail')
                cur = con.cursor()
                
                sqlcmd = 'create table if not exists invc_1 ( invoicepr_id varchar(10) Primary Key not null, \
                        date_prchs date not null, suplr_nm varchar(40) not null, suplr_adrrs varchar(80) not null, \
                            purchase_price varchar(10) not null)'
                cur.execute(sqlcmd)

                sqlcmd = """insert into invc_1 values (%s, %s, %s, %s, %s)"""
                e1 = entry7.get() #INVC No
                e3 = entry8.get()  #SUPPLIER NAME 
                e4 = entry9.get()  #SUPPLIER ADDRESS
                e5 = entry11.get() #NET PURCHASE PRICE
                e2 = self.dopdate.cget('text') #DATE OF PURCHASE
                parameters = (e1, e2, e3, e4, e5)
                cur.execute(sqlcmd,parameters)
                con.commit()
                messagebox.showinfo("Success","Purchase Details have been successfully uploaded.")
                entry7.delete(0,END)
                entry9.delete(0,END)
                entry8.delete(0,END)
                entry11.delete(0,END)
                self.dopdate.config(text='Date not selected')
            except :
                con.rollback()
                messagebox.showerror("Failure","Try uploading correct data or contact administrator")
            con.close()
            clearbtn['state'] = 'normal'
            report['state'] = 'normal'

        def complain():
            
            root2.protocol("WM_DELETE_WINDOW", donothing)

            iid = "kartikeshupadhyay15@gmail.com"
            pas = "gqnoebaxscxnpfnv"
            m = EmailMessage()
            m['From'] = 'kartikeshupadhyay@gmail.com'
            m['To'] = "yashupadhyaydhn@gmail.com"
            m['Subject'] = 'Dhanbad Retail Bazar Error'
            m.set_content('''
This is a system reported error. If by any means this email has been received by an unauthorised person, please report it to kartikeshupadhyay15@gmail.com .


Dhanbad Retail Bazar reported an error in DATA FILE UPLOADING . 


Please contact them @
drbdhanbadmanager@gmail.com''')

            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(iid,pas)
                    smtp.send_message(m)
                    smtp.quit()

            messagebox.showinfo("Reported","The issue has been escalated to the IT Team.Expect a solution soon.")
            root2.protocol("WM_DELETE_WINDOW", close)

        def clear():

            entry7.delete(0,END)
            entry9.delete(0,END)
            entry8.delete(0,END)
            entry11.delete(0,END)
            self.dopdate.config(text='Date not selected')

        sqlupload =Button(root2,text='SUBMIT',bg='royalblue',fg='white', activebackground='olivedrab',
        activeforeground='mintcream', font=('Times New Roman',20,'bold'), command = datasubmit).place(x=150,y=590)

        clearbtn =Button(root2,text='Clear',bg='coral',fg='white', activebackground='olivedrab',
        activeforeground='mintcream', font=('Times New Roman',15),command = clear,bd=0)
        clearbtn.place(x=302,y=610)

        report =Button(root2,text='Report',bg='darkred',fg='white', activebackground='olivedrab',
        activeforeground='mintcream', font=('Times New Roman',15),command=complain,bd=0)
        report.place(x=60,y=610)
        report['state'] = 'disabled'

        Frame_ad= tk.Frame(root2,bg="moccasin")
        Frame_ad.place(x=500,y=80,height=600,width=800)

        display = tk.Frame(Frame_ad, bd=5)
        display.place(relwidth=1, relheight=1)

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new("E:\Coding Projects\Codes\Play2.mp4")
        player.set_hwnd(display.winfo_id())
        player.set_media(Media)
        player.play()

        def time():
            string = strftime('%Y-%m-%d %H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(root2, font=("Times New Roman",18), fg='purple', bg='whitesmoke')
        lbl.place(x=5,y=710)
        time()
    
        root2.mainloop()

    def managebills(self):

        #STARTING MANAGE BILLS MAIN SECTION

        root.withdraw()
        con = pymysql.connect(host='localhost',user='root',password='Yash@2310', database='retail')
        cur = con.cursor()

        root3 = Toplevel()
        root3.geometry('1366x768')
        root3.title('SABE - Bill Management')
        root3.resizable(0,0)
        root3.configure(bg='goldenrod')
        root3.state('zoomed')

        def close():
             if messagebox.askokcancel("EXIT", "Do you wish to end Bill Management ?"):
                root3.destroy()
                con.commit()
                con.close()
                root.deiconify()
        root3.protocol("WM_DELETE_WINDOW", close)

        img3 = Image.open("E:\Coding Projects\Codes\photo3.png")
        bg3=ImageTk.PhotoImage(img3.resize((1255,588)))

        Frame_heading = Frame(root3,bg='white')
        Frame_heading.place(x=0,y=0,height=80,width=1366)

        Frame_content = Frame(root3, bg='bisque')
        Frame_content.place(x=50,y=170, height=588, width=1255)

        bg_image=Label(Frame_content,image=bg3)
        bg_image.pack()

        entry1 = Label(Frame_heading,text="Bill Management", font=('Times New Roman',35), bg='white', fg='#FFA500').place(x=500,y=10)
       
        #BUTTON FUNCTIONS
        def homebtn():

            #SUB-BUTTON FUNCTION
            def addbtn():
                
                a1 = options.get()                          #INVOICE ID
                c2 = centry1.get() 
                a2 =  int(c2)                               #BATCH NO   
                a3 = centry4.get()                          #PRODUCT NAME
                a4 = cal1.get_date()                        #DOM
                a5 = cal2.get_date()                        #DOE
                c6 = centry2.get()                          #UNIT PRICE
                a6 = int(c6)
                c7 = centry3.get()                          #QUANTITY
                a7 = int(c7)
                c8 = centry7.get()  
                a8  = int(c8)                               #GST

                a9 = (((a6)+((a6)*(0.01)*(a8)))*(a7))       #TOTAL MRP
                print(a1,a2,a3,a4,a5,a6,a7,a8,a9)

                try:
                    sqlcmd = """insert into invc_2 values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    parameters = (a1,a2,a3,a4,a5,a6,a7,a8,a9)
                    cur.execute(sqlcmd,parameters)
                    con.commit()
                    messagebox.showinfo("Success","Invoice records have been updated.")
                except pymysql.err.IntegrityError:
                    messagebox.showerror("Integrity Error","Batch No. already exists.Try updating.")
                    con.rollback()
                except pymysql.err.DataError :
                    messagebox.showerror("DataType Error","Please enter correct data values in the feeder.")
                    con.rollback()
                except Exception :
                    messagebox.showerror("Error","Database reporting errors.Contact IT Team.")
                    con.rollback()

                centry1.delete(0,END)
                centry2.delete(0,END)
                centry3.delete(0,END)
                centry4.delete(0,END)
                centry7.delete(0,END)

            btn2.config(bg='darkorchid')
            btn3.config(bg='darkorchid')
            btn1.config(bg='indianred')
            for widgets in Frame_content.winfo_children():
                widgets.destroy()
            
            sel_query ='''SELECT invoicepr_id FROM invc_1'''
            cur.execute(sel_query)
            result1 = cur.fetchall()
            my_list = [r for r, in result1]

            #DESIGNING THE INVOICE NUMBER OPTION
            lbl1 = Label(Frame_content,text="Select the Invoice Number :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            lbl1.place(x=20,y=20)
            options = tk.StringVar(Frame_content)
            menu1 = ttk.Combobox(Frame_content, width = 20, textvariable = options, font = ('Times New Roman',18))
            menu1['values'] = my_list
            menu1['state'] = 'readonly'
            menu1.place(x=350,y=20)

            sqlcmd = 'create table if not exists invc_2 ( invoicepr_id varchar(10) not null, Btch_No int(10) Primary Key not null, prdt_nm char(40) not null,\
                    DOM date not null,  DOE date not null, Unit_PriceRS varchar(6) not null, qty varchar(9) not null , \
                    GST varchar(3) not null, ttl_MRP varchar(10) not null, FOREIGN KEY (invoicepr_id) REFERENCES invc_1(invoicepr_id) ON UPDATE CASCADE ON DELETE CASCADE  )'
            cur.execute(sqlcmd)

            clbl1 = Label(Frame_content,text="Enter Batch Number :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl1.place(x=20,y=80)
            centry1 = Entry(Frame_content,font=('Times New Roman',18),bg='floralwhite',bd=0)
            centry1.place(x=350,y=80, height=30, width=250)
            clbl2 = Label(Frame_content,text="Enter Unit Price :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl2.place(x=20,y=140)
            centry2 = Entry(Frame_content, font=('Times New Roman',18), bg='floralwhite',bd=0)
            centry2.place(x=350,y=140, height=30, width=250)
            clbl3 = Label(Frame_content,text="Enter Quantity :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl3.place(x=20,y=200)
            centry3 = Entry(Frame_content, font=('Times New Roman', 18), bg='floralwhite',bd=0)
            centry3.place(x=350,y=200,height=30, width = 250)
            clbl4 = Label(Frame_content,text="Enter Product Name :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl4.place(x=20,y=260)
            centry4 = Entry(Frame_content, font=('Times New Roman', 18), bg='floralwhite',bd=0)
            centry4.place(x=350,y=260, height=30, width=250)
            clbl5 = Label(Frame_content,text="Enter Manufacturing Date :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl5.place(x=650,y=80)
            clbl6 = Label(Frame_content,text="Enter Expiry Date :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl6.place(x=650,y=140)
            clbl7 = Label(Frame_content,text="Enter GST% Applicable :", font = ('Times New Roman', 20),bg = 'bisque',fg='purple')
            clbl7.place(x=650,y=200)
            centry7= Entry(Frame_content, font=('Times New Roman', 18), bg='floralwhite',bd=0)
            centry7.place(x=980,y=200, height=30, width=250)
            cal1 = DateEntry(Frame_content, width=40, borderwidth=2,background = 'light salmon',foregorund = 'khaki', 
                            selectbackground = 'orange', normalbackground = 'lavender', disabledbackground ='tan1')
            cal1.place(x=980,y=80, height=30, width=250)
            cal2 = DateEntry(Frame_content, width=40, borderwidth=2,background = 'light salmon',foregorund = 'khaki', 
                            selectbackground = 'orange', normalbackground = 'lavender', disabledbackground ='tan1')
            cal2.place(x=980,y=140, height=30, width=250)
            entrybtn = Button(Frame_content, text='ADD', fg='white', bg='limegreen',activebackground='forestgreen',
                       font = ('Times New Roman',20), command= addbtn)
            entrybtn.place(x=580,y=350)


        def modifybtn():

            for widgets in Frame_content.winfo_children():
                widgets.destroy()

            def updatenamebtn():
                try :
                    f1 = prdtentry.get()
                    f2 = selected.get()
                    sqlcmd = """UPDATE invc_2 SET prdt_nm = %s WHERE Btch_No = %s"""
                    parameters = (f1,f2)
                    cur.execute(sqlcmd,parameters)
                    con.commit()
                    messagebox.showinfo("Success","Product Name has been changed.")
                    prdtentry.delete(0,END)
                except Exception as e :
                    con.rollback()
                    messagebox.showerror("Error",e)

            def updateqtybtn():
                try :
                    f1 = prdtentry.get()
                    f2 = selected.get()
                    sqlcmd = """UPDATE invc_2 SET qty = %s WHERE Btch_No = %s"""
                    parameters = (f1,f2)
                    cur.execute(sqlcmd,parameters)
                    con.commit()
                    messagebox.showinfo("Success","Product Quantity has been changed.")
                    prdtentry.delete(0,END)
                except Exception as e :
                    con.rollback()
                    messagebox.showerror("Error",e)

            def updatedoebtn():
                try :
                    f1 = prdtentry.get()
                    f2 = selected.get()
                    sqlcmd = """UPDATE invc_2 SET DOE = %s WHERE Btch_No = %s"""
                    parameters = (f1,f2)
                    cur.execute(sqlcmd,parameters)
                    con.commit()
                    messagebox.showinfo("Success","Expiry Date has been changed.")
                    prdtentry.delete(0,END)
                except Exception as e :
                    con.rollback()
                    messagebox.showerror("Error",e)

            def updatedombtn():
                try :
                    f1 = prdtentry.get()
                    f2 = selected.get()
                    sqlcmd = """UPDATE invc_2 SET DOM = %s WHERE Btch_No = %s"""
                    parameters = (f1,f2)
                    cur.execute(sqlcmd,parameters)
                    con.commit()
                    messagebox.showinfo("Success","Manufacturing Date has been changed.")
                    prdtentry.delete(0,END)
                except Exception as e :
                    con.rollback()
                    messagebox.showerror("Error",e)

            def dombtn():
                x1 = 1
                x2 = 0
                x3 = 0
                x4 = 0
                ubtn1.config(bg='peru')
                ubtn2.config(bg='bisque')
                ubtn3.config(bg='peru')
                ubtn4.config(bg='peru')
                ubtn5.config(bg='peru')
                prdtlabel.config(text='Enter Manufacture Date :')
                prdtentry.config(state='normal')
                updatebtn.config(state='normal')
                updatebtn.config(command= updatedombtn)

            def doebtn():
                x1 = 0 
                x2 = 1
                x3 = 0
                x4 = 0 
                ubtn1.config(bg='peru')
                ubtn2.config(bg='peru')
                ubtn3.config(bg='bisque')
                ubtn4.config(bg='peru')
                ubtn5.config(bg='peru')
                prdtlabel.config(text='Enter Expiry Date :')
                prdtentry.config(state='normal')
                updatebtn.config(state='normal')
                updatebtn.config(command = updatedoebtn)

            def qtybtn():
                x1 = 0
                x2 = 0
                x3 = 1
                x4 = 0
                ubtn1.config(bg='peru')
                ubtn2.config(bg='peru')
                ubtn3.config(bg='peru')
                ubtn4.config(bg='bisque')
                ubtn5.config(bg='peru')
                prdtlabel.config(text='Enter New Item Quantity :')
                prdtentry.config(state='normal')
                updatebtn.config(state='normal')
                updatebtn.config(command=updateqtybtn)

            def pricebtn():
               
                ubtn1.config(bg='peru')
                ubtn2.config(bg='peru')
                ubtn3.config(bg='peru')
                ubtn4.config(bg='peru')
                ubtn5.config(bg='bisque')
                prdtlabel.config(text='This feature is currently unavailable.')
                prdtentry.config(state='disabled')
                updatebtn.config(state='disabled')

            def prdtnmbtn():
                x1 = 0
                x2 = 0
                x3 = 0
                x4 = 1
                ubtn1.config(bg='bisque')
                ubtn2.config(bg='peru')
                ubtn3.config(bg='peru')
                ubtn4.config(bg='peru')
                ubtn5.config(bg='peru')
                prdtlabel.config(text='Enter New Product Name :')
                prdtentry.config(state='normal')
                updatebtn.config(state='normal')
                updatebtn.config(command=updatenamebtn)

            def mysqlfn(event):
                sel_query =  '''SELECT * FROM invc_2 WHERE Btch_No = %s'''
                cur.execute(sel_query,selected.get())
                myresult1 = cur.fetchall()
                for row in myresult1 :
                    olabel1.config(text=row[0])
                    olabel2.config(text=row[2])
                    olabel3.config(text=row[3])
                    olabel4.config(text=row[4])
                    olabel5.config(text=row[5])
                    olabel6.config(text=row[6])
                    olabel7.config(text=row[7])
            btn1.config(bg='darkorchid')
            btn3.config(bg='darkorchid')
            btn2.config(bg='indianred')

            Frame_sub = Frame(Frame_content, bg='peru')
            Frame_sub.place(x=0,y=0, height=588, width=310)

            updatebtn = Button(Frame_content,text='UPDATE',font=('Times New Roman',20),bg='green',fg='white',
             state = 'disabled')
            updatebtn.place(x=1050,y=200)
                
            ubtn1 = Button(Frame_sub, text = 'Product Name', font=('Times New Roman',18),bg='peru',width=25,bd=0, command= prdtnmbtn)
            ubtn1.place(x=0,y=60)
            ubtn2 = Button(Frame_sub, text = 'Manufacture Date', font=('Times New Roman',18),bg='peru',width=25,bd=0, command = dombtn)
            ubtn2.place(x=0,y=130)
            ubtn3 = Button(Frame_sub, text = 'Expiry Date', font=('Times New Roman',18),bg='peru',width=25,bd=0, command = doebtn)
            ubtn3.place(x=0,y=200)
            ubtn4 = Button(Frame_sub, text = 'Item Quantity', font=('Times New Roman',18),bg='peru',width=25,bd=0,  command = qtybtn)
            ubtn4.place(x=0,y=270)
            ubtn5 = Button(Frame_sub, text = 'Pricing & Taxes', font=('Times New Roman',18),bg='peru',width=25,bd=0, command = pricebtn)
            ubtn5.place(x=0,y=340)
            
            prdtlabel = Label(Frame_content,text = 'Select a Side Pane Option', font = ('Times New Roman', 18),bg = 'bisque',fg='black',  bd =0)
            prdtlabel.place(x=350,y=90)
            prdtentry = Entry(Frame_content, font=('Times New Roman',18), bg='floralwhite', fg='black', bd=0, state = 'disabled')
            prdtentry.place(x=630,y=90)
            
            sel_query ='''SELECT Btch_no FROM invc_2'''
            cur.execute(sel_query)
            result2 = cur.fetchall()
            my_options = [r for r, in result2]

            lbl1 = Label(Frame_content,text="Select the Batch Number :", font = ('Times New Roman', 18),bg = 'bisque',fg='black')
            lbl1.place(x=350,y=30)
            
            selected = tk.StringVar(Frame_content)

            menu2 = ttk.Combobox(Frame_content, width = 20, textvariable = selected, font = ('Times New Roman',18))
            menu2['values'] = my_options
            menu2['state'] = 'readonly'
            menu2.place(x=630,y=30)
            menu2.bind("<<ComboboxSelected>>", mysqlfn)

            labelframe = LabelFrame(Frame_content, text="Product Details",bd=4, bg='navajowhite',font=(15))
            labelframe.place(x=350,y=300,height=250, width=850)

            #INFO LABELS
            label1 = Label(labelframe,text = 'INOVICE ID :', font = ('Times New Roman',12), bg='navajowhite')
            label1.place(x=20,y=20)
            label2 = Label(labelframe,text = 'PRODUCT NAME :', font = ('Times New Roman',12), bg='navajowhite')
            label2.place(x=20,y=60)
            label3 = Label(labelframe,text = 'MANUFACTURING DATE :', font = ('Times New Roman',12), bg='navajowhite')
            label3.place(x=20,y=100)
            label4 = Label(labelframe,text = 'EXPIRY DATE :', font = ('Times New Roman',12), bg='navajowhite')
            label4.place(x=20,y=140)
            label5 = Label(labelframe,text = 'UNIT PRICE :', font = ('Times New Roman',12), bg='navajowhite')
            label5.place(x=20,y=180)
            label6 = Label(labelframe,text = 'QUANTITY :', font = ('Times New Roman',12), bg='navajowhite')
            label6.place(x=450,y=20)
            label7 = Label(labelframe,text = 'GST :', font = ('Times New Roman',12), bg='navajowhite')
            label7.place(x=450,y=60)

            #OUTPUT LABELS
            olabel1 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel1.place(x=220,y=20)
            olabel2 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel2.place(x=220,y=60)
            olabel3 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel3.place(x=220,y=100)
            olabel4 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel4.place(x=220,y=140)
            olabel5 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel5.place(x=220,y=180)
            olabel6 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel6.place(x=600,y=20)
            olabel7 = Label(labelframe,text = '', font = ('Times New Roman',12), bg='navajowhite')
            olabel7.place(x=600,y=60)

        
        def deletebtn():
            btn1.config(bg='darkorchid')
            btn2.config(bg='darkorchid')
            btn3.config(bg='indianred')

            for widgets in Frame_content.winfo_children():
                widgets.destroy()

            sel_query ='''SELECT invoicepr_id FROM invc_1'''
            cur.execute(sel_query)
            result3 = cur.fetchall()
            my_values = [r for r, in result3]

            if len(my_values) == 0 :
                    messagebox.showerror("Invoice Not Found","No Invoices are found on this computer.")
            else :
                
                empty_list =[]
                
                def deleteinvc():
                    try :
                        f3 = selected.get()
                        sqlcmd = """DELETE FROM invc_1 WHERE invoicepr_id = %s"""
                        cur.execute(sqlcmd,f3)
                        con.commit()
                        messagebox.showinfo("Success","Selected Invoice has been deleted.")
                    except Exception as e :
                        con.rollback()
                        messagebox.showerror("Error",e)
                
                def delitem():
                    try :
                        f4 = selected_invc.get()
                        sqlcmd = """DELETE FROM invc_2 WHERE Btch_No = %s"""
                        cur.execute(sqlcmd,f4)
                        con.commit()
                        messagebox.showinfo("Success","Select Item has been dropped from invoice.")
                    except Exception as e :
                        con.rollback()
                        messagebox.showerror("Error",e)

                def invc_option(event):

                    global my_list
                    ubtn6.config(state='normal')
                    ubtn7.config(state='normal')
                    sel_query ='''SELECT Btch_No FROM invc_2 WHERE invoicepr_id = %s'''
                    cur.execute(sel_query,selected.get())
                    result4 = cur.fetchall()
                    my_list = [r for r, in result4] 
                    print(my_list)
                    menu4['values'] = my_list
                    if len(my_list) == 0 :
                        print('Empty List')
                    else :
                        menu4.current(0)
                
                def del_invc(): 

                    menu4.place_forget()
                    ubtn6.config(bg='bisque')
                    ubtn7.config(bg='peru')
                    prdtlabel.config(text=' ')
                    deleteoption.config(state='normal')
                    deleteoption.config(command=deleteinvc)
                    
                def invc_item():

                    global my_list
                    if len(my_list) == 0 :
                        messagebox.showerror('Empty List','There are no items in this invoice')
                    else :
                        menu4.current(0)
                        menu4['state'] = 'readonly'
                        menu4.place(x=630,y=90)
                        ubtn7.config(bg='bisque')
                        ubtn6.config(bg='peru')
                        prdtlabel.config(text='Select the Batch Number :')
                        deleteoption.config(state='normal')
                        deleteoption.config(command=delitem)
                
                selected_invc = tk.StringVar()
                menu4 = ttk.Combobox(Frame_content, width = 20, textvariable = selected_invc, font = ('Times New Roman',18))

                prdtlabel = Label(Frame_content,text = 'Select Invoice No to activate Side Panel.', font = ('Times New Roman', 18),bg = 'bisque',fg='black',  bd =0)
                prdtlabel.place(x=350,y=90)
                lbl1 = Label(Frame_content,text="Select the Invoice Number :", font = ('Times New Roman', 18),bg = 'bisque',fg='black')
                lbl1.place(x=350,y=30)
                
                selected = tk.StringVar()

                menu3 = ttk.Combobox(Frame_content, width = 20, textvariable = selected, font = ('Times New Roman',18))
                menu3['values'] = my_values
                menu3['state'] = 'readonly'
                menu3.place(x=630,y=30)
                menu3.bind("<<ComboboxSelected>>", invc_option)

                deleteoption = Button(Frame_content,text='DELETE',font=('Times New Roman',20),bg='green',fg='white', state = 'disabled')
                deleteoption.place(x=1050,y=200)

                Frame_sub = Frame(Frame_content, bg='peru')
                Frame_sub.place(x=0,y=0, height=588, width=310)

                ubtn6 = Button(Frame_sub, text = 'Delete Invoice', font=('Times New Roman',18),bg='peru',width=25,bd=0
                ,command=del_invc, state = 'disabled')
                ubtn6.place(x=0,y=60)
                ubtn7 = Button(Frame_sub, text = 'Invoice Items', font=('Times New Roman',18),bg='peru',width=25,
                command=invc_item,bd=0, state = 'disabled')
                ubtn7.place(x=0,y=130)

            

        #MAIN SECTION BUTTONS
        btn1 = Button(root3, text= 'ADD ENTRY', font=('Times New Roman',18),bg='darkorchid', fg='beige', bd=0, command = homebtn)
        btn1.place(x=50,y=100)
        btn2 = Button(root3, text= 'MODIFY', font=('Times New Roman',18),bg='darkorchid', fg='beige', bd=0, command = modifybtn)
        btn2.place(x=620,y=100)
        btn3 = Button(root3, text= 'DELETE', font=('Times New Roman',18),bg='darkorchid', fg='beige', bd=0, command = deletebtn)
        btn3.place(x=1190,y=100)
        
        #ENDING MANAGE BILLS SECTION
        root3.mainloop()

    def newbill(self):

        root.withdraw()

        con = pymysql.connect(host='localhost',user='root',password='Yash@2310', database='retail')
        cur = con.cursor()

        root4 = Toplevel()
        root4.geometry('1366x768')
        root4.title('SABE - User Billing')
        root4.resizable(0,0)
        root4.configure(bg='mintcream')
        root4.state('zoomed')

        def close():
             if messagebox.askokcancel("EXIT", "Terminate Billing ?"):
                root4.destroy()
                con.rollback()
                con.close()
                root.deiconify()
        root4.protocol("WM_DELETE_WINDOW", close)
        Frame5 = Frame(root4, bg='mintcream')
        Frame5.place(x=330, y=0, height = 768, width=1100)

        def start():
            def next1():
                def emailbill():

                    tabular_table = PrettyTable(["Batch_No","Product","MRP","Qty","GST","Total"])
                    cur.execute( '''SELECT  
                    sale_2.Btch_No as Batch_No, 
                    invc_2.prdt_nm as Product,
                    sale_2.Unit_Price as MRP,
                    sale_2.Qty_sold as Quantity, 
                    sale_2.GST as GST, 
                    sale_2.ttl_sale as Total
                    FROM sale_2, invc_2 
                    WHERE sale_2.invoicesl_id  = %s 
                    AND sale_2.Btch_No  = invc_2.Btch_No
                    ''',e1)
                    result = cur.fetchall() 

                    for Batch_No,Product,MRP,Quantity,GST,Total in result :
                        tabular_table.add_row([Batch_No,Product,MRP,Quantity,GST,Total]) 

                    my_message = tabular_table.get_html_string()

                    html = """\
                    <html>
                        <head>
                        <style>
                            table, th, td {
                                border: 1px solid black;
                                border-collapse: collapse;
                            }
                            th, td {
                                padding: 5px;
                                text-align: left;    
                            }    
                        </style>
                        </head>
                    <body>
                    <p>Dear Customer,<br>
                    <br>
                    Thank You for your recent purchase at Dhanbad Retail Bazar. Here is your TAX-INVOICE.<br>
                    <br>
                    TAX-INVOICE<br>
                    <br>
                    Customer Name     : %s <br>
                    Customer EMail ID : %s <br>
                    Phone No          : %s <br>
                    Purchase Date     : %s <br>
                    <br>
                    Invoice Number    : %s <br>
                    <br>
                    %s
                    <br>
                    <br>
                    Wish you a good day ahead. <br>
                    Looking forward to you next visit. <br>
                    Warm Greetings, <br>
                    Dhanbad Retail Bazar  <br>
                    <br>
                    NOTE : THIS BILL IS VALID DIGITALLY ONLY. ANY HARDCOPY/FORWARDED COPY SHALL NOT BE CONSIDERED GENUINE.
                    <br>
                    <br>
                    Follow Us on Facebook : Dhanbad Retail Bazar
                    <br>
                    Twitter : @DhnRetailBazar <br>
                    Instagram : Dhanbad_RetailBazar <br>
                    Phone  : 1236549875
                    <br>
                    ADDRESS : <br>
                    Shop No. 011, ABC Shopping Complex, Saraidhela, Dhanbad

                    </p>
                    </body>
                    </html>
                    """ % (e4,e3,e5,e6,e1,my_message) 

                    part2 = MIMEText(html, 'html')
                    # Create the root message and fill in the from, to, and subject headers
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = 'DHANBAD RETAIL BAZAR'
                    msg['To'] = 'kartikeshupadhyay15@gmail.com'
                    msg['From'] = 'irsystem720@gmail.com'
                    msg.attach(part2)

                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                        smtp.login('kartikeshupadhyay15@gmail.com','gqnoebaxscxnpfnv')
                        smtp.send_message(msg)
                        smtp.quit()

                def remove_item():
                    lst1.clear()
                    cur.execute('DELETE FROM sale_2 WHERE invoicesl_id = %s',e1)
                    treev.delete(*treev.get_children())
                    

                def treedelete():
                    curItem = treev.item(treev.focus())
                    cell_value = str(curItem['values'][0])
                    lst1.remove(cell_value)
                    selected_item = treev.selection()[0]
                    selected = treev.focus()
                    values = treev.item(selected, 'values' )
                    elbael5.insert(0,values[0])
                    a1 = elbael5.get()
                    cur.execute('DELETE FROM sale_2 WHERE Btch_No = %s AND invoicesl_id = %s',(a1,e1))
                    treev.delete(selected_item)
                    
                    
                def treeinsert():
                    a1 = elbael5.get()
                    if len(a1) == 0 :
                        messagebox.showerror("Empty","Batch No cannot be empty.")
                    elif len(elbael6.get())  == 0 :
                        messagebox.showerror("Empty","Quantity has to  be specified.")
                    else :
                        cur.execute("SELECT Btch_No from invc_2 where Btch_No IN(%s)",a1)
                        myresult = cur.fetchall()
                        cur.execute("SELECT qty from invc_2 where Btch_No = %s",a1)
                        myresult5 = cur.fetchall()
                        for x in myresult5 :
                            def convertTuple(tup):
                                res = int(''.join(map(str, tup))) 
                                return res
                            y = convertTuple(x) 
                    
                    if len(myresult) == 0 :
                        messagebox.showerror("Missing","No item was found for the entered Batch Number.")
                        elbael5.delete(0,END) 
                        elbael6.delete(0,END)
                    elif int(elbael6.get()) > y :
                        messagebox.showerror("Low Quantity","Specified Quantity is more than the availability.")
                        elbael6.delete(0,END)
                    else :
                        if a1 in lst1 :
                            messagebox.showerror("Already Exists","The entered Batch No already exists.")
                            elbael5.delete(0,END) 
                            elbael6.delete(0,END)
                        else :
                            cur.execute("SELECT prdt_nm from invc_2 where Btch_No = %s",a1)
                            myresult5 = cur.fetchall()
                            for x in myresult5 :
                                def convertTuple(tup):
                                    res = str(''.join(map(str, tup))) 
                                    return res
                                name = convertTuple(x)
                            cur.execute("SELECT Unit_PriceRS from invc_2 where Btch_No = %s",a1)
                            myresult5 = cur.fetchall()
                            for x in myresult5 :
                                def convertTuple(tup):
                                    res = float(''.join(map(str, tup))) 
                                    return res
                                unitp = convertTuple(x)
                            cur.execute("SELECT GST from invc_2 where Btch_No = %s",a1)
                            myresult5 = cur.fetchall()
                            for x in myresult5 :
                                def convertTuple(tup):
                                    res = float(''.join(map(str, tup))) 
                                    return res
                                gstper = convertTuple(x)
                            a9 = float(elbael6.get())
                            a10 = (((unitp)+((unitp)*(0.01)*(gstper)))*(a9))

                            cur.execute('''INSERT into sale_2 (Btch_No,  invoicesl_id, Qty_sold, GST, 
                            Unit_Price, ttl_sale) values (%s,%s,%s,%s,%s,%s)'''
                            ,(elbael5.get(),e1, a9,gstper,unitp,a10))
                            lst1.append(a1)
                            treev.insert("", 'end', text ="L1", values =(elbael5.get(),name
                            ,a9,unitp,gstper,a10))
                            elbael5.delete(0,END) 
                            elbael6.delete(0,END)
                            

                def dataaddition():
                    
                    def finalizebill():
                        def cashfinish():
                            if clbael2.get() == '':
                                messagebox.showerror("Empty","Cash Recieved cannot be empty.")
                            if int(clbael2.get()) < printresult12 :
                                messagebox.showerror("Less Cash","Recieved Cash is less than invoice value.")
                            else :
                                returnamount = int(clbael2.get()) -  printresult12
                                slabel6.config(text=returnamount)
                                con.commit()
                                
                                emailbill()
                                messagebox.showinfo("Success","Bill generated successfully. Click OK to terminate.")
                                
                                root4.destroy()
                                root.deiconify()

                        clabel1 = Label(Frame5,text = 'Cash Recieved :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                        clbael2 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
                        clabel3 = Label(Frame5,text = 'Return Amount :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                        returnamount = 0
                        slabel6 = Label(Frame5,text = returnamount,font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                        
                        clabel1.place(x=60,y=300)
                        clbael2.place(x=350,y=300, height=37, width=270)
                        clabel3.place(x=60,y=370)
                        slabel6.place(x=350,y=370)

                        ebtn9 = Button(Frame5, text='Finish', bg='forestgreen', fg='white' , bd=0, font = ('Times New Roman',18), command = cashfinish)
                        ebtn9.place(x=100, y=210)
                        

                    messagebox.showwarning("Warning","You are about to confirm Data Entry.")
                    
                    for widgets in Frame5.winfo_children():
                        widgets.destroy()
                    ebtn2.config(bg='darksalmon')
                    ebtn2.config(state='disabled')
                    ebtn3.config(bg='mintcream' , fg = 'purple')

                    plabel1 = Label(Frame5,text = 'Total Quantity :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    plabel1.place(x=60,y=50)
                    plabel4 = Label(Frame5,text = 'Total Price :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    plabel4.place(x=60,y=120)


                    cur.execute("SELECT SUM(Qty_sold) FROM sale_2 WHERE invoicesl_id = %s",e1)
                    myresult11 = cur.fetchall()
                    for x in myresult11 :
                        def convertTuple(tup):
                            res = str(''.join(map(str, tup))) 
                            return res
                        printresult11 = convertTuple(x)
                    prlabel1 = Label(Frame5,text = printresult11,font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    prlabel1.place(x=350,y=50)

                    cur.execute("SELECT SUM(ttl_sale) FROM sale_2 WHERE invoicesl_id = %s",e1)
                    myresult12 = cur.fetchall()
                    for x in myresult12 :
                        def convertTuple(tup):
                            res = int(''.join(map(str, tup))) 
                            return res
                        printresult12 = convertTuple(x)
                    prlabel2 = Label(Frame5,text = printresult12,font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    prlabel2.place(x=350,y=120)

                    ebtn15 = Button(Frame5, text='Finalize Bill', bg='forestgreen', fg='white' , bd=0, font = ('Times New Roman',18), command = finalizebill)
                    ebtn15.place(x=100, y=210)


                global e1
                global e2
                global e3
                global e4
                global e5
                global e6
                
                e4 = elbael1.get()                              #CUSTOMER NAME
                e3 = elbael4.get()                              #EMAIL-ID
                e2 = selection.get()                            #AGE
                e5 = elbael3.get()                              #PHONE NO
                e6 = date.today()                               #DATE
                e1 = int(random.randint(1000,1000000000))       #INVOICE ID

                if len(e4) == 0 :
                    messagebox.showerror("Empty","Customer Name cannot be empty.")
                elif  len(e3) == 0 :
                    messagebox.showerror("Empty","E-mail ID cannot be empty.")
                elif  len(e2) == 0 :
                    messagebox.showerror("Empty","Age has to be specified.")
                elif len(e5) == 0 :
                    messagebox.showerror("Empty","Phone No cannot be empty.")
                elif len(e5) != 10 :
                    messagebox.showerror("Error","Phone No should be 10 digits long.")
                elif '.com' not in e3 :
                    messagebox.showerror("Error","Recheck the EMail-ID format.")
                elif '@' not in e3 :
                    messagebox.showerror("Error","Recheck the EMail-ID format.")
                
                else :
                    cur.execute("""insert into sale_1 values (%s, %s, %s, %s, %s, %s)""",
                    (e1, e2, e3, e4, e5, e6))
                    
                    for widgets in Frame5.winfo_children():
                        widgets.destroy()
                    ebtn1.config(bg='darksalmon')
                    ebtn1.config(state='disabled')
                    ebtn2.config(bg='mintcream' , fg = 'purple')

                    slabel5 = Label(Frame5,text = 'Enter Batch No  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    slabel5.place(x=60,y=50)
                    elbael5 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
                    elbael5.place(x=350,y=50, height=37, width=270)
                    slabel6 = Label(Frame5,text = 'Enter Quantity  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
                    slabel6.place(x=60,y=120)
                    elbael6 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
                    elbael6.place(x=350,y=120, height=37, width=270)

                    ebtn9 = Button(Frame5, text='Proceed', bg='forestgreen', fg='white' , bd=0, font = ('Times New Roman',18), command = dataaddition)
                    ebtn9.place(x=100, y=210)
                    ebtn10 = Button(Frame5, text='Add Item', bg='slateblue', fg='white' , bd=0, font = ('Times New Roman',18), command= treeinsert)
                    ebtn10.place(x=350, y=210)
                    ebtn11 = Button(Frame5, text='Delete Item', bg='Red', fg='white' , bd=0, font = ('Times New Roman',18), command = treedelete)
                    ebtn11.place(x=600, y=210)
                    ebtn12 = Button(Frame5, text='Clear Bill', bg='crimson', fg='white' , bd=0, font = ('Times New Roman',18), command = remove_item)
                    ebtn12.place(x=850, y=210)

                    Frame7 = LabelFrame(Frame5, text="ADDED ITEMS",bd=3,fg='purple', bg='mintcream',font=('Times New Roman',16))
                    Frame7.place(x=20,y=310,height=340, width=1000)

                    treev = ttk.Treeview(Frame7, selectmode ='extended')
                    treev.place(x=15,y=10)
                    lst1 = []
                    verscrlbar = ttk.Scrollbar(Frame7, orient ="vertical", command = treev.yview)

                    verscrlbar.pack(side ='left', fill ='x')
                    treev.configure(xscrollcommand = verscrlbar.set)

                    treev["columns"] = ("1", "2", "3", "4", "5", "6")
                    treev['show'] = 'headings'

                    treev.column("1", width = 130, anchor ='c')
                    treev.column("2", width = 300, anchor ='c')
                    treev.column("3", width = 130, anchor ='c')
                    treev.column("4", width = 150, anchor ='c')
                    treev.column("5", width = 100, anchor ='c')
                    treev.column("6", width = 150, anchor ='c')

                    treev.heading("1", text ="Batch No")
                    treev.heading("2", text ="Name")
                    treev.heading("3", text ="Quantity")
                    treev.heading("4", text ="Unit Price")
                    treev.heading("5", text ="GST")
                    treev.heading("6", text ="Total Price")
                
            ebtn1.config(bg='mintcream' , fg = 'purple')

            sqlcmd = 'CREATE TABLE if not exists sale_1 ( invoicesl_id INT(10) PRIMARY KEY NOT NULL,Age varchar(7) NOT NULL,  Email_ID varchar(70) NOT NULL, Cust_Nm varchar(40) NOT NULL, Cust_Cntct varchar(10) UNIQUE NOT NULL, \
                    DOSL DATE NOT NULL)'
            cur.execute(sqlcmd)

            sqlcmd = 'CREATE TABLE if not exists sale_2 (srl_id INT(10) AUTO_INCREMENT PRIMARY KEY NOT NULL, Btch_No INT(10) NOT NULL, invoicesl_id INT(10) NOT NULL,\
                        Qty_sold INT(5) NOT NULL,GST varchar(2) NOT NULL, Unit_Price varchar(5) NOT NULL, ttl_sale INT(15) NOT NULL, FOREIGN KEY (Btch_No) REFERENCES invc_2 (Btch_No) ON UPDATE CASCADE ON DELETE CASCADE,\
                        FOREIGN KEY (invoicesl_id) REFERENCES sale_1 (invoicesl_id) ON UPDATE CASCADE ON DELETE CASCADE)'
            cur.execute(sqlcmd)

            slabel1 = Label(Frame5,text = 'Enter Customer Name  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
            slabel1.place(x=60,y=50)
            elbael1 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
            elbael1.place(x=350,y=50, height=37, width=270)
            slabel2 = Label(Frame5,text = 'Select Age Group  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
            slabel2.place(x=60,y=120)
            
            selection = tk.StringVar(Frame5)

            menu6 = ttk.Combobox(Frame5, width = 20, textvariable = selection, font = ('Times New Roman',18))
            menu6['values'] = ['18-25','25-35','35-42','42-50','50-60','60+']
            menu6['state'] = 'readonly'
            menu6.place(x=350,y=120)

            slabel3 = Label(Frame5,text = 'Enter Phone Number  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
            slabel3.place(x=60,y=190)
            elbael3 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
            elbael3.place(x=350,y=190, height=37, width=270)
            slabel4 = Label(Frame5,text = 'Enter Email-ID  :',font=('Times New Roman',22),fg='goldenrod',bg='mintcream') 
            slabel4.place(x=60,y=260)
            elbael4 = Entry(Frame5, font=('Times New Roman', 18), bg='khaki', fg='purple',bd=0)
            elbael4.place(x=350,y=260, height=37, width=270)
            ebtn6 = Button(Frame5, text='Proceed', bg='slateblue', fg='white' , font = ('Times New Roman',18), command= next1)
            ebtn6.place(x=350, y=450)

        Frame1 = Frame(root4,bg='darksalmon')
        Frame1.place(x=0,y=0, height=768, width=330)

        ebtn1 = Button(Frame1, text = 'Customer Details', font=('Times New Roman',18),bg='darksalmon',width=25,bd=0)
        ebtn1.place(x=0,y=150)
        ebtn2 = Button(Frame1, text = 'Purchase Details', font=('Times New Roman',18),bg='darksalmon',width=25,bd=0)
        ebtn2.place(x=0,y=300)
        ebtn3 = Button(Frame1, text = 'Finalize', font=('Times New Roman',18),bg='darksalmon',width=25,bd=0)
        ebtn3.place(x=0,y=450)
        

        Frame3 = Frame(root4,bg='khaki')
        Frame3.place(x=0,y=660, height=50, width=330)
        Frame2 = Frame(root4, bg='purple')
        Frame2.place(x=0,y=700,height=50,width=1366)

        elbl1 = Label(Frame2,text='Dhanbad Retail Bazar',font=('Times New Roman',22),fg='white',bg='purple')
        elbl1.place(x=580,y=0)

        def time():
            string = strftime('%Y-%m-%d %H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(Frame3, font=("Times New Roman",18), fg='purple', bg='khaki')
        lbl.place(x=30,y=0)
        time()

        start()

        root4.mainloop()

    def businessinsider(self):

        con = pymysql.connect(host='localhost',user='root',password='Yash@2310', database='retail')
        cur = con.cursor()

        root.withdraw()
        root4 = Toplevel()
        root4.geometry('1366x768')
        root4.title('Business Insights')
        root4.resizable(0,0)
        root4.configure(bg='coral1')
        root4.state('zoomed')
        root4.iconbitmap('icon1.ico')

        def countdown(time):
            if time == 0:
                root4.destroy()
            else:
                root4.after(500, countdown, time-1)

        def close():
             if messagebox.askokcancel("EXIT", "End Analysis Session?"):
                root4.destroy()
                root.deiconify()
        root4.protocol("WM_DELETE_WINDOW", close)    

        Frame1 = Frame(root4,bg='khaki')
        Frame1.place(x=35,y=30, height=680, width=1300)

        Frame2 = Frame(Frame1,bg='dark salmon')
        Frame2.place(x=0,y=0, height=680, width=300) 

        def monthlysales():
            cur.execute("select DISTINCT(select year(DOSL)) from sale_1")
            my_values1 = cur.fetchall()
            selected = tk.StringVar()
            menu1 = ttk.Combobox(Frame1, width = 20, textvariable = selected, font = ('Times New Roman',18))
            menu1['values'] = my_values1
            menu1['state'] = 'readonly'
            menu1.place(x=360,y=30)
            
        ubtn1 = Button(Frame2, text = 'Monthly Sales', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0, command=monthlysales )
        ubtn1.place(x=0,y=80)
        ubtn2 = Button(Frame2, text = 'MoM Sales', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0)
        ubtn2.place(x=0,y=160)
        ubtn3 = Button(Frame2, text = 'Annual Sales', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0)
        ubtn3.place(x=0,y=240)
        ubtn4 = Button(Frame2, text = 'YoY Sales', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0)
        ubtn4.place(x=0,y=320)
        ubtn5 = Button(Frame2, text = 'Nett Margins', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0)
        ubtn5.place(x=0,y=400)
        ubtn6 = Button(Frame2, text = 'Nett Sales', font=('Times New Roman',18),bg='dark salmon',width=25,bd=0)
        ubtn6.place(x=0,y=480)

        countdown(10)
        root4.mainloop()

    def __init__(self,root):

        self.root = root
        self.root.title("Retail Management Application")
        self.root.geometry('1366x768')
        self.root.resizable(False,False)
        root.configure(bg='moccasin')
        root.state('zoomed')
        self.bg1=PhotoImage(file='E:\Coding Projects\Codes\photo1.png')
        
        heading = Label(root, text='Dhanbad Retail Bazaar', fg= 'Blue', bg='moccasin', font=("Times New Roman",28)).place(x=480,y=20)
        Frame_sales=Frame(self.root,bg="moccasin")
        Frame_sales.place(x=100,y=150,height=420,width=450)

        self.bg_image=Label(Frame_sales,image=self.bg1)
        self.bg_image.place(x=0,y=0,relheight=1,relwidth=1)
        
        toggle_btn1=Button(Frame_sales, text='CUSTOMER INVOICE',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2', command=self.newbill )
        toggle_btn1.place(x=90, y=70)
        toggle_btn2=Button(Frame_sales, text='RETAIL INVOICE',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2',command= self.purchasebill)
        toggle_btn2.place(x=90, y=170)
        toggle_btn3=Button(Frame_sales, text='INVOICE MANAGER',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2', command= self.managebills)
        toggle_btn3.place(x=90, y=270)

        self.bg2=PhotoImage(file='E:\Coding Projects\Codes\photo1.png')

        Frame_notice=Frame(self.root,bg='azure')
        Frame_notice.place(x=770,y=150,height=420,width=450)

        self.bg_image=Label(Frame_notice,image=self.bg2)
        self.bg_image.place(x=0,y=0,relheight=1,relwidth=1)

        toggle_btn1=Button(Frame_notice, text='MANAGE STOCKS',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2')
        toggle_btn1.place(x=90, y=70)
        toggle_btn2=Button(Frame_notice, text='MANAGE PAYMENTS',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2')
        toggle_btn2.place(x=90, y=170)
        toggle_btn3=Button(Frame_notice, text='BUSINESS INSIGHTS',bg='gold',fg='blue',font=('Times New Roman',18),bd=0, height=2, width=20, cursor='hand2', command=self.businessinsider)
        toggle_btn3.place(x=90, y=270)

        def time():
            string = strftime('%Y-%m-%d %H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(root, font=("Times New Roman",18), fg='purple', bg='moccasin')
        lbl.place(x=10,y=700)
        time()
        messagebox.showinfo("Note","This software is meant for Store Managers only.")

        root.mainloop()

root=Tk()    
obj = Login(root)