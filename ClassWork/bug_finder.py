"""
A student wants to swap a= 5 and b = 10 so that a becomes 10 and b becomes 5. They write: a = b; b = a. Explain the bug. Write the correct solution
"""

var_a = 5
var_b = 10
print("variable a: ",var_a,"variable b: ",var_b)

"""
var_a = var_b
var_b = var_a

The error here is that reassigning a to become b and b to become a is automatically making one value which is 10 to remain consistent.

hence a, becomes b and b still takes the same value that it has already replaced at the first instance
"""
# temp = var_a
# var_a = var_b
# var_b = temp

var_a,var_b = var_b,var_a

print("variable a: ",var_a,"variable b: ",var_b)
