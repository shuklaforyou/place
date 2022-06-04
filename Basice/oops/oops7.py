#single inhertance


from re import L


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

        
#   A static method is also a method that is bound to the class and not the object of the class.
# A static method can’t access or modify the class state.
# It is present in a class because it makes sense for the method to be present in class.
    @staticmethod
    def printgood(string):
        print("this is good " + string)
 

class programmer(employee):
    no_of_holiday=58
    def __init__(self, name, salary, role,languages) -> None:
        super().__init__(name, salary, role)
        self.languages=languages


    def printprog(self):
        return f"The Programmer's name is {self.name}.salary is {self.salary} and role is {self.role}.this languages are {self.languages}"


harry=employee('harry',4554,"instructor")
rohan=employee("rohan",4554,"student")


shubham = programmer("shubhum",555,"Programmer",["python"])
karan = programmer("karan",777,"Programmer",["python","cpp"])
print(karan.printprog())
print(karan.printdetails())
print(karan.no_of_holiday)
print(shubham.salary)