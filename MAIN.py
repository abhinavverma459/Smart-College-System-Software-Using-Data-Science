import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import csv

screen=tkinter.Tk()
screen.geometry("1380x640+0+0")
screen.title("SMART COLLEGE SYSTEM SOFTWARE")
screen.iconbitmap('LOGO.ico')

def LOGIN():  # for Login the administrator
    adminstrator=A1.get()
    password=B1.get()
    
    if adminstrator == "root" and password == "root" :
        messagebox.showinfo("STATUS","LOGIN SUCCESSFULLY..")
        t=Toplevel(screen)
        t.geometry("1380x640+0+0")
        t.title("ADMINSTRATIR LOGIN")
        t.iconbitmap('LOGO.ico')
        
        def STUDENT_SUPERVISION(): # for Student Supervision Screen
            ss=Toplevel(t)
            ss.geometry("1380x640+0+0")
            ss.title("STUDENT SUPERVISION")
            ss.iconbitmap('LOGO.ico')
            
            def enter1():
                
                Twelfth=twelfth_marks_entry.get()
                
                
                if Twelfth >= '85':
                    
                    def genrate():
                        
                        lower="abcdefghijklmnopqrstuvwxyz"
                        upper="ABCDEFGHIJKLMNOPQRSTUVWXTZ"
                        numbers="0123456789"
                        symbols="!@#$%^&*()_+=?><]["
                        all_chars= lower + upper + numbers + symbols
                        length=10
                        
                        password1= ''.join(random.sample(all_chars,length))
                        
                        print1=Label(SS_Home1,text=password1,font=25)
                        print1.place(x=650,y=435)
                        
                    def ID():
                        
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        a1=int(id_entry.get())
                        a2=str(name_entry.get())
                        a3=int(dob_entry.get())
                        a4=int(mobile_no_entry.get())
                        a5=str(email_id_entry.get())
                        a6=int(aadhar_no_entry.get())
                        a7=int(tenth_marks_entry.get())
                        a8=int(tenth_year_entry.get())
                        a9=int(twelfth_marks_entry.get())
                        a10=int(twelfth_year_entry.get())
                        a11=int(session_entry.get())
                        a12=str(branch1.get())
                        a13=int(roll_no_entry.get())
                        a14=str(father_name_entry.get())
                        a15=str(mother_name_entry.get())
                        a16=int(father_mobile_entry.get())
                        a17=str(father_email_entry.get())
                        a18=int(mother_mobile_entry.get())
                        a19=str(Address_entry.get())
                        a20=int(Pincode_entry.get())
                        a21=str(s_password_entry.get())
                        sql="insert into students values('%d','%s','%d','%d','%s','%d','%d','%d','%d','%d','%d','%s','%d','%s','%s','%d','%s','%d','%s','%d','%s')"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21)
                        cur.execute(sql)
                        sql="select Student_Id,Student_Name,DOB,Student_Mobile_No,Aadhar_No,Session,Roll_No,Father_Name,Mother_Name,Father_Mobile_No,Mother_Mobile_No,Father_Email_Id,Address,Pincode from students where Student_Email_Id='%s'and Student_Id='%d'"%(a5,a1)
                        cur.execute(sql)
                        data=cur.fetchone()
                        r=list(data)
                        a={}
                        a['Student Id']=r[0]
                        a['Student Name']=r[1]
                        a['DOB']=r[2]
                        a['Student Mobile Number']=r[3]
                        a['Aadhar Number']=r[4]
                        a['Session']=r[5]
                        a['Roll Number']=r[6]
                        a['Father Name']=r[7]
                        a['Mother Name']=r[8]
                        a['Father Mobile Number']=r[9]
                        a['Mother Mobile Number']=r[10]
                        a['Father Email Id']=r[11]
                        a['Address']=r[12]
                        a['Pincode']=r[13]
                        def send_email(sender_email, password, recipient_email, subject, message):
                            try:
                                # Connect to SMTP server
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)

                                # Create MIMEText object for the email body
                                msg = MIMEMultipart()
                                msg['From'] = sender_email
                                msg['To'] = recipient_email
                                msg['Subject'] = subject

                                # Convert dictionary to a formatted string
                                message_text = "\n".join([f"{key}: {value}" for key, value in message.items()])
                                msg.attach(MIMEText(message_text, 'plain'))
            
                                # Send email
                                server.sendmail(sender_email, recipient_email, msg.as_string())
                                
                                print("Email sent successfully!")
                                server.quit()

                            except Exception as e:
                                print(f"Failed to send email. Error: {e}")

                        data= a
    
                        # Email configuration
                        sender_email = "ayushverma63210@gmail.com"
                        password = "neel ipmt hhtw undg"
                        recipient_email = "%s"%(a5)
                        subject = "CONGRATULATIONS..! Your Application Has Been Registered Successfully."
                        message =  data # Dictionary data to be sent in email body

                        # Call function to send email
                        send_email(sender_email, password, recipient_email, subject, message)

                        #print(a)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved and Emailed')
                        
                        
                    student_side=Label(SS_Home1,text="STUDENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    student_side.place(x=625,y=85)
                    
                    student_id=Label(SS_Home1,text="Student Id",font=5,bg="#1E90FF")
                    student_id.place(x=6,y=115)
                    id_entry=Entry(SS_Home1,width=30)
                    id_entry.place(x=180,y=120)
                    
                    student_name=Label(SS_Home1,text="Student Name",font=5,bg="#1E90FF")
                    student_name.place(x=450,y=115)
                    name_entry=Entry(SS_Home1,width=30)
                    name_entry.place(x=624,y=120)
                    
                    dob=Label(SS_Home1,text="DOB",font=5,bg="#1E90FF")
                    dob.place(x=864,y=115)
                    dob_entry=Entry(SS_Home1,width=30)
                    dob_entry.place(x=1035,y=120)
                    
                    mobile_no=Label(SS_Home1,text="Student Mobile No.",font=5,bg="#1E90FF")
                    mobile_no.place(x=6,y=155)
                    mobile_no_entry=Entry(SS_Home1,width=30)
                    mobile_no_entry.place(x=180,y=160)
                    
                    email_id=Label(SS_Home1,text="Student Email Id",font=5,bg="#1E90FF")
                    email_id.place(x=450,y=155)
                    email_id_entry=Entry(SS_Home1,width=30)
                    email_id_entry.place(x=624,y=160)
                    
                    aadhar_no=Label(SS_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
                    aadhar_no.place(x=864,y=155)
                    aadhar_no_entry=Entry(SS_Home1,width=30)
                    aadhar_no_entry.place(x=1035,y=160)
                    
                    tenth_marks=Label(SS_Home1,text="Tenth Marks",font=5,bg="#1E90FF")
                    tenth_marks.place(x=6,y=195)
                    tenth_marks_entry=Entry(SS_Home1,width=30)
                    tenth_marks_entry.place(x=180,y=200)
                    
                    tenth_year=Label(SS_Home1,text="Tenth Year",font=5,bg="#1E90FF")
                    tenth_year.place(x=450,y=195)
                    tenth_year_entry=Entry(SS_Home1,width=30)
                    tenth_year_entry.place(x=624,y=200)
                    
                    twelfth_year=Label(SS_Home1,text="Twelfth Year",font=5,bg="#1E90FF")
                    twelfth_year.place(x=864,y=195)
                    twelfth_year_entry=Entry(SS_Home1,width=30)
                    twelfth_year_entry.place(x=1035,y=200)
                    
                    session=Label(SS_Home1,text="Session",font=5,bg="#1E90FF")
                    session.place(x=6,y=235)
                    session_entry=Entry(SS_Home1,width=30)
                    session_entry.place(x=180,y=240)
                    
                    branch=Label(SS_Home1,text="Branch",font=5,bg="#1E90FF")
                    branch.place(x=450,y=235)
            
                    lt=['C.S.E','Bio.Tech','C.E','E.C.E','E.E','M.E','CIVIL']
                    branch1=ttk.Combobox(SS_Home1)
                    branch1['values']=lt
                    branch1.place(x=624,y=240)
                    
                    roll_no=Label(SS_Home1,text="Roll Number",font=5,bg="#1E90FF")
                    roll_no.place(x=864,y=235)
                    roll_no_entry=Entry(SS_Home1,width=30)
                    roll_no_entry.place(x=1035,y=240)
                    
                    parent_side=Label(SS_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    parent_side.place(x=625,y=275)
                    
                    father_name=Label(SS_Home1,text="Father Name",font=5,bg="#1E90FF")
                    father_name.place(x=6,y=315)
                    father_name_entry=Entry(SS_Home1,width=30)
                    father_name_entry.place(x=180,y=320)
                    
                    mother_name=Label(SS_Home1,text="Mother Name",font=5,bg="#1E90FF")
                    mother_name.place(x=450,y=315)
                    mother_name_entry=Entry(SS_Home1,width=30)
                    mother_name_entry.place(x=624,y=320)
                    
                    father_mobile=Label(SS_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
                    father_mobile.place(x=6,y=355)
                    father_mobile_entry=Entry(SS_Home1,width=30)
                    father_mobile_entry.place(x=180,y=360)
                    
                    mother_mobile=Label(SS_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
                    mother_mobile.place(x=450,y=355)
                    mother_mobile_entry=Entry(SS_Home1,width=30)
                    mother_mobile_entry.place(x=624,y=360)
                    
                    father_email=Label(SS_Home1,text="Father Email Id",font=5,bg="#1E90FF")
                    father_email.place(x=864,y=355)
                    father_email_entry=Entry(SS_Home1,width=30)
                    father_email_entry.place(x=1035,y=360)
                    
                    Address=Label(SS_Home1,text="Address",font=5,bg="#1E90FF")
                    Address.place(x=6,y=395)
                    Address_entry=Entry(SS_Home1,width=30)
                    Address_entry.place(x=180,y=400)
            
                    Pincode=Label(SS_Home1,text="Pincode",font=5,bg="#1E90FF")
                    Pincode.place(x=450,y=395)
                    Pincode_entry=Entry(SS_Home1,width=30)
                    Pincode_entry.place(x=624,y=400)
                    
                    s_password=Label(SS_Home1,text="Student Password",font=5,bg="#1E90FF")
                    s_password.place(x=6,y=435)
                    s_password_entry=Entry(SS_Home1,width=30)
                    s_password_entry.place(x=180,y=440)
                    
                    genrate=Button(SS_Home1,text="GENRATE",width=10,font=2,bg='blue',fg='white',command=genrate)
                    genrate.place(x=450,y=430)
                    
                    insert_details=Button(SS_Home1,text="INSERT DETAILS",width=15,font=20,bg='blue',fg='white',command=ID)
                    insert_details.place(x=6,y=480)
                    
                    def close_back():
                        ss.destroy()
            
                    Loginback=Button(SS_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=close_back)
                    Loginback.place(x=982,y=530)
                
                elif Twelfth >= '80' and Twelfth < '85' :
                    
                    def genrate():
                        
                        lower="abcdefghijklmnopqrstuvwxyz"
                        upper="ABCDEFGHIJKLMNOPQRSTUVWXTZ"
                        numbers="0123456789"
                        symbols="!@#$%^&*()_+=?><]["
                        all_chars= lower + upper + numbers + symbols
                        length=10
                        
                        password1= ''.join(random.sample(all_chars,length))
                        
                        print1=Label(SS_Home1,text=password1,font=25)
                        print1.place(x=650,y=435)
                        
                    def ID():
                        
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        a1=int(id_entry.get())
                        a2=str(name_entry.get())
                        a3=int(dob_entry.get())
                        a4=int(mobile_no_entry.get())
                        a5=str(email_id_entry.get())
                        a6=int(aadhar_no_entry.get())
                        a7=int(tenth_marks_entry.get())
                        a8=int(tenth_year_entry.get())
                        a9=int(twelfth_marks_entry.get())
                        a10=int(twelfth_year_entry.get())
                        a11=int(session_entry.get())
                        a12=str(branch1.get())
                        a13=int(roll_no_entry.get())
                        a14=str(father_name_entry.get())
                        a15=str(mother_name_entry.get())
                        a16=int(father_mobile_entry.get())
                        a17=str(father_email_entry.get())
                        a18=int(mother_mobile_entry.get())
                        a19=str(Address_entry.get())
                        a20=int(Pincode_entry.get())
                        a21=str(s_password_entry.get())
                        sql="insert into students values('%d','%s','%d','%d','%s','%d','%d','%d','%d','%d','%d','%s','%d','%s','%s','%d','%s','%d','%s','%d','%s')"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21)
                        cur.execute(sql)
                        sql="select Student_Id,Student_Name,DOB,Student_Mobile_No,Aadhar_No,Session,Roll_No,Father_Name,Mother_Name,Father_Mobile_No,Mother_Mobile_No,Father_Email_Id,Address,Pincode from students where Student_Email_Id='%s'and Student_Id='%d'"%(a5,a1)
                        cur.execute(sql)
                        data=cur.fetchone()
                        r=list(data)
                        a={}
                        a['Student Id']=r[0]
                        a['Student Name']=r[1]
                        a['DOB']=r[2]
                        a['Student Mobile Number']=r[3]
                        a['Aadhar Number']=r[4]
                        a['Session']=r[5]
                        a['Roll Number']=r[6]
                        a['Father Name']=r[7]
                        a['Mother Name']=r[8]
                        a['Father Mobile Number']=r[9]
                        a['Mother Mobile Number']=r[10]
                        a['Father Email Id']=r[11]
                        a['Address']=r[12]
                        a['Pincode']=r[13]
                        def send_email(sender_email, password, recipient_email, subject, message):
                            try:
                                # Connect to SMTP server
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)

                                # Create MIMEText object for the email body
                                msg = MIMEMultipart()
                                msg['From'] = sender_email
                                msg['To'] = recipient_email
                                msg['Subject'] = subject

                                # Convert dictionary to a formatted string
                                message_text = "\n".join([f"{key}: {value}" for key, value in message.items()])
                                msg.attach(MIMEText(message_text, 'plain'))
            
                                # Send email
                                server.sendmail(sender_email, recipient_email, msg.as_string())
                                
                                print("Email sent successfully!")
                                server.quit()

                            except Exception as e:
                                print(f"Failed to send email. Error: {e}")

                        data= a
    
                        # Email configuration
                        sender_email = "ayushverma63210@gmail.com"
                        password = "neel ipmt hhtw undg"
                        recipient_email = "%s"%(a5)
                        subject = "CONGRATULATIONS..! Your Application Has Been Registered Successfully."
                        message =  data # Dictionary data to be sent in email body

                        # Call function to send email
                        send_email(sender_email, password, recipient_email, subject, message)

                        #print(a)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved and Emailed')
                    
                    student_side=Label(SS_Home1,text="STUDENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    student_side.place(x=625,y=85)
                    
                    student_id=Label(SS_Home1,text="Student Id",font=5,bg="#1E90FF")
                    student_id.place(x=6,y=115)
                    id_entry=Entry(SS_Home1,width=30)
                    id_entry.place(x=180,y=120)
                    
                    student_name=Label(SS_Home1,text="Student Name",font=5,bg="#1E90FF")
                    student_name.place(x=450,y=115)
                    name_entry=Entry(SS_Home1,width=30)
                    name_entry.place(x=624,y=120)
                    
                    dob=Label(SS_Home1,text="DOB",font=5,bg="#1E90FF")
                    dob.place(x=864,y=115)
                    dob_entry=Entry(SS_Home1,width=30)
                    dob_entry.place(x=1035,y=120)
                    
                    mobile_no=Label(SS_Home1,text="Student Mobile No.",font=5,bg="#1E90FF")
                    mobile_no.place(x=6,y=155)
                    mobile_no_entry=Entry(SS_Home1,width=30)
                    mobile_no_entry.place(x=180,y=160)
                    
                    email_id=Label(SS_Home1,text="Student Email Id",font=5,bg="#1E90FF")
                    email_id.place(x=450,y=155)
                    email_id_entry=Entry(SS_Home1,width=30)
                    email_id_entry.place(x=624,y=160)
                    
                    aadhar_no=Label(SS_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
                    aadhar_no.place(x=864,y=155)
                    aadhar_no_entry=Entry(SS_Home1,width=30)
                    aadhar_no_entry.place(x=1035,y=160)
                    
                    tenth_marks=Label(SS_Home1,text="Tenth Marks",font=5,bg="#1E90FF")
                    tenth_marks.place(x=6,y=195)
                    tenth_marks_entry=Entry(SS_Home1,width=30)
                    tenth_marks_entry.place(x=180,y=200)
                    
                    tenth_year=Label(SS_Home1,text="Tenth Year",font=5,bg="#1E90FF")
                    tenth_year.place(x=450,y=195)
                    tenth_year_entry=Entry(SS_Home1,width=30)
                    tenth_year_entry.place(x=624,y=200)
                    
                    twelfth_year=Label(SS_Home1,text="Twelfth Year",font=5,bg="#1E90FF")
                    twelfth_year.place(x=864,y=195)
                    twelfth_year_entry=Entry(SS_Home1,width=30)
                    twelfth_year_entry.place(x=1035,y=200)
                    
                    session=Label(SS_Home1,text="Session",font=5,bg="#1E90FF")
                    session.place(x=6,y=235)
                    session_entry=Entry(SS_Home1,width=30)
                    session_entry.place(x=180,y=240)
                    
                    branch=Label(SS_Home1,text="Branch",font=5,bg="#1E90FF")
                    branch.place(x=450,y=235)
            
                    lt=['E.C.E','E.E','M.E','CIVIL']
                    branch1=ttk.Combobox(SS_Home1)
                    branch1['values']=lt
                    branch1.place(x=624,y=240)
                    
                    roll_no=Label(SS_Home1,text="Roll Number",font=5,bg="#1E90FF")
                    roll_no.place(x=864,y=235)
                    roll_no_entry=Entry(SS_Home1,width=30)
                    roll_no_entry.place(x=1035,y=240)
                    
                    parent_side=Label(SS_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    parent_side.place(x=625,y=275)
                    
                    father_name=Label(SS_Home1,text="Father Name",font=5,bg="#1E90FF")
                    father_name.place(x=6,y=315)
                    father_name_entry=Entry(SS_Home1,width=30)
                    father_name_entry.place(x=180,y=320)
                    
                    mother_name=Label(SS_Home1,text="Mother Name",font=5,bg="#1E90FF")
                    mother_name.place(x=450,y=315)
                    mother_name_entry=Entry(SS_Home1,width=30)
                    mother_name_entry.place(x=624,y=320)
                    
                    father_mobile=Label(SS_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
                    father_mobile.place(x=6,y=355)
                    father_mobile_entry=Entry(SS_Home1,width=30)
                    father_mobile_entry.place(x=180,y=360)
                    
                    mother_mobile=Label(SS_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
                    mother_mobile.place(x=450,y=355)
                    mother_mobile_entry=Entry(SS_Home1,width=30)
                    mother_mobile_entry.place(x=624,y=360)
                    
                    father_email=Label(SS_Home1,text="Father Email Id",font=5,bg="#1E90FF")
                    father_email.place(x=864,y=355)
                    father_email_entry=Entry(SS_Home1,width=30)
                    father_email_entry.place(x=1035,y=360)
                    
                    Address=Label(SS_Home1,text="Address",font=5,bg="#1E90FF")
                    Address.place(x=6,y=395)
                    Address_entry=Entry(SS_Home1,width=30)
                    Address_entry.place(x=180,y=400)
            
                    Pincode=Label(SS_Home1,text="Pincode",font=5,bg="#1E90FF")
                    Pincode.place(x=450,y=395)
                    Pincode_entry=Entry(SS_Home1,width=30)
                    Pincode_entry.place(x=624,y=400)
                    
                    s_password=Label(SS_Home1,text="Student Password",font=5,bg="#1E90FF")
                    s_password.place(x=6,y=435)
                    s_password_entry=Entry(SS_Home1,width=30)
                    s_password_entry.place(x=180,y=440)
                    
                    genrate=Button(SS_Home1,text="GENRATE",width=10,font=2,bg='blue',fg='white',command=genrate)
                    genrate.place(x=450,y=430)
                    
                    insert_details=Button(SS_Home1,text="INSERT DETAILS",width=15,font=20,bg='blue',fg='white',command=ID)
                    insert_details.place(x=6,y=480)
                    
                    def close_back():
                        ss.destroy()
            
                    Loginback=Button(SS_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=close_back)
                    Loginback.place(x=982,y=530)
                    
                elif Twelfth >= '75' and Twelfth < '80' :
                    
                    def genrate():
                        
                        lower="abcdefghijklmnopqrstuvwxyz"
                        upper="ABCDEFGHIJKLMNOPQRSTUVWXTZ"
                        numbers="0123456789"
                        symbols="!@#$%^&*()_+=?><]["
                        all_chars= lower + upper + numbers + symbols
                        length=10
                        
                        password1= ''.join(random.sample(all_chars,length))
                        
                        print1=Label(SS_Home1,text=password1,font=25)
                        print1.place(x=650,y=435)
                        
                    def ID():
                        
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        a1=int(id_entry.get())
                        a2=str(name_entry.get())
                        a3=int(dob_entry.get())
                        a4=int(mobile_no_entry.get())
                        a5=str(email_id_entry.get())
                        a6=int(aadhar_no_entry.get())
                        a7=int(tenth_marks_entry.get())
                        a8=int(tenth_year_entry.get())
                        a9=int(twelfth_marks_entry.get())
                        a10=int(twelfth_year_entry.get())
                        a11=int(session_entry.get())
                        a12=str(branch1.get())
                        a13=int(roll_no_entry.get())
                        a14=str(father_name_entry.get())
                        a15=str(mother_name_entry.get())
                        a16=int(father_mobile_entry.get())
                        a17=str(father_email_entry.get())
                        a18=int(mother_mobile_entry.get())
                        a19=str(Address_entry.get())
                        a20=int(Pincode_entry.get())
                        a21=str(s_password_entry.get())
                        sql="insert into students values('%d','%s','%d','%d','%s','%d','%d','%d','%d','%d','%d','%s','%d','%s','%s','%d','%s','%d','%s','%d','%s')"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21)
                        cur.execute(sql)
                        sql="select Student_Id,Student_Name,DOB,Student_Mobile_No,Aadhar_No,Session,Roll_No,Father_Name,Mother_Name,Father_Mobile_No,Mother_Mobile_No,Father_Email_Id,Address,Pincode from students where Student_Email_Id='%s'and Student_Id='%d'"%(a5,a1)
                        cur.execute(sql)
                        data=cur.fetchone()
                        r=list(data)
                        a={}
                        a['Student Id']=r[0]
                        a['Student Name']=r[1]
                        a['DOB']=r[2]
                        a['Student Mobile Number']=r[3]
                        a['Aadhar Number']=r[4]
                        a['Session']=r[5]
                        a['Roll Number']=r[6]
                        a['Father Name']=r[7]
                        a['Mother Name']=r[8]
                        a['Father Mobile Number']=r[9]
                        a['Mother Mobile Number']=r[10]
                        a['Father Email Id']=r[11]
                        a['Address']=r[12]
                        a['Pincode']=r[13]
                        def send_email(sender_email, password, recipient_email, subject, message):
                            try:
                                # Connect to SMTP server
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)

                                # Create MIMEText object for the email body
                                msg = MIMEMultipart()
                                msg['From'] = sender_email
                                msg['To'] = recipient_email
                                msg['Subject'] = subject

                                # Convert dictionary to a formatted string
                                message_text = "\n".join([f"{key}: {value}" for key, value in message.items()])
                                msg.attach(MIMEText(message_text, 'plain'))
            
                                # Send email
                                server.sendmail(sender_email, recipient_email, msg.as_string())
                                
                                print("Email sent successfully!")
                                server.quit()

                            except Exception as e:
                                print(f"Failed to send email. Error: {e}")

                        data= a
    
                        # Email configuration
                        sender_email = "ayushverma63210@gmail.com"
                        password = "neel ipmt hhtw undg"
                        recipient_email = "%s"%(a5)
                        subject = "CONGRATULATIONS..! Your Application Has Been Registered Successfully."
                        message =  data # Dictionary data to be sent in email body

                        # Call function to send email
                        send_email(sender_email, password, recipient_email, subject, message)

                        #print(a)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved and Emailed')
                    
                    student_side=Label(SS_Home1,text="STUDENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    student_side.place(x=625,y=85)
                    
                    student_id=Label(SS_Home1,text="Student Id",font=5,bg="#1E90FF")
                    student_id.place(x=6,y=115)
                    id_entry=Entry(SS_Home1,width=30)
                    id_entry.place(x=180,y=120)
                    
                    student_name=Label(SS_Home1,text="Student Name",font=5,bg="#1E90FF")
                    student_name.place(x=450,y=115)
                    name_entry=Entry(SS_Home1,width=30)
                    name_entry.place(x=624,y=120)
                    
                    dob=Label(SS_Home1,text="DOB",font=5,bg="#1E90FF")
                    dob.place(x=864,y=115)
                    dob_entry=Entry(SS_Home1,width=30)
                    dob_entry.place(x=1035,y=120)
                    
                    mobile_no=Label(SS_Home1,text="Student Mobile No.",font=5,bg="#1E90FF")
                    mobile_no.place(x=6,y=155)
                    mobile_no_entry=Entry(SS_Home1,width=30)
                    mobile_no_entry.place(x=180,y=160)
                    
                    email_id=Label(SS_Home1,text="Student Email Id",font=5,bg="#1E90FF")
                    email_id.place(x=450,y=155)
                    email_id_entry=Entry(SS_Home1,width=30)
                    email_id_entry.place(x=624,y=160)
                    
                    aadhar_no=Label(SS_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
                    aadhar_no.place(x=864,y=155)
                    aadhar_no_entry=Entry(SS_Home1,width=30)
                    aadhar_no_entry.place(x=1035,y=160)
                    
                    tenth_marks=Label(SS_Home1,text="Tenth Marks",font=5,bg="#1E90FF")
                    tenth_marks.place(x=6,y=195)
                    tenth_marks_entry=Entry(SS_Home1,width=30)
                    tenth_marks_entry.place(x=180,y=200)
                    
                    tenth_year=Label(SS_Home1,text="Tenth Year",font=5,bg="#1E90FF")
                    tenth_year.place(x=450,y=195)
                    tenth_year_entry=Entry(SS_Home1,width=30)
                    tenth_year_entry.place(x=624,y=200)
                    
                    twelfth_year=Label(SS_Home1,text="Twelfth Year",font=5,bg="#1E90FF")
                    twelfth_year.place(x=864,y=195)
                    twelfth_year_entry=Entry(SS_Home1,width=30)
                    twelfth_year_entry.place(x=1035,y=200)
                    
                    session=Label(SS_Home1,text="Session",font=5,bg="#1E90FF")
                    session.place(x=6,y=235)
                    session_entry=Entry(SS_Home1,width=30)
                    session_entry.place(x=180,y=240)
                    
                    branch=Label(SS_Home1,text="Branch",font=5,bg="#1E90FF")
                    branch.place(x=450,y=235)
            
                    lt=['M.E','CIVIL']
                    branch1=ttk.Combobox(SS_Home1)
                    branch1['values']=lt
                    branch1.place(x=624,y=240)
                    
                    roll_no=Label(SS_Home1,text="Roll Number",font=5,bg="#1E90FF")
                    roll_no.place(x=864,y=235)
                    roll_no_entry=Entry(SS_Home1,width=30)
                    roll_no_entry.place(x=1035,y=240)
                    
                    parent_side=Label(SS_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    parent_side.place(x=625,y=275)
                    
                    father_name=Label(SS_Home1,text="Father Name",font=5,bg="#1E90FF")
                    father_name.place(x=6,y=315)
                    father_name_entry=Entry(SS_Home1,width=30)
                    father_name_entry.place(x=180,y=320)
                    
                    mother_name=Label(SS_Home1,text="Mother Name",font=5,bg="#1E90FF")
                    mother_name.place(x=450,y=315)
                    mother_name_entry=Entry(SS_Home1,width=30)
                    mother_name_entry.place(x=624,y=320)
                    
                    father_mobile=Label(SS_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
                    father_mobile.place(x=6,y=355)
                    father_mobile_entry=Entry(SS_Home1,width=30)
                    father_mobile_entry.place(x=180,y=360)
                    
                    mother_mobile=Label(SS_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
                    mother_mobile.place(x=450,y=355)
                    mother_mobile_entry=Entry(SS_Home1,width=30)
                    mother_mobile_entry.place(x=624,y=360)
                    
                    father_email=Label(SS_Home1,text="Father Email Id",font=5,bg="#1E90FF")
                    father_email.place(x=864,y=355)
                    father_email_entry=Entry(SS_Home1,width=30)
                    father_email_entry.place(x=1035,y=360)
                    
                    Address=Label(SS_Home1,text="Address",font=5,bg="#1E90FF")
                    Address.place(x=6,y=395)
                    Address_entry=Entry(SS_Home1,width=30)
                    Address_entry.place(x=180,y=400)
            
                    Pincode=Label(SS_Home1,text="Pincode",font=5,bg="#1E90FF")
                    Pincode.place(x=450,y=395)
                    Pincode_entry=Entry(SS_Home1,width=30)
                    Pincode_entry.place(x=624,y=400)
                    
                    s_password=Label(SS_Home1,text="Student Password",font=5,bg="#1E90FF")
                    s_password.place(x=6,y=435)
                    s_password_entry=Entry(SS_Home1,width=30)
                    s_password_entry.place(x=180,y=440)
                    
                    genrate=Button(SS_Home1,text="GENRATE",width=10,font=2,bg='blue',fg='white',command=genrate)
                    genrate.place(x=450,y=430)
                    
                    insert_details=Button(SS_Home1,text="INSERT DETAILS",width=15,font=20,bg='blue',fg='white',command=ID)
                    insert_details.place(x=6,y=480)
                    
                    def close_back():
                        ss.destroy()
            
                    Loginback=Button(SS_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=close_back)
                    Loginback.place(x=982,y=530)
                    
                elif Twelfth >= '60' and Twelfth < '75' :
                    
                    def genrate():
                        
                        lower="abcdefghijklmnopqrstuvwxyz"
                        upper="ABCDEFGHIJKLMNOPQRSTUVWXTZ"
                        numbers="0123456789"
                        symbols="!@#$%^&*()_+=?><]["
                        all_chars= lower + upper + numbers + symbols
                        length=10
                        
                        password1= ''.join(random.sample(all_chars,length))
                        
                        print1=Label(SS_Home1,text=password1,font=25)
                        print1.place(x=650,y=435)
                        
                    def ID():
                        
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        a1=int(id_entry.get())
                        a2=str(name_entry.get())
                        a3=int(dob_entry.get())
                        a4=int(mobile_no_entry.get())
                        a5=str(email_id_entry.get())
                        a6=int(aadhar_no_entry.get())
                        a7=int(tenth_marks_entry.get())
                        a8=int(tenth_year_entry.get())
                        a9=int(twelfth_marks_entry.get())
                        a10=int(twelfth_year_entry.get())
                        a11=int(session_entry.get())
                        a12=str(branch1.get())
                        a13=int(roll_no_entry.get())
                        a14=str(father_name_entry.get())
                        a15=str(mother_name_entry.get())
                        a16=int(father_mobile_entry.get())
                        a17=str(father_email_entry.get())
                        a18=int(mother_mobile_entry.get())
                        a19=str(Address_entry.get())
                        a20=int(Pincode_entry.get())
                        a21=str(s_password_entry.get())
                        sql="insert into students values('%d','%s','%d','%d','%s','%d','%d','%d','%d','%d','%d','%s','%d','%s','%s','%d','%s','%d','%s','%d','%s')"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21)
                        cur.execute(sql)
                        sql="select Student_Id,Student_Name,DOB,Student_Mobile_No,Aadhar_No,Session,Roll_No,Father_Name,Mother_Name,Father_Mobile_No,Mother_Mobile_No,Father_Email_Id,Address,Pincode from students where Student_Email_Id='%s'and Student_Id='%d'"%(a5,a1)
                        cur.execute(sql)
                        data=cur.fetchone()
                        r=list(data)
                        a={}
                        a['Student Id']=r[0]
                        a['Student Name']=r[1]
                        a['DOB']=r[2]
                        a['Student Mobile Number']=r[3]
                        a['Aadhar Number']=r[4]
                        a['Session']=r[5]
                        a['Roll Number']=r[6]
                        a['Father Name']=r[7]
                        a['Mother Name']=r[8]
                        a['Father Mobile Number']=r[9]
                        a['Mother Mobile Number']=r[10]
                        a['Father Email Id']=r[11]
                        a['Address']=r[12]
                        a['Pincode']=r[13]
                        def send_email(sender_email, password, recipient_email, subject, message):
                            try:
                                # Connect to SMTP server
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login(sender_email, password)

                                # Create MIMEText object for the email body
                                msg = MIMEMultipart()
                                msg['From'] = sender_email
                                msg['To'] = recipient_email
                                msg['Subject'] = subject

                                # Convert dictionary to a formatted string
                                message_text = "\n".join([f"{key}: {value}" for key, value in message.items()])
                                msg.attach(MIMEText(message_text, 'plain'))
            
                                # Send email
                                server.sendmail(sender_email, recipient_email, msg.as_string())
                                
                                print("Email sent successfully!")
                                server.quit()

                            except Exception as e:
                                print(f"Failed to send email. Error: {e}")

                        data= a
    
                        # Email configuration
                        sender_email = "ayushverma63210@gmail.com"
                        password = "neel ipmt hhtw undg"
                        recipient_email = "%s"%(a5)
                        subject = "CONGRATULATIONS..! Your Application Has Been Registered Successfully."
                        message =  data # Dictionary data to be sent in email body

                        # Call function to send email
                        send_email(sender_email, password, recipient_email, subject, message)

                        #print(a)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved')
                    
                    student_side=Label(SS_Home1,text="STUDENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    student_side.place(x=625,y=85)
                    
                    student_id=Label(SS_Home1,text="Student Id",font=5,bg="#1E90FF")
                    student_id.place(x=6,y=115)
                    id_entry=Entry(SS_Home1,width=30)
                    id_entry.place(x=180,y=120)
                    
                    student_name=Label(SS_Home1,text="Student Name",font=5,bg="#1E90FF")
                    student_name.place(x=450,y=115)
                    name_entry=Entry(SS_Home1,width=30)
                    name_entry.place(x=624,y=120)
                    
                    dob=Label(SS_Home1,text="DOB",font=5,bg="#1E90FF")
                    dob.place(x=864,y=115)
                    dob_entry=Entry(SS_Home1,width=30)
                    dob_entry.place(x=1035,y=120)
                    
                    mobile_no=Label(SS_Home1,text="Student Mobile No.",font=5,bg="#1E90FF")
                    mobile_no.place(x=6,y=155)
                    mobile_no_entry=Entry(SS_Home1,width=30)
                    mobile_no_entry.place(x=180,y=160)
                    
                    email_id=Label(SS_Home1,text="Student Email Id",font=5,bg="#1E90FF")
                    email_id.place(x=450,y=155)
                    email_id_entry=Entry(SS_Home1,width=30)
                    email_id_entry.place(x=624,y=160)
                    
                    aadhar_no=Label(SS_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
                    aadhar_no.place(x=864,y=155)
                    aadhar_no_entry=Entry(SS_Home1,width=30)
                    aadhar_no_entry.place(x=1035,y=160)
                    
                    tenth_marks=Label(SS_Home1,text="Tenth Marks",font=5,bg="#1E90FF")
                    tenth_marks.place(x=6,y=195)
                    tenth_marks_entry=Entry(SS_Home1,width=30)
                    tenth_marks_entry.place(x=180,y=200)
                    
                    tenth_year=Label(SS_Home1,text="Tenth Year",font=5,bg="#1E90FF")
                    tenth_year.place(x=450,y=195)
                    tenth_year_entry=Entry(SS_Home1,width=30)
                    tenth_year_entry.place(x=624,y=200)
                    
                    twelfth_year=Label(SS_Home1,text="Twelfth Year",font=5,bg="#1E90FF")
                    twelfth_year.place(x=864,y=195)
                    twelfth_year_entry=Entry(SS_Home1,width=30)
                    twelfth_year_entry.place(x=1035,y=200)
                    
                    session=Label(SS_Home1,text="Session",font=5,bg="#1E90FF")
                    session.place(x=6,y=235)
                    session_entry=Entry(SS_Home1,width=30)
                    session_entry.place(x=180,y=240)
                    
                    branch=Label(SS_Home1,text="Branch",font=5,bg="#1E90FF")
                    branch.place(x=450,y=235)
            
                    lt=['M.E']
                    branch1=ttk.Combobox(SS_Home1)
                    branch1['values']=lt
                    branch1.place(x=624,y=240)
                    
                    roll_no=Label(SS_Home1,text="Roll Number",font=5,bg="#1E90FF")
                    roll_no.place(x=864,y=235)
                    roll_no_entry=Entry(SS_Home1,width=30)
                    roll_no_entry.place(x=1035,y=240)
                    
                    parent_side=Label(SS_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                    parent_side.place(x=625,y=275)
                    
                    father_name=Label(SS_Home1,text="Father Name",font=5,bg="#1E90FF")
                    father_name.place(x=6,y=315)
                    father_name_entry=Entry(SS_Home1,width=30)
                    father_name_entry.place(x=180,y=320)
                    
                    mother_name=Label(SS_Home1,text="Mother Name",font=5,bg="#1E90FF")
                    mother_name.place(x=450,y=315)
                    mother_name_entry=Entry(SS_Home1,width=30)
                    mother_name_entry.place(x=624,y=320)
                    
                    father_mobile=Label(SS_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
                    father_mobile.place(x=6,y=355)
                    father_mobile_entry=Entry(SS_Home1,width=30)
                    father_mobile_entry.place(x=180,y=360)
                    
                    mother_mobile=Label(SS_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
                    mother_mobile.place(x=450,y=355)
                    mother_mobile_entry=Entry(SS_Home1,width=30)
                    mother_mobile_entry.place(x=624,y=360)
                    
                    father_email=Label(SS_Home1,text="Father Email Id",font=5,bg="#1E90FF")
                    father_email.place(x=864,y=355)
                    father_email_entry=Entry(SS_Home1,width=30)
                    father_email_entry.place(x=1035,y=360)
                    
                    Address=Label(SS_Home1,text="Address",font=5,bg="#1E90FF")
                    Address.place(x=6,y=395)
                    Address_entry=Entry(SS_Home1,width=30)
                    Address_entry.place(x=180,y=400)
            
                    Pincode=Label(SS_Home1,text="Pincode",font=5,bg="#1E90FF")
                    Pincode.place(x=450,y=395)
                    Pincode_entry=Entry(SS_Home1,width=30)
                    Pincode_entry.place(x=624,y=400)
                    
                    s_password=Label(SS_Home1,text="Student Password",font=5,bg="#1E90FF")
                    s_password.place(x=6,y=435)
                    s_password_entry=Entry(SS_Home1,width=30)
                    s_password_entry.place(x=180,y=440)
                    
                    genrate=Button(SS_Home1,text="GENRATE",width=10,font=2,bg='blue',fg='white',command=genrate)
                    genrate.place(x=450,y=430)
                    
                    insert_details=Button(SS_Home1,text="INSERT DETAILS",width=15,font=20,bg='blue',fg='white',command=ID)
                    insert_details.place(x=6,y=480)
                    
                    def close_back():
                        ss.destroy()
            
                    Loginback=Button(SS_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=close_back)
                    Loginback.place(x=982,y=530)
                    
                else:
                    
                    messagebox.showerror("ERROR","You Are Not Eligible To Take Admission")
                    ss.destroy()
                  
            def CD():
                cd=Toplevel(ss)
                cd.geometry("1380x640+0+0")
                cd.title("CHANGE DATA")
                cd.iconbitmap('LOGO.ico')
                
                def FD():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                    cur=db.cursor()
                    x=int(id_entry.get())
                    sql="select Student_Name,DOB,Student_Mobile_No,Student_Email_Id,Aadhar_No,Session,Roll_No,Father_Name,Mother_Name,Father_Mobile_No,Mother_Mobile_No,Father_Email_Id,Address,Pincode from students where Student_Id='%d'"%(x)
                    cur.execute(sql)
                    data=cur.fetchall()
                    if len(data)==0:
                        messagebox.showinfo('STATUS',"No records found")
                        cd.destroy()
                        ss.destroy()
                    else:
                        for res in data:
                            name_entry.insert(0,str(res[0]))
                            dob_entry.insert(0,int(res[1]))
                            mobile_no_entry.insert(0,int(res[2]))
                            email_id_entry.insert(0,str(res[3]))
                            aadhar_no_entry.insert(0,int(res[4]))
                            session_entry.insert(0,int(res[5]))
                            roll_no_entry.insert(0,int(res[6]))
                            father_name_entry.insert(0,str(res[7]))
                            mother_name_entry.insert(0,str(res[8]))
                            father_mobile_entry.insert(0,int(res[9]))
                            mother_mobile_entry.insert(0,int(res[10]))
                            father_email_entry.insert(0,str(res[11]))
                            Address_entry.insert(0,str(res[12]))
                            Pincode_entry.insert(0,int(res[13]))
                    db.close()
                    
                def UD():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                    cur=db.cursor()
                    x1=int(id_entry.get())
                    x2=str(name_entry.get())
                    x3=int(dob_entry.get())
                    x4=int(mobile_no_entry.get())
                    x5=str(email_id_entry.get())
                    x6=int(aadhar_no_entry.get())
                    x7=int(session_entry.get())
                    x8=int(roll_no_entry.get())
                    x9=str(father_name_entry.get())
                    x10=str(mother_name_entry.get())
                    x11=int(father_mobile_entry.get())
                    x12=int(mother_mobile_entry.get())
                    x13=str(father_email_entry.get())
                    x14=str(Address_entry.get())
                    x15=int(Pincode_entry.get())
                    sql=("update students set Student_Name='%s',DOB='%d',Student_Mobile_No='%d',Student_Email_Id='%s',Aadhar_No='%d',Session='%d',Roll_No='%d',Father_Name='%s',Mother_Name='%s',Father_Mobile_No='%d',Mother_Mobile_No='%d',Father_Email_Id='%s',Address='%s',Pincode='%d' where Student_Id='%d'")%(x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x1)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    messagebox.showinfo('STATUS','Data Updated')
                    cd.destroy()
                    ss.destroy()
                    
                def DD():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                    cur=db.cursor()
                    x11=int(id_entry.get())
                    sql="delete from students where Student_Id='%s'"%(x11)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    messagebox.showinfo("STATUS",'DELETED')
                    cd.destroy()
                    ss.destroy()
                    
                def CDB():
                    cd.destroy()
               
                
                CD_Home=Canvas(cd,width=1380,height=640,bg='#104E8B')
                CD_Home.place(x=0,y=0)
                
                CD_heading=Label(cd,text="CHANGE DATA",bg="#104E8B",fg="#F0FFFF",font=('Aeries',25))
                CD_heading.place(x=480,y=2)
                
                CD_Home1=Canvas(cd,width=1380,height=640,bg='#1E90FF')
                CD_Home1.place(x=0,y=50)
                
                student_side=Label(CD_Home1,text="Student side",font=25,bg="GREEN",fg="YELLOW")
                student_side.place(x=6,y=20)
                
                student_id=Label(CD_Home1,text="Student Id",font=5,bg="#1E90FF")
                student_id.place(x=6,y=50)
                id_entry=Entry(CD_Home1,width=30)
                id_entry.place(x=180,y=55)
                
                student_name=Label(CD_Home1,text="Student Name",font=5,bg="#1E90FF")
                student_name.place(x=450,y=50)
                name_entry=Entry(CD_Home1,width=30)
                name_entry.place(x=624,y=55)
                
                dob=Label(CD_Home1,text="DOB",font=5,bg="#1E90FF")
                dob.place(x=864,y=50)
                dob_entry=Entry(CD_Home1,width=30)
                dob_entry.place(x=1035,y=55)
            
                mobile_no=Label(CD_Home1,text="Student Mobile No.",font=5,bg="#1E90FF")
                mobile_no.place(x=6,y=90)
                mobile_no_entry=Entry(CD_Home1,width=30)
                mobile_no_entry.place(x=180,y=95)
            
                email_id=Label(CD_Home1,text="Student Email Id",font=5,bg="#1E90FF")
                email_id.place(x=450,y=90)
                email_id_entry=Entry(CD_Home1,width=30)
                email_id_entry.place(x=624,y=95)
            
                aadhar_no=Label(CD_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
                aadhar_no.place(x=864,y=90)
                aadhar_no_entry=Entry(CD_Home1,width=30)
                aadhar_no_entry.place(x=1035,y=95)
                
                session=Label(CD_Home1,text="Session",font=5,bg="#1E90FF")
                session.place(x=6,y=130)
                session_entry=Entry(CD_Home1,width=30)
                session_entry.place(x=180,y=130)
                
                roll_no=Label(CD_Home1,text="Roll Number",font=5,bg="#1E90FF")
                roll_no.place(x=450,y=130)
                roll_no_entry=Entry(CD_Home1,width=30)
                roll_no_entry.place(x=624,y=130)
                    
                parent_side=Label(CD_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
                parent_side.place(x=6,y=170)
                
                father_name=Label(CD_Home1,text="Father Name",font=5,bg="#1E90FF")
                father_name.place(x=6,y=200)
                father_name_entry=Entry(CD_Home1,width=30)
                father_name_entry.place(x=180,y=200)
                    
                mother_name=Label(CD_Home1,text="Mother Name",font=5,bg="#1E90FF")
                mother_name.place(x=450,y=200)
                mother_name_entry=Entry(CD_Home1,width=30)
                mother_name_entry.place(x=624,y=200)
                    
                father_mobile=Label(CD_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
                father_mobile.place(x=6,y=240)
                father_mobile_entry=Entry(CD_Home1,width=30)
                father_mobile_entry.place(x=180,y=240)
                    
                mother_mobile=Label(CD_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
                mother_mobile.place(x=450,y=240)
                mother_mobile_entry=Entry(CD_Home1,width=30)
                mother_mobile_entry.place(x=624,y=240)
                    
                father_email=Label(CD_Home1,text="Father Email Id",font=5,bg="#1E90FF")
                father_email.place(x=864,y=240)
                father_email_entry=Entry(CD_Home1,width=30)
                father_email_entry.place(x=1035,y=240)
                    
                Address=Label(CD_Home1,text="Address",font=5,bg="#1E90FF")
                Address.place(x=6,y=280)
                Address_entry=Entry(CD_Home1,width=30)
                Address_entry.place(x=180,y=280)
            
                Pincode=Label(CD_Home1,text="Pincode",font=5,bg="#1E90FF")
                Pincode.place(x=450,y=280)
                Pincode_entry=Entry(CD_Home1,width=30)
                Pincode_entry.place(x=624,y=280)
                
                find_details=Button(CD_Home1,text="FIND DETAILS",width=15,font=20,bg='blue',fg='white',command=FD)
                find_details.place(x=6,y=350)
                
                update_details=Button(CD_Home1,text="UPDATE DETAILS",width=15,font=20,bg='blue',fg='white',command=UD)
                update_details.place(x=450,y=350)
                
                delete_details=Button(CD_Home1,text="DELETE DETAILS",width=15,font=20,bg='blue',fg='white',command=DD)
                delete_details.place(x=864,y=350)
                
                Loginclose=Button(CD_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=CDB)
                Loginclose.place(x=1077,y=540)
                
                cd.mainloop()
                
            def SD():
                sd=Toplevel(ss)
                sd.geometry("1270x250+0+0")
                sd.title("SHOW STUDENTS DATA")
                sd.iconbitmap('LOGO.ico')

                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                sql="select * from students"
                cur.execute(sql)
     
                my_tree=ttk.Treeview(sd)

                #define columns
                my_tree['columns']=("Student_Id","Student_Name","DOB","Student_Mobile_No","Student_Email_Id","Aadhar_No","Tenth_Marks","Tenth_Year","Twelfth_Marks","Twelfth_Year","Session","Branch","Roll_No","Father_Name","Mother_Name","Father_Mobile_No","Father_Email_Id","Mother_Mobile_No","Address","Pincode","Password")

                #formate our columns
                my_tree.column('#0',width=0,stretch=NO)
                my_tree.column("Student_Id",anchor=W,width=80)
                my_tree.column("Student_Name",anchor=W,width=105)
                my_tree.column("DOB",anchor=W,width=60)
                my_tree.column("Student_Mobile_No",anchor=W,width=100)
                my_tree.column("Student_Email_Id",anchor=W,width=200)
                my_tree.column("Aadhar_No",anchor=W,width=100)
                my_tree.column("Tenth_Marks",anchor=W,width=80)
                my_tree.column("Tenth_Year",anchor=W,width=70)
                my_tree.column("Twelfth_Marks",anchor=W,width=90)
                my_tree.column("Twelfth_Year",anchor=W,width=80)
                my_tree.column("Session",anchor=W,width=100)
                my_tree.column("Branch",anchor=W,width=50)
                my_tree.column("Roll_No",anchor=W,width=100)
                my_tree.column("Father_Name",anchor=W,width=105)
                my_tree.column("Mother_Name",anchor=W,width=105)
                my_tree.column("Father_Mobile_No",anchor=W,width=100)
                my_tree.column("Father_Email_Id",anchor=W,width=200)
                my_tree.column("Mother_Mobile_No",anchor=W,width=100)
                my_tree.column("Address",anchor=W,width=100)
                my_tree.column("Pincode",anchor=W,width=100)
                my_tree.column("Password",anchor=W,width=100)

                #create headings
                my_tree.heading("#0",text="",anchor=W)
                my_tree.heading("Student_Id",text="Student Id",anchor=W)
                my_tree.heading("Student_Name",text="Student Name",anchor=W)
                my_tree.heading("DOB",text="DOB",anchor=W)
                my_tree.heading("Student_Mobile_No",text="Student No",anchor=W)
                my_tree.heading("Student_Email_Id",text="Student Email",anchor=W)
                my_tree.heading("Aadhar_No",text="Aadhar No",anchor=W)
                my_tree.heading("Tenth_Marks",text="Tenth Marks",anchor=W)
                my_tree.heading("Tenth_Year",text="Tenth year",anchor=W)
                my_tree.heading("Twelfth_Marks",text="Twelfth Marks",anchor=W)
                my_tree.heading("Twelfth_Year",text="Twelfth year",anchor=W)
                my_tree.heading("Session",text="Session",anchor=W)
                my_tree.heading("Branch",text="Branch",anchor=W)
                my_tree.heading("Roll_No",text="Roll No",anchor=W)
                my_tree.heading("Father_Name",text="Father Name",anchor=W)
                my_tree.heading("Mother_Name",text="Mother Name",anchor=W)
                my_tree.heading("Father_Mobile_No",text="Father No",anchor=W)
                my_tree.heading("Father_Email_Id",text="Father Email",anchor=W)
                my_tree.heading("Mother_Mobile_No",text="Mother No",anchor=W)
                my_tree.heading("Address",text="Address",anchor=W)
                my_tree.heading("Pincode",text="Pincode",anchor=W)
                my_tree.heading("Password",text="Password",anchor=W)

                count=0
                for record in cur:
                    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],
                    record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18],record[19],record[20]))
                    count += 1
    
                hsb=ttk.Scrollbar(sd,orient="horizontal")
                hsb.configure(command=my_tree.xview)
                my_tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X,side=BOTTOM)

                vsb=ttk.Scrollbar(sd,orient="vertical")
                vsb.configure(command=my_tree.yview)
                my_tree.configure(yscrollcommand=vsb.set)
                vsb.pack(fill=Y,side=RIGHT)
                
                my_tree.pack(padx=20,pady=50)

                sd.mainloop()
                       
              
            SS_Home=Canvas(ss,width=1380,height=640,bg='#104E8B')
            SS_Home.place(x=0,y=0)
            
            SS_heading=Label(ss,text="STUDENT SUPERVISION",bg="#104E8B",fg="#F0FFFF",font=('Aeries',25))
            SS_heading.place(x=480,y=2)
            
            SS_Home1=Canvas(ss,width=1380,height=640,bg='#1E90FF')
            SS_Home1.place(x=0,y=50)
            
            cut_off=Label(SS_Home1,text="CUT-OFF (12TH-MARKS)",font=25,bg="GREEN",fg="YELLOW")
            cut_off.place(x=6,y=20)
            
            twelfth_marks=Label(SS_Home1,text="Twelfth Marks",font=5,bg="#1E90FF")
            twelfth_marks.place(x=6,y=50)
            twelfth_marks_entry=Entry(SS_Home1,width=30)
            twelfth_marks_entry.place(x=200,y=55)
            
            enter=Button(SS_Home1,text="ENTER",width=7,font=2,bg='blue',fg='white',command=enter1)
            enter.place(x=450,y=45)
            
            change_data=Button(SS_Home1,text="CHANGE DATA",width=15,font=20,bg='blue',fg='white',command=CD)
            change_data.place(x=1080,y=10)
            
            show_data=Button(SS_Home1,text="SHOW DATA",width=15,font=20,bg='blue',fg='white',command=SD)
            show_data.place(x=1080,y=60)
            
            ss.mainloop()    # Student Supervision Cloased Screen
            
        def FACULTY_INFORMATION(): # for Faculty Information Screen
            fi=Toplevel(t)
            fi.geometry("1380x640+0+0")
            fi.title("TEACHER INFORMATION")
            fi.iconbitmap('LOGO.ico')
            
            def t_genrate():
                lower="abcdefghijklmnopqrstuvwxyz"
                upper="ABCDEFGHIJKLMNOPQRSTUVWXTZ"
                numbers="0123456789"
                symbols="!@#$%^&*()_+=?><]["
                all_chars= lower + upper + numbers + symbols
                length=10
    
                password1= ''.join(random.sample(all_chars,length))
    
                print2=Label(FI_Home1,text=password1,font=25)
                print2.place(x=640,y=400)
    
            def t_close_back():
                fi.destroy()
                
            def t_ID():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                t1=int(teacher_id_entry.get())
                t2=str(teacher_name_entry.get())
                t3=int(t_dob_entry.get())
                t4=int(teacher_mobile_no_entry.get())
                t5=str(t_email_id_entry.get())
                t6=int(t_aadhar_no_entry.get())
                t7=int(t_tenth_entry.get())
                t8=int(t_twelfth_entry.get())
                t9=int(t_graduation_entry.get())
                t10=str(t_father_name_entry.get())
                t11=str(t_mother_name_entry.get())
                t12=int(t_father_mobile_entry.get())
                t13=str(t_father_email_entry.get())
                t14=int(t_mother_mobile_entry.get())
                t15=str(t_Address_entry.get())
                t16=int(t_Pincode_entry.get())
                t17=int(joining_entry.get())
                t18=str(department_entry.get())
                t19=int(salary_entry.get())
                t20=str(t_Password_entry.get())
                sql="insert into teachers values('%d','%s','%d','%d','%s','%d','%d','%d','%d','%s','%s','%d','%s','%d','%s','%d','%d','%s','%d','%s')"%(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20)
                cur.execute(sql)
                #sql="select Teacher_Id,Teacher_Name,DOB,Teacher_Mobile_No,Aadhar_No,Tenth_Year,Twelfth_Year,Graduation_Year,Father_Name,Mother_Name,Father_Mobile_No,Father_Email_Id,Mother_Mobile_No,Address,Pincode,Joining_Date,Department,Salary from teachers where Teacher_Email_Id='%s'and Teacher_Id='%d'"%(t5,t1)
                #cur.execute(sql)  
                db.commit()
                db.close()
                messagebox.showinfo('STATUS','Data Saved')
                fi.destroy()
                
            def t_FD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                ta1=int(teacher_id_entry.get())
                sql="select Teacher_Name,DOB,Teacher_Mobile_No,Teacher_Email_Id,Aadhar_No,Tenth_Year,twelfth_Year,Graduation_Year,Father_Name,Mother_Name,Father_Mobile_No,Father_Email_Id,Mother_Mobile_No,Address,Pincode,Joining_Date,Department,Salary,Password from teachers where Teacher_Id='%d'"%(ta1)
                cur.execute(sql)
                data=cur.fetchall()
                if len(data)==0:
                    messagebox.showinfo('STATUS',"No records found")
                    fi.destroy()
                else:
                    for res in data:
                        teacher_name_entry.insert(0,str(res[0]))
                        t_dob_entry.insert(0,int(res[1]))
                        teacher_mobile_no_entry.insert(0,int(res[2]))
                        t_email_id_entry.insert(0,str(res[3]))
                        t_aadhar_no_entry.insert(0,int(res[4]))
                        t_tenth_entry.insert(0,int(res[5]))
                        t_twelfth_entry.insert(0,int(res[6]))
                        t_graduation_entry.insert(0,int(res[7]))
                        t_father_name_entry.insert(0,str(res[8]))
                        t_mother_name_entry.insert(0,str(res[9]))
                        t_father_mobile_entry.insert(0,int(res[10]))
                        t_father_email_entry.insert(0,str(res[11]))
                        t_mother_mobile_entry.insert(0,int(res[12]))
                        t_Address_entry.insert(0,str(res[13]))
                        t_Pincode_entry.insert(0,int(res[14]))
                        joining_entry.insert(0,int(res[15]))
                        department_entry.insert(0,str(res[16]))
                        salary_entry.insert(0,int(res[17]))
                        t_Password_entry.insert(0,str(res[18]))
                db.close()
                
            def t_UD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                t1=int(teacher_id_entry.get())
                t2=str(teacher_name_entry.get())
                t3=int(t_dob_entry.get())
                t4=int(teacher_mobile_no_entry.get())
                t5=str(t_email_id_entry.get())
                t6=int(t_aadhar_no_entry.get())
                t7=int(t_tenth_entry.get())
                t8=int(t_twelfth_entry.get())
                t9=int(t_graduation_entry.get())
                t10=str(t_father_name_entry.get())
                t11=str(t_mother_name_entry.get())
                t12=int(t_father_mobile_entry.get())
                t13=str(t_father_email_entry.get())
                t14=int(t_mother_mobile_entry.get())
                t15=str(t_Address_entry.get())
                t16=int(t_Pincode_entry.get())
                t17=int(joining_entry.get())
                t18=str(department_entry.get())
                t19=int(salary_entry.get())
                t20=str(t_Password_entry.get())
                sql=("update teachers set Teacher_Name='%s',DOB='%d',Teacher_Mobile_No='%d',Teacher_Email_Id='%s',Aadhar_No='%d',Tenth_Year='%d',twelfth_Year='%d',Graduation_Year='%d',Father_Name='%s',Mother_Name='%s',Father_Mobile_No='%d',Father_Email_Id='%s',Mother_Mobile_No='%d',Address='%s',Pincode='%d',Joining_Date='%d',Department='%s',Salary='%d',Password='%s' where Teacher_Id='%d'")%(t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t1)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('STATUS','Data Updated')
                fi.destroy()
                
            def t_DD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                tb1=int(teacher_id_entry.get())
                sql="delete from teachers where Teacher_Id='%d'"%(tb1)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo("STATUS",'DELETED')
                fi.destroy()
                
            def t_SD():
                tsd=Toplevel(fi)
                tsd.geometry("1270x250+0+0")
                tsd.title("SHOW TEACHERS DATA")
                tsd.iconbitmap('LOGO.ico')
    
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                sql="select * from teachers"
                cur.execute(sql)
     
                my_tree=ttk.Treeview(tsd)

                #define columns
                my_tree['columns']=("Teacher_Id","Teacher_Name","DOB","Teacher_Mobile_No","Teacher_Email_Id","Aadhar_No","Tenth_Year","Twelfth_Year","Graduation_Year","Father_Name","Mother_Name","Father_Mobile_No","Father_Email_Id","Mother_Mobile_No","Address","Pincode","Joining_Date","Department","Salary","Password")

                #formate our columns
                my_tree.column('#0',width=0,stretch=NO)
                my_tree.column("Teacher_Id",anchor=W,width=80)
                my_tree.column("Teacher_Name",anchor=W,width=105)
                my_tree.column("DOB",anchor=W,width=60)
                my_tree.column("Teacher_Mobile_No",anchor=W,width=100)
                my_tree.column("Teacher_Email_Id",anchor=W,width=200)
                my_tree.column("Aadhar_No",anchor=W,width=100)
                my_tree.column("Tenth_Year",anchor=W,width=70)
                my_tree.column("Twelfth_Year",anchor=W,width=80)
                my_tree.column("Graduation_Year",anchor=W,width=80)
                my_tree.column("Father_Name",anchor=W,width=105)
                my_tree.column("Mother_Name",anchor=W,width=105)
                my_tree.column("Father_Mobile_No",anchor=W,width=100)
                my_tree.column("Father_Email_Id",anchor=W,width=200)
                my_tree.column("Mother_Mobile_No",anchor=W,width=100)
                my_tree.column("Address",anchor=W,width=100)
                my_tree.column("Pincode",anchor=W,width=100)
                my_tree.column("Joining_Date",anchor=W,width=100)
                my_tree.column("Department",anchor=W,width=100)
                my_tree.column("Salary",anchor=W,width=100)
                my_tree.column("Password",anchor=W,width=100)

                #create headings
                my_tree.heading("#0",text="",anchor=W)
                my_tree.heading("Teacher_Id",text="Teacher Id",anchor=W)
                my_tree.heading("Teacher_Name",text="Teacher Name",anchor=W)
                my_tree.heading("DOB",text="DOB",anchor=W)
                my_tree.heading("Teacher_Mobile_No",text="Teacher No",anchor=W)
                my_tree.heading("Teacher_Email_Id",text="Teacher Email",anchor=W)
                my_tree.heading("Aadhar_No",text="Aadhar No",anchor=W)
                my_tree.heading("Tenth_Year",text="Tenth year",anchor=W)
                my_tree.heading("Twelfth_Year",text="Twelfth year",anchor=W)
                my_tree.heading("Graduation_Year",text="Graduation Year",anchor=W)
                my_tree.heading("Father_Name",text="Father Name",anchor=W)
                my_tree.heading("Mother_Name",text="Mother Name",anchor=W)
                my_tree.heading("Father_Mobile_No",text="Father No",anchor=W)
                my_tree.heading("Father_Email_Id",text="Father Email",anchor=W)
                my_tree.heading("Mother_Mobile_No",text="Mother No",anchor=W)
                my_tree.heading("Address",text="Address",anchor=W)
                my_tree.heading("Pincode",text="Pincode",anchor=W)
                my_tree.heading("Joining_Date",text="Joining Date",anchor=W)
                my_tree.heading("Department",text="Department",anchor=W)
                my_tree.heading("Salary",text="Salary",anchor=W)
                my_tree.heading("Password",text="Password",anchor=W)

                count=0
                for record in cur:
                    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],
                    record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18],record[19]))
                    count += 1
    
                hsb=ttk.Scrollbar(tsd,orient="horizontal")
                hsb.configure(command=my_tree.xview)
                my_tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X,side=BOTTOM)

                vsb=ttk.Scrollbar(tsd,orient="vertical")
                vsb.configure(command=my_tree.yview)
                my_tree.configure(yscrollcommand=vsb.set)
                vsb.pack(fill=Y,side=RIGHT)

                my_tree.pack(padx=20,pady=50)
    
                tsd.mainloop()


            
            FI_Home=Canvas(fi,width=1380,height=640,bg='#104E8B')
            FI_Home.place(x=0,y=0)
            
            FI_heading=Label(fi,text="FACULTY INFORMATION",bg="#104E8B",fg="#F0FFFF",font=('Aeries',25))
            FI_heading.place(x=480,y=2)
            
            FI_Home1=Canvas(fi,width=1380,height=640,bg='#1E90FF')
            FI_Home1.place(x=0,y=50)
            
            teacher_side=Label(FI_Home1,text="TEACHER SIDE",font=25,bg="GREEN",fg="YELLOW")
            teacher_side.place(x=6,y=20)
            
            teacher_id=Label(FI_Home1,text="Teacher Id",font=5,bg="#1E90FF")
            teacher_id.place(x=6,y=50)
            teacher_id_entry=Entry(FI_Home1,width=30)
            teacher_id_entry.place(x=180,y=55)
                
            teacher_name=Label(FI_Home1,text="Teacher Name",font=5,bg="#1E90FF")
            teacher_name.place(x=450,y=50)
            teacher_name_entry=Entry(FI_Home1,width=30)
            teacher_name_entry.place(x=624,y=55)
                
            t_dob=Label(FI_Home1,text="DOB",font=5,bg="#1E90FF")
            t_dob.place(x=864,y=50)
            t_dob_entry=Entry(FI_Home1,width=30)
            t_dob_entry.place(x=1035,y=55)
            
            teacher_mobile_no=Label(FI_Home1,text="Teacher Mobile No.",font=5,bg="#1E90FF")
            teacher_mobile_no.place(x=6,y=90)
            teacher_mobile_no_entry=Entry(FI_Home1,width=30)
            teacher_mobile_no_entry.place(x=180,y=95)
            
            t_email_id=Label(FI_Home1,text="Teacher Email Id",font=5,bg="#1E90FF")
            t_email_id.place(x=450,y=90)
            t_email_id_entry=Entry(FI_Home1,width=30)
            t_email_id_entry.place(x=624,y=95)
            
            t_aadhar_no=Label(FI_Home1,text="Aadhar Number",font=5,bg="#1E90FF")
            t_aadhar_no.place(x=864,y=90)
            t_aadhar_no_entry=Entry(FI_Home1,width=30)
            t_aadhar_no_entry.place(x=1035,y=95)

            t_tenth=Label(FI_Home1,text="Tenth Year",font=5,bg="#1E90FF")
            t_tenth.place(x=6,y=130)
            t_tenth_entry=Entry(FI_Home1,width=30)
            t_tenth_entry.place(x=180,y=130)
                
            t_twelfth=Label(FI_Home1,text="Twelfth Year",font=5,bg="#1E90FF")
            t_twelfth.place(x=450,y=130)
            t_twelfth_entry=Entry(FI_Home1,width=30)
            t_twelfth_entry.place(x=624,y=130)

            t_graduation=Label(FI_Home1,text="Graduation Year",font=5,bg="#1E90FF")
            t_graduation.place(x=864,y=130)
            t_graduation_entry=Entry(FI_Home1,width=30)
            t_graduation_entry.place(x=1035,y=130)
    
            t_parent_side=Label(FI_Home1,text="PARENT SIDE",font=25,bg="GREEN",fg="YELLOW")
            t_parent_side.place(x=6,y=170)
                
            t_father_name=Label(FI_Home1,text="Father Name",font=5,bg="#1E90FF")
            t_father_name.place(x=6,y=200)
            t_father_name_entry=Entry(FI_Home1,width=30)
            t_father_name_entry.place(x=180,y=200)
                    
            t_mother_name=Label(FI_Home1,text="Mother Name",font=5,bg="#1E90FF")
            t_mother_name.place(x=450,y=200)
            t_mother_name_entry=Entry(FI_Home1,width=30)
            t_mother_name_entry.place(x=624,y=200)
                    
            t_father_mobile=Label(FI_Home1,text="Father Mobile No.",font=5,bg="#1E90FF")
            t_father_mobile.place(x=6,y=240)
            t_father_mobile_entry=Entry(FI_Home1,width=30)
            t_father_mobile_entry.place(x=180,y=240)

            t_father_email=Label(FI_Home1,text="Father Email Id",font=5,bg="#1E90FF")
            t_father_email.place(x=450,y=240)
            t_father_email_entry=Entry(FI_Home1,width=30)
            t_father_email_entry.place(x=624,y=240)
                    
            t_mother_mobile=Label(FI_Home1,text="Mother Mobile No.",font=5,bg="#1E90FF")
            t_mother_mobile.place(x=864,y=240)
            t_mother_mobile_entry=Entry(FI_Home1,width=30)
            t_mother_mobile_entry.place(x=1035,y=240)
                
            t_Address=Label(FI_Home1,text="Address",font=5,bg="#1E90FF")
            t_Address.place(x=6,y=280)
            t_Address_entry=Entry(FI_Home1,width=30)
            t_Address_entry.place(x=180,y=280)
            
            t_Pincode=Label(FI_Home1,text="Pincode",font=5,bg="#1E90FF")
            t_Pincode.place(x=450,y=280)
            t_Pincode_entry=Entry(FI_Home1,width=30)
            t_Pincode_entry.place(x=624,y=280)

            joining=Label(FI_Home1,text="Joining Date",font=5,bg="#1E90FF")
            joining.place(x=6,y=350)
            joining_entry=Entry(FI_Home1,width=30)
            joining_entry.place(x=180,y=350)

            department=Label(FI_Home1,text="Department",font=5,bg="#1E90FF")
            department.place(x=450,y=350)
            department_entry=Entry(FI_Home1,width=30)
            department_entry.place(x=624,y=350)

            salary=Label(FI_Home1,text="Salary",font=5,bg="#1E90FF")
            salary.place(x=864,y=350)
            salary_entry=Entry(FI_Home1,width=30)
            salary_entry.place(x=1035,y=350)

            t_Password=Label(FI_Home1,text="Password",font=5,bg="#1E90FF")
            t_Password.place(x=6,y=400)
            t_Password_entry=Entry(FI_Home1,width=30)
            t_Password_entry.place(x=180,y=400)

            insert_details=Button(FI_Home1,text="INSERT DETAILS",width=15,font=20,bg='blue',fg='white',command=t_ID)
            insert_details.place(x=6,y=455)

            find_details=Button(FI_Home1,text="FIND DETAILS",width=15,font=20,bg='blue',fg='white',command=t_FD)
            find_details.place(x=255,y=455)

            update_details=Button(FI_Home1,text="UPDATE DETAILS",width=15,font=20,bg='blue',fg='white',command=t_UD)
            update_details.place(x=524,y=455)

            delete_details=Button(FI_Home1,text="DELETE DETAILS",width=15,font=20,bg='blue',fg='white',command=t_DD)
            delete_details.place(x=813,y=455)

            delete_details=Button(FI_Home1,text="SHOW DETAILS",width=15,font=20,bg='blue',fg='white',command=t_SD)
            delete_details.place(x=1090,y=455)

            t_genrate=Button(FI_Home1,text="GENRATE",width=10,font=2,bg='blue',fg='white',command=t_genrate)
            t_genrate.place(x=450,y=395)

            Loginclose=Button(FI_Home1,text="BACK",width=15,font=10,bg='Red',fg='white',command=t_close_back)
            Loginclose.place(x=1090,y=530)
            
            fi.mainloop()   # Faculty Information Closed Screen
            
        def LIBERARY_INFORMATION():  # for Liberary Information Screen
            li=Toplevel(t)
            li.geometry("1380x640+0+0")
            li.title("LIBRARY INFORMATION")
            li.iconbitmap('LOGO.ico')
            
            def enter():
                Membership=membership_entry.get()
    
                if Membership == 'STUDENTS':
        
                    def S_ID():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        s1=int(student_id_entry.get())
                        s2=str(book_id_entry.get())
                        s3=int(issue_date_entry.get())
                        s4=str(place_entry.get())
                        sql="insert into slibrary values('%d','%s','%d','%s')"%(s1,s2,s3,s4)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved')
            
                    def S_FD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        s9=int(student_id_entry.get())
                        sql="select Book_Id,Issue_Date,Place from slibrary where Student_Id='%d'"%(s9)
                        cur.execute(sql)
                        data=cur.fetchall()
                        if len(data)==0:
                            messagebox.showinfo('STATUS',"No records found")
                        else:
                            for res in data:
                                book_id_entry.insert(0,str(res[0]))
                                issue_date_entry.insert(0,int(res[1]))
                                place_entry.insert(0,str(res[2]))
                        db.close()
                        
                    def S_UD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        s5=int(student_id_entry.get())
                        s6=str(book_id_entry.get())
                        s7=int(issue_date_entry.get())
                        s8=str(place_entry.get())
                        sql=("update slibrary set Book_Id='%s',Issue_Date='%d',Place='%s' where Student_Id='%d'")%(s6,s7,s8,s5)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Updated')
            
                    def S_DD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        s10=int(student_id_entry.get())
                        sql="delete from slibrary where Student_Id='%d'"%(s10)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo("STATUS",'DELETED')
            
                    def S_SD():
                        lis=Toplevel(li)
                        lis.geometry("500x250+50+370")
                        lis.title("SHOW DATABASE")
                        lis.iconbitmap('LOGO.ico')

                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        sql="select * from slibrary"
                        cur.execute(sql)
     
                        my_tree=ttk.Treeview(lis)

                        #define columns
                        my_tree['columns']=("Student_Id","Book_Id","Issue_Date","Place")

                        #formate our columns
                        my_tree.column('#0',width=0,stretch=NO)
                        my_tree.column("Student_Id",anchor=W,width=80)
                        my_tree.column("Book_Id",anchor=W,width=80)
                        my_tree.column("Issue_Date",anchor=W,width=100)
                        my_tree.column("Place",anchor=W,width=150)



                        #create headings
                        my_tree.heading("#0",text="",anchor=W)
                        my_tree.heading("Student_Id",text="Student Id",anchor=W)
                        my_tree.heading("Book_Id",text="Book Id",anchor=W)
                        my_tree.heading("Issue_Date",text="Issue Date",anchor=W)
                        my_tree.heading("Place",text="Place",anchor=W)



                        count=0
                        for record in cur:
                            my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3]))
                            count += 1
    
                        hsb=ttk.Scrollbar(lis,orient="horizontal")
                        hsb.configure(command=my_tree.xview)
                        my_tree.configure(xscrollcommand=hsb.set)
                        hsb.pack(fill=X,side=BOTTOM)

                        vsb=ttk.Scrollbar(lis,orient="vertical")
                        vsb.configure(command=my_tree.yview)
                        my_tree.configure(yscrollcommand=vsb.set)
                        vsb.pack(fill=Y,side=RIGHT)

                        my_tree.pack(padx=20,pady=50)

                        lis.mainloop()
                        
                    student_id=Label(LI_Home1,text="Student Id",font=5,bg="#1E90FF")
                    student_id.place(x=6,y=80)
                    student_id_entry=Entry(LI_Home1,width=30)
                    student_id_entry.place(x=180,y=85)

                    book_id=Label(LI_Home1,text="Book Id",font=5,bg="#1E90FF")
                    book_id.place(x=6,y=110)
                    book_id_entry=Entry(LI_Home1,width=30)
                    book_id_entry.place(x=180,y=115)

                    issue_date=Label(LI_Home1,text="Issue Date",font=5,bg="#1E90FF")
                    issue_date.place(x=6,y=140)
                    issue_date_entry=Entry(LI_Home1,width=30)
                    issue_date_entry.place(x=180,y=145)

                    place=Label(LI_Home1,text="Place",font=5,bg="#1E90FF")
                    place.place(x=6,y=170)
                    place_entry=Entry(LI_Home1,width=30)
                    place_entry.place(x=180,y=175)
        
                    insert_details=Button(LI_Home1,text="ID",width=5,font=5,bg='blue',fg='white',command=S_ID)
                    insert_details.place(x=6,y=200)

                    find_details=Button(LI_Home1,text="FD",width=5,font=5,bg='blue',fg='white',command=S_FD)
                    find_details.place(x=100,y=200)

                    update_details=Button(LI_Home1,text="UD",width=5,font=5,bg='blue',fg='white',command=S_UD)
                    update_details.place(x=194,y=200)

                    delete_details=Button(LI_Home1,text="DD",width=5,font=5,bg='blue',fg='white',command=S_DD)
                    delete_details.place(x=288,y=200)

                    show_details=Button(LI_Home1,text="SD",width=5,font=5,bg='blue',fg='white',command=S_SD)
                    show_details.place(x=382,y=200)
                    
                elif Membership == 'TEACHERS':
        
                    def T_ID():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        z1=int(teacher_id_entry.get())
                        z2=str(book_id_entry.get())
                        z3=int(issue_date_entry.get())
                        z4=str(place_entry.get())
                        sql="insert into tlibrary values('%d','%s','%d','%s')"%(z1,z2,z3,z4)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Saved')
            
                    def T_FD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        z5=int(teacher_id_entry.get())
                        sql="select Book_Id,Issue_Date,Place from tlibrary where Teacher_Id='%d'"%(z5)
                        cur.execute(sql)
                        data=cur.fetchall()
                        if len(data)==0:
                            messagebox.showinfo('STATUS',"No records found")
                        else:
                            for res in data:
                                book_id_entry.insert(0,str(res[0]))
                                issue_date_entry.insert(0,int(res[1]))
                                place_entry.insert(0,str(res[2]))
                        db.close()
            
                    def T_UD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        z6=int(teacher_id_entry.get())
                        z7=str(book_id_entry.get())
                        z8=int(issue_date_entry.get())
                        z9=str(place_entry.get())
                        sql=("update tlibrary set Book_Id='%s',Issue_Date='%d',Place='%s' where Teacher_Id='%d'")%(z7,z8,z9,z6)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('STATUS','Data Updated')
            
                    def T_DD():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        z10=int(teacher_id_entry.get())
                        sql="delete from tlibrary where Teacher_Id='%d'"%(z10)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo("STATUS",'DELETED')
            
                    def T_SD():
                        lit=Toplevel(li)
                        lit.geometry("500x250+50+370")
                        lit.title("SHOW DATABASE")
                        lit.iconbitmap('LOGO.ico')

                        db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                        cur=db.cursor()
                        sql="select * from tlibrary"
                        cur.execute(sql)
     
                        my_tree=ttk.Treeview(lit)

                        #define columns
                        my_tree['columns']=("Teacher_Id","Book_Id","Issue_Date","Place")

                        #formate our columns
                        my_tree.column('#0',width=0,stretch=NO)
                        my_tree.column("Teacher_Id",anchor=W,width=80)
                        my_tree.column("Book_Id",anchor=W,width=80)
                        my_tree.column("Issue_Date",anchor=W,width=100)
                        my_tree.column("Place",anchor=W,width=150)



                        #create headings
                        my_tree.heading("#0",text="",anchor=W)
                        my_tree.heading("Teacher_Id",text="Teacher Id",anchor=W)
                        my_tree.heading("Book_Id",text="Book Id",anchor=W)
                        my_tree.heading("Issue_Date",text="Issue Date",anchor=W)
                        my_tree.heading("Place",text="Place",anchor=W)



                        count=0
                        for record in cur:
                            my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3]))
                            count += 1
    
                        hsb=ttk.Scrollbar(lit,orient="horizontal")
                        hsb.configure(command=my_tree.xview)
                        my_tree.configure(xscrollcommand=hsb.set)
                        hsb.pack(fill=X,side=BOTTOM)

                        vsb=ttk.Scrollbar(lit,orient="vertical")
                        vsb.configure(command=my_tree.yview)
                        my_tree.configure(yscrollcommand=vsb.set)
                        vsb.pack(fill=Y,side=RIGHT)

                        my_tree.pack(padx=20,pady=50)

                        lit.mainloop()
                        
                    teacher_id=Label(LI_Home1,text="Teacher Id",font=5,bg="#1E90FF")
                    teacher_id.place(x=6,y=80)
                    teacher_id_entry=Entry(LI_Home1,width=30)
                    teacher_id_entry.place(x=180,y=85)

                    book_id=Label(LI_Home1,text="Book Id",font=5,bg="#1E90FF")
                    book_id.place(x=6,y=110)
                    book_id_entry=Entry(LI_Home1,width=30)
                    book_id_entry.place(x=180,y=115)

                    issue_date=Label(LI_Home1,text="Issue Date",font=5,bg="#1E90FF")
                    issue_date.place(x=6,y=140)
                    issue_date_entry=Entry(LI_Home1,width=30)
                    issue_date_entry.place(x=180,y=145)
                    
                    place=Label(LI_Home1,text="Place",font=5,bg="#1E90FF")
                    place.place(x=6,y=170)
                    place_entry=Entry(LI_Home1,width=30)
                    place_entry.place(x=180,y=175)
        
                    insert_details=Button(LI_Home1,text="ID",width=5,font=5,bg='blue',fg='white',command=T_ID)
                    insert_details.place(x=6,y=200)

                    find_details=Button(LI_Home1,text="FD",width=5,font=5,bg='blue',fg='white',command=T_FD)
                    find_details.place(x=100,y=200)

                    update_details=Button(LI_Home1,text="UD",width=5,font=5,bg='blue',fg='white',command=T_UD)
                    update_details.place(x=194,y=200)

                    delete_details=Button(LI_Home1,text="DD",width=5,font=5,bg='blue',fg='white',command=T_DD)
                    delete_details.place(x=288,y=200)

                    show_details=Button(LI_Home1,text="SD",width=5,font=5,bg='blue',fg='white',command=T_SD)
                    show_details.place(x=382,y=200)
       
                else:
                    messagebox.showerror("ERROR","You Are Not Member")    
            
            def B_ID():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                y1=str(books_id_entry.get())
                y2=str(books_name_entry.get())
                y3=str(author_entry.get())
                y4=int(edition_entry.get())
                y5=int(price_entry.get())
                sql="insert into books values('%s','%s','%s','%d','%d')"%(y1,y2,y3,y4,y5)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('STATUS','Data Saved')
    
            def B_FD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                y6=str(books_id_entry.get())
                sql="select Book_Name,Author,Edition,Price from books where Book_Id='%s'"%(y6)
                cur.execute(sql)
                data=cur.fetchall()
                if len(data)==0:
                    messagebox.showinfo('STATUS',"No records found")
                else:
                    for res in data:
                        books_name_entry.insert(0,str(res[0]))
                        author_entry.insert(0,str(res[1]))
                        edition_entry.insert(0,int(res[2]))
                        price_entry.insert(0,int(res[3]))
                db.close()
    
            def B_UD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                y7=str(books_id_entry.get())
                y8=str(books_name_entry.get())
                y9=str(author_entry.get())
                y10=int(edition_entry.get())
                y11=int(price_entry.get())
                sql=("update books set Book_Name='%s',Author='%s',Edition='%d',Price='%d' where Book_Id='%s'")%(y8,y9,y10,y11,y7)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('STATUS','Data Updated')
    
            def B_DD():
                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                y12=str(books_id_entry.get())
                sql="delete from books where Book_Id='%s'"%(y12)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo("STATUS",'DELETED')
    
            def B_SD():
                lib=Toplevel(li)
                lib.geometry("500x250+750+370")
                lib.title("SHOW DATABASE")
                lib.iconbitmap('LOGO.ico')

                db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
                cur=db.cursor()
                sql="select * from books"
                cur.execute(sql)
     
                my_tree=ttk.Treeview(lib)

                #define columns
                my_tree['columns']=("Book_Id","Book_Name","Author","Edition","Price")

                #formate our columns
                my_tree.column('#0',width=0,stretch=NO)
                my_tree.column("Book_Id",anchor=W,width=80)
                my_tree.column("Book_Name",anchor=W,width=150)
                my_tree.column("Author",anchor=W,width=200)
                my_tree.column("Edition",anchor=W,width=100)
                my_tree.column("Price",anchor=W,width=100)


                #create headings
                my_tree.heading("#0",text="",anchor=W)
                my_tree.heading("Book_Id",text="Book Id",anchor=W)
                my_tree.heading("Book_Name",text="Book Name",anchor=W)
                my_tree.heading("Author",text="Author",anchor=W)
                my_tree.heading("Edition",text="Edition",anchor=W)
                my_tree.heading("Price",text="Price",anchor=W)


                count=0
                for record in cur:
                    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3],record[4]))
                    count += 1
    
                hsb=ttk.Scrollbar(lib,orient="horizontal")
                hsb.configure(command=my_tree.xview)
                my_tree.configure(xscrollcommand=hsb.set)
                hsb.pack(fill=X,side=BOTTOM)

                vsb=ttk.Scrollbar(lib,orient="vertical")
                vsb.configure(command=my_tree.yview)
                my_tree.configure(yscrollcommand=vsb.set)
                vsb.pack(fill=Y,side=RIGHT)

                my_tree.pack(padx=20,pady=50)

                lib.mainloop()
    
            
            LI_Home=Canvas(li,width=1380,height=640,bg='#104E8B')
            LI_Home.place(x=0,y=0)
            
            LI_heading=Label(li,text="LIBERARY INFORMATION",bg="#104E8B",fg="#F0FFFF",font=('Aeries',25))
            LI_heading.place(x=480,y=2)
            
            LI_Home1=Canvas(li,width=1380,height=640,bg='#1E90FF')
            LI_Home1.place(x=0,y=50)

            library_side=Label(LI_Home1,text="LIBRARY WORK",font=25,bg="GREEN",fg="YELLOW")
            library_side.place(x=6,y=20)

            membership=Label(LI_Home1,text="Membership",font=5,bg="#1E90FF")
            membership.place(x=6,y=50)
            lt=['STUDENTS','TEACHERS']
            membership_entry=ttk.Combobox(LI_Home1)
            membership_entry['values']=lt
            membership_entry.place(x=180,y=55)

            enter=Button(LI_Home1,text="Enter",width=5,font=5,bg='blue',fg='white',command=enter)
            enter.place(x=420,y=50)
            
            books_side=Label(LI_Home1,text="BOOKS SIDE",font=25,bg="GREEN",fg="YELLOW")
            books_side.place(x=690,y=20)

            books_id=Label(LI_Home1,text="Book Id",font=5,bg="#1E90FF")
            books_id.place(x=690,y=50)
            books_id_entry=Entry(LI_Home1,width=30)
            books_id_entry.place(x=864,y=55)

            books_name=Label(LI_Home1,text="Book Name",font=5,bg="#1E90FF")
            books_name.place(x=690,y=80)
            books_name_entry=Entry(LI_Home1,width=30)
            books_name_entry.place(x=864,y=85)

            author=Label(LI_Home1,text="Author",font=5,bg="#1E90FF")
            author.place(x=690,y=110)
            author_entry=Entry(LI_Home1,width=30)
            author_entry.place(x=864,y=115)

            edition=Label(LI_Home1,text="Edition",font=5,bg="#1E90FF")
            edition.place(x=690,y=140)
            edition_entry=Entry(LI_Home1,width=30)
            edition_entry.place(x=864,y=145)

            price=Label(LI_Home1,text="Price",font=5,bg="#1E90FF")
            price.place(x=690,y=170)
            price_entry=Entry(LI_Home1,width=30)
            price_entry.place(x=864,y=175)
     
            insertt_details=Button(LI_Home1,text="ID",width=5,font=5,bg='blue',fg='white',command=B_ID)
            insertt_details.place(x=690,y=200)

            findd_details=Button(LI_Home1,text="FD",width=5,font=5,bg='blue',fg='white',command=B_FD)
            findd_details.place(x=784,y=200)
            
            updatee_details=Button(LI_Home1,text="UD",width=5,font=5,bg='blue',fg='white',command=B_UD)
            updatee_details.place(x=878,y=200)

            deletee_details=Button(LI_Home1,text="DD",width=5,font=5,bg='blue',fg='white',command=B_DD)
            deletee_details.place(x=972,y=200)

            showw_details=Button(LI_Home1,text="SD",width=5,font=5,bg='blue',fg='white',command=B_SD)
            showw_details.place(x=1066,y=200)

      
            li.mainloop()  # Liberary Information Closed Screen
            
        def LoginClose():
            t.destroy()
            
        def Student_File_Update():
            
            def update_csv(filename, table, host, user, password, database):
                # Connect to MySQL database
                try:
                    conn = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                    )
                    cursor = conn.cursor()

                    # Fetch data from MySQL table
                    cursor.execute(f"SELECT * FROM {table}")
                    rows = cursor.fetchall()

                    # Check if CSV file exists, if not create one
                    with open(filename, 'a', newline='') as file:
                        writer = csv.writer(file)

                        # Write header if the file is empty
                        if file.tell() == 0:
                            writer.writerow([i[0] for i in cursor.description])

                        # Write data to CSV file
                        for row in rows:
                            writer.writerow(row)

                    print("CSV file updated successfully.")
                    messagebox.showinfo('STATUS','Data Saved')

                except pymysql.Error as error:
                    messagebox.showerror("ERROR","Data Not Saved")

                finally:
                    if conn.open:
                        cursor.close()
                        conn.close()

            # Example usage
            filename = "STUDENT_DATA.csv"
            table = "students"
            host = "localhost"
            user = "root"
            password = "root"
            database = "scss"

            update_csv(filename, table, host, user, password, database)
            
        def Teacher_File_Update():
            
            def update_csv(filename, table, host, user, password, database):
                # Connect to MySQL database
                try:
                    conn = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                    )
                    cursor = conn.cursor()

                    # Fetch data from MySQL table
                    cursor.execute(f"SELECT * FROM {table}")
                    rows = cursor.fetchall()

                    # Check if CSV file exists, if not create one
                    with open(filename, 'a', newline='') as file:
                        writer = csv.writer(file)

                        # Write header if the file is empty
                        if file.tell() == 0:
                            writer.writerow([i[0] for i in cursor.description])

                        # Write data to CSV file
                        for row in rows:
                            writer.writerow(row)

                    print("CSV file updated successfully.")
                    messagebox.showinfo('STATUS','Data Saved')

                except pymysql.Error as error:
                    messagebox.showerror("ERROR","Data Not Saved")

                finally:
                    if conn.open:
                        cursor.close()
                        conn.close()

            # Example usage
            filename = "TEACHER_DATA.csv"
            table = "teachers"
            host = "localhost"
            user = "root"
            password = "root"
            database = "scss"

            update_csv(filename, table, host, user, password, database)           
        
        LoginHome=Canvas(t,width=1380,height=640,bg='#104E8B')
        LoginHome.place(x=0,y=0)
        
        LoginHeading=Label(t,text="COLLEGE ADMINSTRATION",bg="#1874CD",fg="#F0FFFF",width=30,height=3,font=('Aeries',28))
        LoginHeading.place(x=300,y=2)
        
        Line2=Label(t,text="_________________________________________________________________________________________________________",bg="#104E8B",fg="#F0FFFF",font=50)
        Line2.place(x=70,y=150)
        
        Teachers=Button(t,text="FACULTY  INFORMATION",width=35,height=3,font=20,bg='blue',fg='#FFD700',command=FACULTY_INFORMATION)
        Teachers.place(x=150,y=280)
        
        Teachers_File=Button(t,text="FACULTY FILE UPDATE",width=25,height=1,font=10,bg='cornflower blue',fg='black',command=Teacher_File_Update)
        Teachers_File.place(x=70,y=515)
        
        Students=Button(t,text="STUDENT  SUPERVISION",width=35,height=3,font=20,bg='blue',fg='#FFD700',command=STUDENT_SUPERVISION)
        Students.place(x=450,y=430)
        
        Students_File=Button(t,text="STUDENT FILE UPDATE",width=25,height=1,font=10,bg='cornflower blue',fg='black',command=Student_File_Update)
        Students_File.place(x=70,y=555)
        
        Liberary=Button(t,text="LIBERARY  INFORMATION",width=35,height=3,font=20,bg='blue',fg='#FFD700',command=LIBERARY_INFORMATION)
        Liberary.place(x=770,y=280)
        
        Library_File=Button(t,text="LIBRARY FILE UPDATE",width=25,height=1,font=10,bg='cornflower blue',fg='black')
        Library_File.place(x=70,y=595)
               
        Loginclose=Button(t,text="BACK",width=15,font=10,bg='Red',fg='white',command=LoginClose)
        Loginclose.place(x=1077,y=580)
        
        t.mainloop()  # for closed the administrator side
    
    elif adminstrator == "root" and password != "root" :
        messagebox.showerror("ERROR","PASSWORD IS NOT CORRECT..!")
        
    elif adminstrator != "root" and password == "root" :
        messagebox.showerror("ERROR","ADMINSTRATOR ID IS NOT CORRECT..!")
    
    else :
        messagebox.showerror("ERROR","ADMINSTRATOR ID AND PASSWORD IS NOT CORRECT..!")
 
        
 
