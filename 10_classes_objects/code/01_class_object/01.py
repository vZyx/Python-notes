
# This is a bit improper...wait with me
class Employee:
    name = None
    salary = None
    address = None

mostafa = Employee()
mostafa.name = 'mostafa saad'
mostafa.salary = 1000
mostafa.address = 'Lovely Canada'

print(mostafa.address)  # Lovely Canada

emp2 = Employee()
emp2.name = 'belal mostafa saad'
emp2.salary = 0
emp2.address = 'Same as his dad'

print(emp2.address)  # Same as his dad
emp2.address = 'BC'
print(emp2.address)  # BC

emp3 = Employee()
emp4 = Employee()

