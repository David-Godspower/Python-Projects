import random
import string 
print("This is a simple payroll system")

Payroll = {} #payroll dictionary 

    
    
# Function for Adding of Employees 
def AddEmployee ():
    try:
        i =i+1
        while True:
           
            choice=int(input("Enter number of employees to be added or \"0\" to quit: ")) # Accepting choice for number of employees to be added
            if choice== 0:
                print("Goodbye \n")
                break 
                # The loop for addition of the employee starts
            while i<=choice:
                employee_name = input(f"\nEnter Employee {i}'s name: ").title()
                if all(char.isalpha() or char.isspace() for char in employee_name) and len(employee_name) >= 5:
                    known_id = input("Did Employee has ID? (Yes or No)").lower()
                    if known_id == "yes":
                        EmployeeID = input("Enter Employee ID:").upper()
                        if EmployeeID in Payroll:
                            print(f"{EmployeeID} already exist")
                            continue 
                        if not EmployeeID.startswith("POW-") and not len(EmployeeID) ==9:
                                  print("Invalid ID")
                                  continue 
                        
                    elif known_id == "no":
                        EmployeeID = "POW-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))# Generate ID for the employees 
                        
                    else:
                        print("Invalid Input" )
                        continue 
                    employee_email = input("Enter Employee's email address: ").lower()
                    if not (employee_email.endswith("@gmail.com") and  len(employee_email) >=5):
                        print("Invalid Email Address")
                        continue 
                    employee_phonenumber = input("Enter Employee's phone number: ").replace(' ', '').replace('-', '')
                    if not (employee_phonenumber.startswith('0') or employee_phonenumber.startswith('+')):
                      print("Invalid Phone Number ")
                      continue  
                    if not (10 <= len(employee_phonenumber) <=15 and employee_phonenumber.replace('+','').isdigit() ):
                        print("Invalid Phone Number ")
                        continue 
                    salary_per_hour = int(input("Enter salary per hour($): "))
                    
                    if salary_per_hour <= 0:
                        print("Salary per hour can't be less than Zero")
                        continue 
                    else:
                        Payroll[EmployeeID] = {
                            "Employee ID": EmployeeID,
                            "Employee Name": employee_name,
                            "Employee Email Address": employee_email,
                            "Employee Phone Number": employee_phonenumber,
                            "Salary Per Hour($)": salary_per_hour,
                          }

                        print("Employees' data saved successfully ")
                        print(f"\n     Employee with ID ({EmployeeID})'s data \n Employee Name: {employee_name} \n Employee ID: {EmployeeID} \n Salary: ${salary_per_hour}\n")
                    i=i+1
                   
                else:
                    print("Name must be alphabets and at least five characters \n")
    
    except ValueError:
        print("You didn't enter a valid input\n ")
        


# Salary Calculations
def CalcSalary():
    try:
        EmployeeID = input("Enter the last five value of the Employee's ID: ").upper()
        updatedID = f"POW-{EmployeeID}"
        if updatedID in Payroll:
            hours_worked = int(input("How many hours did the employee work?"))
            total_salary = hours_worked * Payroll[updatedID]['Salary Per Hour($)']
            print(f"Salary for ID, \"{updatedID}\" = ${total_salary}\n")
            Payroll[updatedID]["Total Salary($)"] = total_salary
            
            
        else:
            print(f"\"{updatedID}\" not found. You would be directed to the Adding of Employees Page now. \n")
            AddEmployee()
    except ValueError:
         print("You didn't enter a valid input ")
         
         
         
         
         
 # Payslip
def Payslip():
    if Payroll:
                for details in Payroll.values():
                    print("------------------------------")
                    for key, value in details.items():
                        print(f"{key}: {value}")
    else:
           print("No Employee Data Available.\n")


try: 
# Main Menu
    while True:
        print("\n\n\nWelcome to Power Companies\n ")
        print("        ++++++++++ Main Menu ++++++++++")
        print("\n 1. Add Employee \n 2. Calculate Salary \n 3. View Payslip \n 4. Exit \n ")
        user_choice= int(input("Select  your choice:..")) 
        if user_choice == 1:
            AddEmployee()
        elif user_choice == 2:
            CalcSalary ()
        elif user_choice == 3:
            Payslip()
        elif user_choice == 4:
            print("Thanks for making use of this platform\n")
            break 
        else:
            print ("You didn't enter correct choice ")
except ValueError:
    print("You didn't enter a valid input ")
    