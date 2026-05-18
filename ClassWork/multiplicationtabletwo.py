# write a script that generate multiplication table as displayed below


for number in range(1,10):
    print(number,"|",end=" \t")
    for multiply in range(1,10):
        print(number * multiply,end=" \t")
    print()
