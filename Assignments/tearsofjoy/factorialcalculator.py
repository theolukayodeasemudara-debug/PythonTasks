# 10. Factorial calculator
# Calculate the factorial of a number n entered by the user using a while loop.
# Expected output: 
# Enter n: 5 
# Factorial: 120

user_num = int(input("enter a number: "))
factor = 0

while user_num <= 1:
    factor +=1
    user_num * factor
    print(factor)
    user_num-=1
