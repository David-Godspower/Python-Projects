import random
import json
import string

print("A Simple School Management System\n\n")

DATA_FILE = "school_data.json"

# Dictionary to store teachers information 
Teachers_Info = {}

# Dictionary to store students information 
Students_Info = {}


# Load data from the file when the program starts
def load_data():
    global Teachers_Info, Students_Info
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            Teachers_Info = data.get("Teachers_Info", {})
            Students_Info = data.get("Students_Info", {})
    except (FileNotFoundError, json.JSONDecodeError):
        Teachers_Info = {}
        Students_Info = {}

# Save data to the file after every update
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump({"Teachers_Info": Teachers_Info, "Students_Info": Students_Info}, file, indent=4)






    
# Teacher Function 
def Teachers():
    while True:
        print("\n\n\t+++++ Welcome to Teachers Menu +++++ \n\n 1) Add a Teacher \n 2) View Teachers \n 3) Back to Home Page \n ")
        userchoice = input("\tPlease Select your choice:.... ")

        if userchoice == "1":
            Teacher_Name = input("\nEnter Teacher Name: ")
            if all(char.isalpha() or char.isspace() for char in Teacher_Name) and len(Teacher_Name) >= 5:
                Teacher_Phone_Number = input("Enter Teacher Phone Number: ")
                if len(Teacher_Phone_Number) == 11:
                    Teacher_Subjects = input("Enter Teacher Subject(s): ").title()
                    if all(char.isalpha() or char.isspace() for char in Teacher_Subjects):
                        TeacherID = "TCH-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                        print(f"Teacher ID: {TeacherID}")

                        Teachers_Info[TeacherID] = {
                            "Teacher ID": TeacherID,
                            "Teacher Name": Teacher_Name,
                            "Teacher Phone Number": Teacher_Phone_Number,
                            "Teacher Subjects": Teacher_Subjects
                        }

                        save_data()  # Save data after adding teacher
                        print("\nTeacher Information successfully saved!")
                    else:
                        print("Teacher Subjects can only contain alphabets and spaces.")
                else:
                    print("Phone Number must be 11 digits.")
            else:
                print("Invalid Name. Must be at least 5 characters and contain only letters and spaces.")

        elif userchoice == "2":
            if Teachers_Info:
                for details in Teachers_Info.values():
                    print("------------------------------")
                    for key, value in details.items():
                        print(f"{key}: {value}")
            else:
                print("No Teacher Details Available.\n")

        elif userchoice == "3":
            print("Returning to Home Page.\n")
            break

        else:
            print("Invalid Input.\n ")
  
        
              
                    
                          
#Student Function 
def Students():
    while True:
        print("\n\n\t+++++ Welcome to Students Menu +++++ \n\n 1) Add a Student \n 2) View Students \n 3) Back to Home Page \n ")
        userchoice = input("\tPlease Select your choice:.... ")

        if userchoice == "1":
            Student_Name = input("\nEnter Student Name: ")
            if all(char.isalpha() or char.isspace() for char in Student_Name) and len(Student_Name) >= 5:
                StudentAge = input("Enter Student Age: ")
                if StudentAge.isdigit() and 0 <= int(StudentAge) <= 20:
                    Student_Class = input("Enter Student Class: ").upper()
                    valid_classes = ("JSS", "SSS", "PRIMARY", "NURSERY", "KG", "CRECHE")
                    if any(Student_Class.startswith(cls) for cls in valid_classes):
                        Student_Parent_Phone_Number = input("Enter Parent Phone Number: ")
                        if len(Student_Parent_Phone_Number) == 11:
                            Student_Address = input("Enter Student Address: ")
                            StudentID = "STU-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                            print(f"Student ID: {StudentID}")

                            Students_Info[StudentID] = {
                                "Student ID": StudentID,
                                "Student Name": Student_Name,
                                "Student Age": StudentAge,
                                "Student Class": Student_Class,
                                "Parent Phone Number": Student_Parent_Phone_Number,
                                "Student Address": Student_Address
                            }

                            save_data()  # Save data after adding student
                            print("\nStudent Information successfully saved!")
                        else:
                            print("Phone Number must be 11 digits.")
                    else:
                        print("Invalid Student Class.")
                else:
                    print("Invalid Age. Must be a number between 0 and 20.")
            else:
                print("Invalid Name. Must be at least 5 characters and contain only letters and spaces.")

        elif userchoice == "2":
            if Students_Info:
                for details in Students_Info.values():
                    print("------------------------------")
                    for key, value in details.items():
                        print(f"{key}: {value}")
            else:
                print("No Student Details Available.\n")

        elif userchoice == "3":
            print("Returning to Home Page.\n")
            break

        else:
            print("Invalid Input.\n ")

      
            
                  
# Attendance Function
def Attendance():
    TeacherInput = input("Enter Student ID: ").upper()
    if TeacherInput in Students_Info:
       TeacherAttend = input("Enter \"0\" to mark student absent or \"1\" to mark the student present: ")
       if TeacherAttend == "0":
           print(f"You marked student with ID \"{TeacherInput}\" absent.")
       if TeacherAttend == "1":
           print(f"You marked student with ID \"{TeacherInput}\" present.")
           
       #STOP
    else:
        print(f"{TeacherInput} not found")
def AttendancePage ():
    print("\n\t\t     ATTENDANCE PAGE\n\n")
    username = input("Enter your username:  ").title()
    if username == "Teacher":
        password = input("Enter your password: "). title ()
        if password == "Teacher":
            print("Login Successful! ")
            Attendance ()
        else:
            print("Login Unsuccessful! ")
    else:
        print("Invalid Username ")
    
    
    
    
    
    
    
    
    
    
    #Fees
def Fees():
    while True:
        print("Fees for different classes:\n 1. Creche  = #15000 \n 2. Nursery = #25000 \n 3. Primary = #50000 \n 4. Junior Secondary School = #65000 \n 5. Senior Secondary School = #85000 \n")
        StudentID = input("Enter Student ID or \"0\" to exit: ").upper()
        if StudentID == "0":
            print("You have been redirected to the Home Page. \n")
            break
        elif StudentID in Students_Info:
            student_class = Students_Info[StudentID]["Student Class"]
            
            fees_structure = {
                "CRECHE": 15000,
                "NURSERY": 25000,
                "PRIMARY": 50000,
                "JSS": 65000,
                "SSS": 85000
            }
            for category, fee in fees_structure.items():
                if student_class.startswith(category):
                    print(f"Fees for {student_class}: #{fee}\n")
                    break
            else:
                print("Invalid class category.")
        else:
            print(f"{StudentID} not found")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
load_data()
# Main Program
while True:
    print("\n\n\tWelcome to School Management System\n")
    print("\n\t------------- HOME PAGE ------------\n")
    print(" 1) Manage Teachers \n 2) Manage Students \n 3) Manage Attendance \n 4) Manage Fees  \n 5) Exit \n ")
    userchoice = input("\tPlease Select your choice:...... ")
    if userchoice == "1":
        Teachers()
    elif userchoice == "2":
        Students ()
    elif userchoice == "3":
        AttendancePage ()
    elif userchoice == "4":
        Fees()
    elif userchoice == "5":
        print("Goodbye! Thanks for using this system. ")
        break
    else:
        print("Invalid lnput. Input the correct choice. ")
