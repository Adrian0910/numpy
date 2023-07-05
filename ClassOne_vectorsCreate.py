# First we have to import numpy
import numpy as np


# We can create vectors in numpy using the array function, in this case we create a vector of 3 elements
vector = np.array([1, 2, 3])

# how to know the dimensions of the vector
print(vector.shape)

# how to know the size of the vector
print(vector.size)

# how to know the type of the vector
print(type(vector))

print("*"*20)

# Here we create an array with 3 elemnts 1
print(np.ones(3))

# NOw we can create an array with 3 elements 0
print(np.zeros(3))

# We can create an array with secuencial numbers
print(np.arange(5))

# And we can do the same using aleatory numbers
print(np.random.random(3))

