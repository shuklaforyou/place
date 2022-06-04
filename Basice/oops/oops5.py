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
    
    @classmethod
    def form_dash(cls,string):
        # parms=string.split("-")
        # return cls(parms[0],parms[1],parms[2])
        return cls(*string.split("-"))
harry=employee('harry',4554,"instructor")
rohan=employee("rohan",4554,"student")
karan =employee.form_dash("karan-480-student")
rohan.change_leaves(34)
print(karan.__dict__)
