"""
Tip: to get the percentage monthly rate, you divide the annual
interest rate by percentage and number of months in a year and to
get the number of months from the duration you multiply it by
number of months in a year
"""


# collect and convert user's input to a number
amt = int(input("How much do you wish to borrow? "))
dur = int(input("What is your preferred duration? "))
rate = float(input("Enter your interest rate "))

# check the input type
# print(type(loan_amount))

"""
m = mortgage calculator
p = principal amount
r = rate
n = duration of the loan
"""
# PEMDAS (Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction)
m = amt*(dur*(rate*1+rate*rate) // (dur*(1+rate)-1))

print("Your monthly repayment is", m)
