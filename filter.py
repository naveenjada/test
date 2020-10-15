# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o','u','w']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e','j', 'i','j', 'k', 's', 'p', 'r','w']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)
# a list contains both even and odd numbers.
'''seq = [0, 1, 2, 3, 5, 8, 13]

#odd numbers
result = filter(lambda x: x % 3 != 0, seq)
print(list(result))
 #even numbers
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))'''
