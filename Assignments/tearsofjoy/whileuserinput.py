user_num = int(input("enter a number: "))

while user_num <= 0:
    user_num = int(input("enter a number: "))
    if user_num > 0:
        print(f"You entered {user_num}!")
        break
