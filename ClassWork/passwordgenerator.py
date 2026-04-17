# create a program that evaluates the strength of a user's password based on its length. The program should prompt the user to enter a password, analyze its length, abd classify it into one of four categories: "Very weak", 'weak', 'Strong', or 'very strong'.

# pseudo code
# 1.Start the program
# 2.collect a user's supposed password
# 3.check the length of the password using len() checker
# 4.use for select statements to check the category it falls in
# 5.print the category to the user

user_password = input("Enter a password: ")

length_checker = len(user_password)


if(length_checker < 8):
    print("very weak")
elif(length_checker == 8):
    print("weak")
elif(length_checker == 8 and length_checker <= 16):
    print("strong")
elif(length_checker > 16):
    print("very strong")
    




