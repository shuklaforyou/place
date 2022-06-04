class  employee:
    no_of_leaves=8
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role


    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary} and role is {self.role}"
  
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry=employee('harry',4554,"instructor")
rohan=employee("rohan",4554,"student")

rohan.change_leaves(34)
print(harry.no_of_leaves)
