# define a static threshold
# collect user value from the terminal
# check for the unit in which user enters their value to determine which function to use
# use the standard formlar given c = (f - 32)* 5/9, to calculate for fahrenheit to celsius
# use f = (c * 9/5) + 32 to convert from celsius to fahrenheit
# check whether the converted temperature is below or above the given threshold


celsius_threshold = 20
fahrenheit_threshold = 68
temp = input("enter a temperature value: ").lower()

unit = temp[-1]
number = int(temp[:-1])
# print(unit, number)

def fah_converter(number):
    fahrenheit = (number * 9/5) + 32
    return fahrenheit

def cel_converter(number):
    celsius = (number - 32) * 5/9
    return celsius


if unit == "f":
    converted = cel_converter(number)
    if converted < celsius_threshold:
        print(f"{converted:.2f}C - Cold advisory")
    else:
        print(f"{converted:.2f}C - Heat alert")
        
elif unit == "c":
    converted = fah_converter(number)
    if converted < fahrenheit_threshold:
        print(f"{converted}F - Cold advisory")
    else:
        print(f"{converted}F - Heat alert")
else: print("invalid temperature value")



