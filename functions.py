#calling function
# To call a function, use the function name followed by parenthesis
def my_function():
  print("Hello from a function")

my_function()
# A simple Python function to check
# whether x is even or odd
def evenOdd( x ):
	if (x % 2 == 0):
		print ("even")
	else:
		print ("odd")

# Driver code
evenOdd(2)
evenOdd(3)

# lambda  functions
x = lambda a : a + 10
print(x(5))
