class  employee:
    no_of_leaves=8
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role


    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary} and role is {self.role}"

harry=employee('harry',4554,"instructor")
rohan=employee("rohan",4554,"student")

# harry.name='harry'
# harry.salary =4554
# harry.role="instructor"

# rohan.name="rohan"
# rohan.salary=4554
# rohan.role="student"

print(rohan.printdetails())

print(harry.printdetails())