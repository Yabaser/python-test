#This code is for designing the employee management system

#Creating a class 

class Employee:

    #Defining the constructors

    def __init__(self, emp_id, name, department, basic_salary, experience_years):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.experience_years = experience_years
    
    #method creation - calculate_annual_salary()

    def calculate_annual_salary(self):
        final_ctc = self.basic_salary * 12
        return final_ctc
    
    #method creation - apply_increment()

    def apply_increment(self, increment_percent):
        self.basic_salary = (self.basic_salary * ((100 + increment_percent)/100))
        return self.basic_salary
    
    #method creation - add_experience()

    def add_experience(self, years):
        self.experience_years +=years
        return self.experience_years
    
    #method creation - change_department()

    def change_department(self, new_dept):
        self.department = new_dept
        return self.department
    
    #method creation - get_employee_summary()

    def get_employee_summary(self):
        print("The employee details are as follows ")
        print(f"Employee ID:{self.emp_id}")
        print(f"Name:{self.name}")
        print(f"Department: {self.department}")
        print(f"Experience: {self.experience_years} Years")  
        print(f"Current Basic Salary:Rs {self.basic_salary}")

#Creating an object

E1 = Employee(emp_id="IN134", name="Prashant", department="IT", basic_salary=12500, experience_years=2)

#Invoking the methods

E1.add_experience(2)
E1.apply_increment(9)
E1.change_department("HR")
E1.calculate_annual_salary()

#Printing the details

E1.get_employee_summary()

