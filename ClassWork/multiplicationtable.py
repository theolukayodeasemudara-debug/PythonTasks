# 1.collect user input using Scanner
# 2.use a loop to loop over the input collected


user_number = int(input("enter a number: ")) 
index = 1
for number in range(1,11):
    product = number *  index
    print( user_number, "x", number, "=",product);
    index+=1
