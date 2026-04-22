# collect the 5 digits 
# divide by 10000 to get the last digit
# divide the number with modolus to get reminder



num = int(input("Enter a five-digit number: "))

divisor = 10000

while divisor > 0:
    digit = num // divisor
    print(digit, end=' ')
    num = num % divisor
    divisor //= 10
