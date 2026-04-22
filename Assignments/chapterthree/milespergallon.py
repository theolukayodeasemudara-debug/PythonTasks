total_miles = 0
total_gallons = 0

gallons = float(input("Enter gallons used (-1 to end): "))

while gallons != -1:
    miles = float(input("Enter miles driven: "))
    
    mpg = miles / gallons
    print(f"Miles per gallon: {mpg:.6f}")
    
    total_miles += miles
    total_gallons += gallons
    
    gallons = float(input("Enter gallons used (-1 to end): "))

if total_gallons != 0:
    overall = total_miles / total_gallons
    print(f"Overall MPG: {overall:.6f}")
else:
    print("No data entered.")
