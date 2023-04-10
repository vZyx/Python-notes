
name1 = input("Enter the first stduent's name: ")
id1 = input("Enter the first stduent's ID: ")
grade1 = float(input("Enter the first stduent's grade: "))

name2 = input("\nEnter the second stduent's name: ")
id2 = input("Enter the second stduent's ID: ")
grade2 = float(input("Enter the second stduent's grade: "))

print('\n\nInformat for students and their "Math" grades')
msg = name1 + '(ID ' + id1 + ') got grade: ' + str(grade1)
print(msg)
msg = name2 + '(ID ' + id2 + ') got grade: ' + str(grade2)
print(msg)

average = (grade1 + grade2) / 2.0
print('Average math grade is', average)
