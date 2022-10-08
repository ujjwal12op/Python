# Make a menu driven program on student system.
"""
**** MENU****
1.Add a student
2.View all student details
3.Search student using roll number
4.Remove student using roll number
5.Update student details using roll number
6.Exit

In SQL share the details as Roll no, name , std , div, Address , phone no 
In option 5 allow user to update student std, div, phone no details

On displaying student details , please display them in following format

*** Student details****
Roll no :
Name :
Std :
Div :
Phone no :

"""
import mysql.connector

class student:
    def __init__(self):      # Initialisation
        self.roll=-1
        self.name=""
        self.std=-1
        self.div=""
        self.phone=-1
    
    def EnterDetails(self):
        self.roll=input("Enter your roll number ")
        self.name=input("Enter your name ")
        self.std=input("Enter your standard ")
        self.div=input("Enter your division ")
        self.phone=input("Enter your phone number ")
    
    def DisplayStudent(self):
        print("Roll no :",self.roll)
        print("Name :",self.name)
        print("std :",self.std)
        print("div :",self.div)
        print("Phone no :",self.phone)
        

choice=0
studentList=[]
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password@123",
  database="pythonproject"
)
while choice!=6:
    print( "**** MENU****")
    print("1.Add a student")
    print("2.View all student details")
    print("3.Search student using roll number")
    print("4.Remove student using roll number")
    print("5.Update student details using roll number")
    print("6.Exit")

    choice=int(input("Enter your choice "))

    if choice==1:
        print("Add student")
        s1=student()
        s1.EnterDetails()
        studentList.append(s1)
        mycursor=mydb.cursor()
        query="""INSERT INTO pythonproject.table (`Roll no`, `Name`, `Std`, `Div`, `Phone no`) VALUES ('"""+s1.roll+"""','"""+s1.name+"""','"""+s1.std+"""','"""+s1.div+"""','"""+s1.phone+"""')"""
        mycursor.execute(query)
    
    
    elif choice==2:
        print("Displaying the student list ")
        i=0
        length=len(studentList)
        while i<length:
            s1=studentList[i]
            s1.DisplayStudent()
            i+=1
        for student in studentList:
            student.DisplayStudent()

    elif choice==3:
        
        studentfound=0
        print("Search student using roll number ")
        rollnotosearch=int(input("Enter the roll number to be searched for "))
        l=len(studentList)
        i=0
        while i<l:
            s=studentList[i]
            if rollnotosearch==s.roll:
                studentfound=1
                s.DisplayStudent()
            i+=1
        if studentfound==0:
            print("student with roll number ",rollnotosearch,"is not present in the database")       
    
    elif choice==4:
        print("Delete student based on roll number")
        rollnotodelete=int(input("Enter the roll no of student to be deleted "))
        studentfound=0
        studenttodelete=""
        i=0
        l=len(studentList)
        for student in studentList:
            if rollnotodelete==student.roll:
                studentfound=1
                studenttodelete=student
                studentList.remove(student)
            
        if studentfound==0:
            print("student with roll no ", rollnotodelete,"is not present in the database ")
        else:
            print("Student deleted with the following information")
            print(studenttodelete.DisplayStudent())
            studentList.remove(studenttodelete)
         
    elif choice==5:
        rolltoupdate=int(input("Enter the roll number you want to update "))
        studentfound=0
        studenttoupdate=""
        l=len(studentList)
        for student in studentList:
            if rolltoupdate==student.roll:
                studentfound=1
                student.EnterDetails()
            
            else:
                print("Student with roll number ",rolltoupdate,"is not in our database")
    
    elif choice==6:
        break
    