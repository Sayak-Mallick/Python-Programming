# position,name,age,level,salary
se1 = ["Software Engineer", "Sayak", 21, "Junior", 5000]
se2 = ["Software Engineer", "Priyanka", 23, "Senior", 7000]


# class
class SoftwareEngineer:
    # class Attribute
    alias = "Defence Aspirant"

    # Instance Attributes/variables
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance/object
se1 = SoftwareEngineer("Sayak", 21, "Junior", 5000)
print(se1.name, se1.age, se1.level, se1.salary)  # printing Instance Attributes
print(se1.alias)  # Printing Class Attributes
print(SoftwareEngineer.alias)  # Printing Class Attributes

se2 = SoftwareEngineer("Priyanka", 23, "Senior", 7000)
print(se2.name, se2.age, se2.level, se2.salary)  # printing Instance Attributes
print(se2.alias)  # Printing Class Attributes
print(SoftwareEngineer.alias)  # Printing Class Attributes
