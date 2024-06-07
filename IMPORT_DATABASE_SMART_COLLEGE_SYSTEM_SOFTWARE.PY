while True:
    import pymysql
    print("1 : LOCALHOST= localhost , USER= root , PASSWORD= ?")
    print("2 : LOCALHOST= ? , USER= ? , PASSWORD= ?")
    print("3 : EXIT")
    
    choice=input("Enter Choice :")
    if choice == "3":
        break
    
    if choice == "1":
        host='localhost'
        user='root'
        password=input("Enter Password  :")
        db=pymysql.connect(host=host,user=user,password=password)
        cur=db.cursor()
        def opt():
            operation="create database SCSS"# SMART COLLEGE SYSTEM SOFTWARE
            cur.execute(operation)
            operation="use SCSS"
            cur.execute(operation)
            operation="create table TEACHERS(Teacher_Id INT AUTO_INCREMENT PRIMARY KEY,Teacher_Name VARCHAR(50),DOB INT,Teacher_Mobile_No BIGINT,Teacher_Email_Id VARCHAR(50),Aadhar_No BIGINT,Tenth_Year INT,Twelfth_Year INT,Graduation_Year INT,Father_Name VARCHAR(50),Mother_Name VARCHAR(50),Father_Mobile_No BIGINT,Father_Email_Id VARCHAR(50),Mother_Mobile_No BIGINT,Address VARCHAR(255),Pincode INT,Joining_Date INT,Department VARCHAR(20),Salary BIGINT,Password VARCHAR(50))"
            cur.execute(operation)
            operation="desc TEACHERS"
            cur.execute(operation)
            operation="create table STUDENTS(Student_Id INT AUTO_INCREMENT PRIMARY KEY,Student_Name VARCHAR(50),DOB INT,Student_Mobile_No BIGINT,Student_Email_Id VARCHAR(50),Aadhar_No BIGINT,Tenth_Marks INT,Tenth_Year INT,Twelfthth_Marks INT,Twelfthth_Year INT,Session INT,Branch VARCHAR(20),Roll_No BIGINT,Father_Name VARCHAR(50),Mother_Name VARCHAR(50),Father_Mobile_No BIGINT,Father_Email_Id VARCHAR(50),Mother_Mobile_No BIGINT,Address VARCHAR(100),Pincode INT,Password VARCHAR(50))"
            cur.execute(operation)
            operation="desc STUDENTS"
            cur.execute(operation)
            operation="create table BOOKS(Book_Id VARCHAR(50) PRIMARY KEY,Book_Name VARCHAR(100),Author VARCHAR(50),Edition INT,Price INT)"
            cur.execute(operation)
            operation="desc BOOKS"
            cur.execute(operation)
            operation="create table SLIBRARY(Student_Id INT,Book_Id VARCHAR(50),Issue_Date INT,Place VARCHAR(50),foreign key(student_Id) references STUDENTS(student_Id))"
            cur.execute(operation)
            operation="alter table SLIBRARY add foreign key(Book_Id) references BOOKS(Book_Id)"
            cur.execute(operation)
            operation="desc SLIBRARY"
            cur.execute(operation)
            operation="create table TLIBRARY(Teacher_Id INT,Book_Id VARCHAR(50),Issue_Date INT,Place VARCHAR(50),foreign key(Teacher_Id) references TEACHERS(Teacher_Id))"
            cur.execute(operation)
            operation="alter table TLIBRARY add foreign key(Book_Id) references BOOKS(Book_Id)"
            cur.execute(operation)
            db.commit()
            db.close()
        print("Database created successfully...")
        opt()
    elif choice =="2":
        host=input("Enter Host :")
        user=input("Enter User :")
        password=input("Enter Password  :")
        db=pymysql.connect(host=host,user=user,password=password)
        cur=db.cursor()
        def opt():
            operation="create database SCSS"
            cur.execute(operation)
            operation="use SCSS"
            cur.execute(operation)
            operation="create table TEACHERS(Teacher_Id INT AUTO_INCREMENT PRIMARY KEY,Teacher_Name VARCHAR(50),DOB INT,Teacher_Mobile_No BIGINT,Teacher_Email_Id VARCHAR(50),Aadhar_No BIGINT,Tenth_Year INT,Twelfth_Year INT,Graduation_Year INT,Father_Name VARCHAR(50),Mother_Name VARCHAR(50),Father_Mobile_No BIGINT,Father_Email_Id VARCHAR(50),Mother_Mobile_No BIGINT,Address VARCHAR(255),Pincode INT,Joining_Date INT,Department VARCHAR(20),Salary BIGINT,Password VARCHAR(50))"
            cur.execute(operation)
            operation="desc TEACHERS"
            cur.execute(operation)
            operation="create table STUDENTS(Student_Id INT AUTO_INCREMENT PRIMARY KEY,Student_Name VARCHAR(50),DOB INT,Student_Mobile_No BIGINT,Student_Email_Id VARCHAR(50),Aadhar_No BIGINT,Tenth_Marks INT,Tenth_Year INT,Twelfthth_Marks INT,Twelfthth_Year INT,Session INT,Branch VARCHAR(20),Roll_No BIGINT,Father_Name VARCHAR(50),Mother_Name VARCHAR(50),Father_Mobile_No BIGINT,Father_Email_Id VARCHAR(50),Mother_Mobile_No BIGINT,Address VARCHAR(100),Pincode INT,Password VARCHAR(50))"
            cur.execute(operation)
            operation="desc STUDENTS"
            cur.execute(operation)
            operation="create table BOOKS(Book_Id VARCHAR(50) AUTO_INCREMENT PRIMARY KEY,Book_Name VARCHAR(100),Author VARCHAR(50),Edition INT,Price INT)"
            cur.execute(operation)
            operation="desc BOOKS"
            cur.execute(operation)
            operation="create table SLIBRARY(Student_Id INT,Book_Id VARCHAR(50),Issue_Date INT,Place VARCHAR(50),foreign key(student_Id) references STUDENTS(student_Id))"
            cur.execute(operation)
            operation="alter table SLIBRARY add foreign key(Book_Id) references BOOKS(Book_Id)"
            cur.execute(operation)
            operation="desc SLIBRARY"
            cur.execute(operation)
            operation="create table TLIBRARY(Teacher_Id INT,Book_Id VARCHAR(50),Issue_Date INT,Place VARCHAR(50),foreign key(Teacher_Id) references TEACHERS(Teacher_Id))"
            cur.execute(operation)
            operation="alter table TLIBRARY add foreign key(Book_Id) references BOOKS(Book_Id)"
            cur.execute(operation)
  
            db.commit()
            db.close()
        print("Database created successfully...")
        opt()
    else:
        print("INVALID CHOICE")
    print()
        
    