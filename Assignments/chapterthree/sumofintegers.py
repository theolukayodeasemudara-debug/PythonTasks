#Prompt the user to enter the first integer
#Input the first integer
#Prompt the user to enter the second integer
#Input the second integer
#Add first integer and second integer, store their sum
#Display the numbers and their sum




students = 10
passes = 0
count = 0

while count < students:
    while True:
        result = int(input("Enter result (1 = pass, 2 = fail): "))
        
        if result == 1:
            passes += 1
            break
        elif result == 2:
            break
        else:
            print("Invalid input. Enter 1 or 2 only.")
    
    count += 1

failures = students - passes

print("Passes:", passes)
print("Failures:", failures)
