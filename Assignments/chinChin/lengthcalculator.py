print("Write any value lets calculate whether it is a 3 digit number.")
user_val = int(input())


length_of_num = len(str(abs(user_val)))

if length_of_num == 3:
    print(f"{user_val} is a 3 digit number")
else:
    print(f"{user_val} is not a 3 digit number. It has {length_of_num} digit(s)")
