import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="Popson_2013", database="school_portal")
cursor = myconn.cursor()

def registration():
        print("Kindly proceed with your registration by providing your details below ")
        val= []
        admin_info= ("First_name", "Last_name", "Gender", "Age","Email_address", "Pass_word")
        querry= "INSERT INTO admin (First_name, Last_name, Gender, Age, Email_address, Pass_word) VALUES (%s, %s, %s, %s, %s, %s)"
        for holder in range(6):
            user= input(f"Enter your {admin_info[holder]}: ")
            val.append(user)
        # print(val)
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(2)
        print(f"Dear {val[0]} {val[1]} you have succesfully registered as an Admin, you can login with your {val[4]} as your username and {val[5]} as your password")
        time.sleep(2)
        regs= input("""
        Enter 1 to login 
        Enter 2 to logout
        """)
        time.sleep(2)
        if regs =="1":
            login()
        else:
             sys.exit()    

def login():
    global username
    global Pass_word
    username = input("Enter your Email address: ")
    Pass_word = input("Enter your password ")
    val = (username, Pass_word)
    querry = "select * from admin where Email_address=%s and Pass_word=%s "
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        print("You have successfully login")
        time.sleep(2)
        print("""
        Enter 1 to set new question
        Enter 2 to replace a set question
        """)
        action=input(">>>> ")
        if action=="1":
             quest()
        elif action=="2":
             update()              
    else:
        print("Invalid username or password")
        login() 

def quest():
    print("""
    Enter 1 to set new question
    Enter 2 to stop
    """)
    dec= input(">>> ")
    while dec =="1":
        querry = "INSERT INTO question (question, optiona, optionb, optionc, answer) VALUES(%s, %s, %s, %s, %s)"
        question = input("Set question : ")
        optiona = input("Enter option A: ")
        optionb = input("Enter option B: ")
        optionc = input("Enter option C: ")
        answer = input("Enter answer: ")
        val = (question, optiona, optionb, optionc, answer)
        cursor.execute(querry, val)
        myconn.commit() 
        print("""
    Enter 1 to set new question
    Enter 2 to update a question
    """)
        dec= input(">>> ")         
    else:
         print("Redirecting to Exam Portal to Update the Question of your choice ")
         time.sleep(2)
         update()

def update():
    print("""
            Enter 1 to change aother question
            Enter 2 to set a new question
            """)
    time.sleep(2)
    dec = input("Enter question number to update: ")
    val = (dec, )
    querry = "SELECT * FROM question where id = %s" 
    cursor.execute(querry, val)
    result = cursor.fetchone()
    while dec=="1": 
        if result:
            newquestion = input("Enter new question: ")
            optiona = input("Enter optiona: ")
            optionb = input("Enter optionb: ")
            optionc = input("Enter optionc: ")
            answer = input("Enter answer: ")
            val = (newquestion, optiona, optionb, optionc, answer, dec)
            querry = "UPDATE question SET question =%s, optiona= %s, optionb =%s, optionc=%s, answer=%s where id = %s"
            cursor.execute(querry, val)
            myconn.commit()
            print("""
            Enter 1 to change aother question
            Enter 2 to set a new question
            """)
            time.sleep(1)
            dec=input(">>> ")
    else:
         print("Redirecting to Exam POrtal to Set a new Question")
         time.sleep(2)
         quest()


