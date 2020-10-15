
# python program to demonstrate
# creation of list



List=[]
print('blank list ')
print(List)

# creating list of numbers
List=[3,5,7]
print('\nList of numbers:')
print(List)

# creating a list of strings and aceesing using index

List=["naveen","appu","radhika"]
print("\nList of items:")
print(List[0])
print(List[1])

# creating a multi-dimensional List and accesing using index

List=[[5],[8],[23]]
print("\nList multi-of dimensions:")
print(List[1])
print(List[0])

# creating a list with mixed values it's means that(strings & integer values)

List=[1,'raja','bunny',8,10,10,'Bank']
print("\nList with the use of Mixed values:")
print(List)

# knowing the size of List
List1=[]#empty of list
print('\nList1 empty size')
print(len(List1))
List2=[5,8,10,78]        #creating list of numbers
print("\nList2 of size:")
print(len(List2))'''

# here on words code different(my purpose)

# addition the elements to a list by using append()
'''List=[]
print(List)
List.append(1)
List.append(2)
List.append(6)
print('\nList after Addition of two elements:')
print(List)

# adding the elements to the list
#using iterator

for i in range(1,6):
 List.append(i)
print("\nList adding the elements using iterator:")
print(List)
# --->iteration is nothing but Repeated execution of set of statements is called iteration

# adding the tuples into list

List.append((8,7))
print("\nList Adding the tuples")
print(List)

#Addition of List into List
List2=['raja', 'kiran', 'hemu']
List.append(List2)
print("\nList Addition of List into List:")
print(List)

# insert method()......>it requries (position & value)
List=[6,7,8,9]
print(" intial List:")
print(List)
List.insert(3, 15)
List.insert(4,17)
List.insert(0,'kiran')
print('\nList after performing insert operations:')
print(List)'''


# extend method()......>it requries for the multiplication

'''List=[78,9,7,1,3]
print("\nIntial values:")
print(List)
List.extend([4,'thamudhu','geeks'])
print("\nList after performing extending operations:")
print(List)'''

# Python program to demonstrate
# accessing of element from list

# Creating a List with
#the use of multiple values
'''List = ["Geeks", "For", "Geeks",]

# accessing a element from the
#list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List

List = [['Geeks', 'For','naveen','lovely'] , ['appu','raju','kitta','raja']]
# index1                               #index2
# Multi-Dimensional List using index number
print("Acessing a element from a Multi-Dimensional list")
print(List[1][3])
print(List[0][2])


# iteration: is nothing but repeated execution.until the conditions satisfied.
# by using while loop
i = 1
while(i < 10):  # here 1<10 condition is true now i becomes 2 (this process will go on up 9<10)
    i += 1 or i + 1
    print(i),
 # now 10<10 condiotion is false now repeated execution will stop


 #iteration on strings
s = "naveen raja"
for i in s :
 print (i)

#iteration on List
List=[1,3,5,7,9]
for i in List:
 print(i),

  #ranges in iteration
for i in range(5,10):
 print(i)

#list comparasion 
l=[x for x in range(1,11)if x%2==0]
print(l)'''

