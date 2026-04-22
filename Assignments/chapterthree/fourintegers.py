# total range is 4
# total the sum of the integers
# calculate the product and average
# print results




numbers = []

for i in range(4):
    num = int(input("Enter integer: "))
    numbers.append(num)

total = sum(numbers)
product = 1
for n in numbers:
    product *= n

average = total / 4

print("Sum:", total)
print("Average:", average)
print("Product:", product)
print("Smallest:", min(numbers))
print("Largest:", max(numbers))
