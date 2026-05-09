# collect father's age from the terminal ranging from 1-80
# collect the son's age from the terminal rangin from 1-80
# calculate how many years ago the father was twice as old as his son
# use the formular twice_fathe_age = father_age - (son_age * 2)


father_age = int(input("enter father's age: "))
son_age = int(input("enter son's age: "))

def twice_as_old(age_one, age_two):
    twice_fathe_age = age_one - (age_two * 2)
    return twice_fathe_age
    
print(twice_as_old(father_age,son_age))

