y = int(input("Enter y: "))
if y % 4 == 0 and y % 100 != 0:
    print(y, "Leap Year")
elif y % 100 == 0:
    print(y, " not Leap Year")
elif y % 400 ==0:
    print(y, "Leap Year")
else:
    print(y, "not Leap Year")
