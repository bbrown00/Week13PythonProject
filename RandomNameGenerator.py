import random
import string

#Hello Welcome to the Random Name Generator for EC2 instances
print("EC2 Random Name Instance Generator for Departments")
print("")


print("Finops", "Accounting", "Marketing")
print("")

Departments = ('finops', 'Accounting', 'Marketing')
Names = []


#The Department names
departments= ['Finops' , 'Accounting' , 'Marketing']
departments= input("Please enter your department ('Finops', 'Accounting', 'Marketing'):").lower()
print ("")

departments= ['Finops' , 'Accounting' , 'Marketing']
print= input ("Please enter the number of EC2 instances:")

# Enter randomnumber, Characters and Instances
for instance in range(1, 999):
    randomnum = random.randint(1, 999)
    randomchar = ''.join(random.choices(string.ascii_letters, k=10))
    EC2 = "{}_{}{}{}".format(departments, randomnum, randomchar, instance)
    Names.append(EC2)

print(''.join(Names))