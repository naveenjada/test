def square(x):
 return x * x
numbers=[1, 2, 3, 4, 5]
sqrList=map(square, numbers)
print(list(sqrList))

 #addition
def addition(n):
	return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (2, 6, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# by using sets map functions in the sets duplicates are not allowed

def change_lower_case(s):
 return str(s).lower()
chars = {'G', 'B', 'E', 'B', 'G'}
result = map(change_lower_case,chars)
print(set(result))

chars = ['g', 'b', 'e','e','b', 'g']
result = list(map(lambda s: str(s).upper(), chars))
print(set(result))

def myfunc(a):
 return len(a)
x=map(myfunc,('apple','mangao','banana'))
print(x)
print(list(x))