# position,name,age,level,salary

se1 = ["Software Engineer","Sayak",21,"Junior",5000]
se2 = ["Software Engineer","Priyanka",23,"Senior",7000]

def code_list(se):
    print(f"{se[1]} is writing code...")

print("From the List")
code_list(se1)
code_list(se2)

print("")
class SoftwareEngineer:
    # constructor
    # Instance Attributes
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method access instance variable
    def code(self):
        print(self.name,"is writing code...")

    def code_in_language(self, language):
        print(self.name,f"is writing code in {language}")

    def information(self):
        information = f"name:- {self.name}, age:- {self.age}, level:- {self.level}, salary:- {self.salary}"
        return information

    # dunder method
    def __str__(self):
        information = f"name:- {self.name}, age:- {self.age}, level:- {self.level}, salary:- {self.salary}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


se1 = SoftwareEngineer("Sayak",21,"Junior",5000)
print(se1.information())
se1.code()# call instance method
se1.code_in_language("Python")
print(se1)

se2 = SoftwareEngineer("Priyanka",23,"Senior",7000)
print(se2.information())
se2.code()
se2.code_in_language("C++")
print(se2)

