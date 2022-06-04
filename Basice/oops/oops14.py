class  employee:
    no_of_leaves=8

    #constructor
    def __init__(self,name,salary,role) -> None:
        self.name=name
        self.salary=salary
        self.role=role


    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary} and role is {self.role}"
  
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self,other):
        return self.salary + other.salary
  
    def __truediv__(self,other):
        return self.salary / other.salary 
    
    def __repr__(self) -> str:
        return f" employeee ({self.name},{self.salary},{self.role})"
   
    def __str__(self):
        return  f" The name is {self.name},salary is {self.salary} and role is {self.role}"

emp1=employee("harry",354,"Programmmer")
emp2=employee("rohan",81,"cleaner")

print(emp1/emp2)
print(str(emp1))