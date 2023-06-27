import time
import sys
time.sleep(1)
def homepage():
    print("Welcome to Sunshine Online Examination Portal")
    time.sleep(1)
    print(""""
    Enter 1 for Admin
    Enter 2 for Student
    """)
    resp=input(">>> ")
    if resp=="1":
        print("WElcome to Admin portal of  Sunshine school")
        time .sleep(1)
        print("""
        Enter 1 to register
        Enter 2 to Login
        """)
        respo=input(">>> ")
        if respo=="1":
            from Admin import registration
            registration()
        elif respo=="2":
            from Admin import login
            login()    
        else:
            homepage()  
    elif resp=="2":
         print("WElcome to Student portal of  Sunshine school")
         time.sleep(1)
         print("""
         Enter 1 to register
         Enter 2 to Login
         """)
         respon = input(">>> ")
         if respon=="1":
           from student import registration
           registration()  
         elif respon=="2":
            from student import login
            login() 
    else:
          homepage()       
homepage()                     

         

        