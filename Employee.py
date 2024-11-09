class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print()


employee1 = Employee("Susan Meyers", 65383, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 76546, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 29472, "Manufacturing", "Engineer")


employee1.display()
employee2.display()
employee3.display()
'''Start
               |
    Create Employee Class
               |
        Define __init__ and
        display methods
               |
        Main Program:
               |
    Prompt for Employee Details
               |
    Create Employee Objects
               |
     Display Employee Data
               |
              End
'''