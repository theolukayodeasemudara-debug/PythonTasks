# 11. Sentinel: stop on zero
# Keep reading integers from the user. When they enter 0, stop and print the total of all entered numbers.
# Expected output: Enter: 4 / Enter: 7 / Enter: 0 / Total: 11

total = 0
while True:
    user_num = int(input("enter a number: "))
    total+=user_num
    if user_num == 0:
        print(f"You total is {total}!")
        break
