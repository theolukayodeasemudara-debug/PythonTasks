# collect user inputs
# initialise number of passes to zero
# initialise number of failures to zero
# initialise number_counter to check how many numbers have been collected
# put it in a while loop cause we do not know the count until an incorrect value is entered
# use a select statement to check whether it is a pass or fail value

total = 0
passes = 0
failures = 0
number_counter = 0

number = int(input("Enter number, -1 to end: "))

while number != -1:
    passes = passes + number_counter
    failures = failures + number_counter
    number_counter += 1
    number = int(input('Enter a number, -1 to end: '))
    
    if(number != 0):
        print(f'Your total number of passes is {passes}, while your number of failures is {failures}')

    print('No numbers were entered')