def ScreenClear():
    A1.delete(0,100)
    B1.delete(0,100)

def ScreenClose():
    screen.destroy()

Home=Canvas(screen,width=1380,height=640,bg='#104E8B')
Home.place(x=0,y=0)

Welcome=Label(screen,text="WELCOME TO SMART COLLEGE SYSTEM SOFTWARE",anchor="w",bg="#1874CD",fg="#F0FFFF",width=100,height=3,font=('Aeries',28))
Welcome.pack()

Screenclose=Button(screen,text="CLOSE",width=15,font=10,bg='Red',fg='white',command=ScreenClose)
Screenclose.place(x=1077,y=580)

SideLabel=Label(screen,bg="#1E90FF",width=30,height=8)
SideLabel.place(x=1052,y=3)

QuizPortal=Button(screen,text="QUIZ PORTAL",width=15,font=10,bg='blue',fg='#FFD700')
QuizPortal.place(x=1090,y=20)

Attendance=Button(screen,text="TEACHERS",width=15,font=10,bg='blue',fg='#FFD700')
Attendance.place(x=1090,y=80)

MidLabel=Label(screen,bg='#1E90FF',width=70,height=20)
MidLabel.place(x=400,y=180)

LoginName=Label(screen,text="ADMINSTRATOR LOGIN",width=35,bg="#104E8B",fg="#F0FFFF",font=50)
LoginName.place(x=455,y=200)

Line=Label(screen,text="_________________________________________",bg="#1E90FF",fg="#F0FFFF",font=50)
Line.place(x=420,y=230)

A=Label(screen,text="ADMINSTRATOR ID",bg="#009ACD",font=5)
A.place(x=450,y=280)
A1=Entry(screen,width=30)
A1.place(x=670,y=280)

B=Label(screen,text="PASSWORD",bg="#009ACD",font=5)
B.place(x=450,y=330)
B1=Entry(screen,width=30,show='*')
B1.place(x=670,y=330)

C=Button(screen,text="LOGIN",width=10,font=10,bg='blue',fg='#FFD700',command=LOGIN)
C.place(x=450,y=400)

C1=Button(screen,text="CLEAR",width=10,font=10,bg='blue',fg='#FFD700',command=ScreenClear)
C1.place(x=680,y=400)

screen.mainloop()