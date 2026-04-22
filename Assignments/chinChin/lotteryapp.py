import random

p_one = int(input("Enter your first one digit number: "))
r_one = random.randint(1, 9)

p_two = int(input("Enter your second one digit number: "))
r_two = random.randint(1, 9)

if r_one == p_one and r_two == p_two:
    print(f"Lottery number: {r_one}{r_two}  player number: {p_one}{p_two} \nCongratulations you have won $10,000")
elif r_one == p_one or r_one == p_two or r_two == p_one or r_two == p_two:
    print(f"Lottery number: {r_one}{r_two}  player number: {p_one}{p_two} \nCongratulations you have won $1,000")
else:
    print("Your money is gone")
