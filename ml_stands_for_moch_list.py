""" Manipulation of lists, n-tuples, Dictionaries """
ml = []

for i in range(101):
    ml.append(i)
    
""" Various examples to slice from a list """
# The ith element of  ml
print("iteration 1: ", ml[i])

# The list of elements with indices starting at 30 and up to (not including) 50
print("iteration 2: ", ml[30:50])

# The first 89 elements
print("iteration 3: ", ml[:89])

# All elements from 30 onwards
print("iteration 4: ", ml[30:])

# The last 10 elements of ml
print("iteration 5: ", ml[-10:])

# Elements from 15 up to (not including) 30 taking only every 10 element
print("iteration 6: ", ml[15:30:10])

# List only even numbers
print("iteration 7: ", ml[::2])

# Reverse a copy of the list
print("Iteration 8: ", ml[::-1])
