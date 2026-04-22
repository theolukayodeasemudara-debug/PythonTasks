num_one = input("what is your first number: ")
num_two = input("what is your your second number: ")
num_three = input("what is your third number: ")


# converting the values from the input to int
num_one = int(num_one)
num_two = int(num_two)
num_three = int(num_three)

print("The sum is; ", num_one+num_two+num_three)
print("The average is: ", (num_one+num_two+num_three)/3)
print("The product is: ", num_one*num_two*num_three)

if num_one > num_two:
    print("the largest number is: ", num_one)
elif num_two > num_three:
    print("the largest number is: ", num_two)
elif num_three > num_two:
    print("the largest number is: ", num_three)

if num_one < num_two:
    print("the smallest number is: ", num_one)
elif num_two < num_three:
    print("the smallest number is: ", num_two)
elif num_three < num_two:
    print("the smallest number is: ", num_three)
