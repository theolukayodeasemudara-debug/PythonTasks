import math
print("Give me the value of your opposite.")
opposite = int(input())
print("Give me the value of your adjacent.")
adjacent = int(input())

# hypotenus formula is A^2 + B^2 = C^2
hypotenus = (opposite * opposite) + (adjacent * adjacent)
hyp = math.sqrt(hypotenus)

print(f"Hypotenus is = {hyp}")
