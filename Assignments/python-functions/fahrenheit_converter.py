# define a static threshold
# collect user value from the terminal
# check for the unit in which user enters their value to determine which function to use
# use the standard formlar given c = (f - 32)* 5/9, to calculate for fahrenheit to celsius
# use f = (c * 9/5) + 32 to convert from celsius to fahrenheit
# check whether the converted temperature is below or above the given threshold


celsius_threshold = "20C"
fahrenheit_threshold = "68F"
temp = input("enter a temperature value: ")

unit = temp[-1]
number = temp[:-1]
# print(unit, number)

def fah_converter(number):
    fahrenheit = (number * 9/5) + 32
    return fahrenheit

def cel_converter(number):
    celsius = (number - 32) * 5/9
    return celsius


if(unit == "f"):
    print(fah_converter(number))
elif(unit == "c"):
    print(cel_converter(number))

