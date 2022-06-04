class  employee:
    no_of_leaves=8
    pass 

harry=employee()
rohan=employee()

harry.name='harry'
harry.salary =4554
harry.role="instructor"

rohan.name="rohan"
rohan.salary=4554
rohan.role="student"
print(rohan.__dict__)
print(harry.__dict__)
rohan.no_of_leaves=9
employee.no_of_leaves=8
print(rohan.no_of_leaves)
print(employee.no_of_leaves)

print(employee.__dict__)
