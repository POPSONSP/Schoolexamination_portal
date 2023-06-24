import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="Popson_2013", database="school_portal")
cursor = myconn.cursor()
def registration():
        print("Kindly proceed with your registration by providing your details below ")
        val= []
        student_info= ("First_name", "Last_name", "Gender", "Age","Email_address","Exam_no", "Student_ID", "Pass_word","Score")
        querry= "INSERT INTO student (First_name, Last_name, Gender, Age, Email_address , Exam_no, Student_ID,Pass_word, Score) VALUES (%s, %s,%s, %s, %s, %s, %s, %s,%s)"
        for holder in range(9):
            if student_info[holder] == "Exam_no":
                user = random.randint(2020270000, 2020299999)
            elif student_info[holder]== "Student_ID":
                user= random.randint( 202021000, 202029876)
            elif student_info[holder]== "Score":
                user= 0    
            else:
                user= input(f"Enter your {student_info[holder]}: ")
            val.append(user)
        # print(val)
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(2)
        print(f"Dear {val[0]} {val[1]} you have succesfully registered as a student, you can login with your {val[4]} as your username and {val[7]} as your password")
        time.sleep(2)
        rega=input("""
        Enter 1 to login 
        Enter 2 to logout
        """)
        if rega=="1":
            login()
        else:
            sys.exit()    

def login():
    global username
    global Pass_word
    username = input("Enter your Email address: ")
    Pass_word = input("Enter your password ")
    val_ = (username, Pass_word)
    querry = "select * from student where Email_address=%s and Pass_word=%s "
    cursor.execute(querry, val_)
    result = cursor.fetchone()
    if result:
        print("You have successfully login")
        time.sleep(2)
        print("""
        Enter 1 to Write your Exam
        Enter 2 to Perform other operation
         """)
        std= input(">>> ")
        if std == "1":
            time.sleep(1)
            print("Redirecting to Exam portal...")
            time.sleep(2)
            select()
        elif std =="2":
            time.sleep(2)
            print("Sorry !!! the operation you have chosen is unavailable at the moment, check back later")   
            login() 

        else:
            sys.exit()    
    else:
        print("Invalid username or password")
        login() 

def select():
    quest_nu= set()
    score=0
    print("""
    Enter 1 to start Exam
    Enter 2 to Quit: """)
    request=input(">>> ")
    if request=="1":
        time.sleep(1)
        print("Reloading Exam Portal...")
        time.sleep(1)
        # for i in range(4):
        print("""
        Dear student kindly note that you are entitled to 10 Question as any attempt to answer above 10 question is purnishable.
        You are encouraged to enter question umber to continue and Stop to quit.
        Goodluck!!!!!!!!!
        """)
        ques_id = input("Enter question number: ")
        while ques_id != "stop":
            if ques_id not in quest_nu:
                val = (ques_id, )
                querry = "select * from question where id = %s"
                cursor.execute(querry, val)
                result = cursor.fetchone()
                if result:
                    print(result[1])
                    time.sleep(1)
                    print(result[2])
                    time.sleep(1)
                    print(result[3])
                    time.sleep(1)
                    print(result[4])
                    time.sleep(2)
                    answ = input("Enter your answer: ").strip().lower()
                    if answ == result[5]:
                        print("CORRECT ANSWER")
                        score += 10
                    else:
                        print("WRONG ANSWER") 
                        score -= 5      
                quest_nu.add(ques_id)
            else:
                print(" you have selected this question number before")    
                time.sleep(2)
            ques_id = input("Enter question number: ") 
        print(score)   
        total= score  
        val2 = (total, username)
        querry= "UPDATE student SET Score = %s where Email_address = %s"
        cursor.execute(querry, val2)
        myconn.commit()
        val3= (username,Pass_word )    
        querry = "select * from student where Email_address=%s and Pass_word=%s "
        cursor.execute(querry, val3)
        u_user = cursor.fetchone() 
        if u_user:
            if score <= 20:
                print(f" Dear {u_user[0]} {u_user[1]} your score is {total}, which is below Cutoff mark, You are hereby denied Admission into our Noble Institution")
            elif score > 20:
                print(f"""
                Dear {u_user[0]} {u_user[1]} i have been directed by the school Authority to congratulate you on your Admssion into our Noble Institution having satified all possible
                Available requirements by scoring above the cutoff mark in the just concluded examination by scoring {total} above the school cutoff score
                Do accept my Congratulation.
                Kindly Note the below details for your singular refrence. 
                Student_ID is {u_user[7]}  
                Exam_no is {u_user[6]}
                """)        
            
    else:
        print(" you are about to quit")
        time.sleep(2)
        sys.exit()
