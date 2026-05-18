# def cube(number):
#     return number ** 3
    
    
# print(cube(10))

def largest_checker(num_one,num_two,num_three):
    largest_num = num_one
    
    # longer logic
    # if num_one > num_two and num_one > num_three:
    #     largest_num = num_one
    # elif num_two > num_one and num_two > num_three:
    #     largest_num = num_two
    # elif num_three > num_two and num_three > num_one:
    #     largest_num = num_three
    # return largest_num
    
    # shorter logic
    if num_two > largest_num:
        largest_num = num_two
    if num_three > largest_num:
        largest_num = num_three
    return largest_num
    
    
print(largest_checker(40,20,10))
print(largest_checker(num_three = 70, num_one =10, num_two = 50))
