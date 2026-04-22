# principal amount 10000
# rate 7% = 0.07

amount = 10000
rate = 0.07

for year in range(1, 31):
    amount *= (1 + rate)
    print(f"Year {year}: {amount:.2f}")
