num1=int(input("enter the first no:"))
num2=int(input("enter the sec no:"))
print("select operation")
print("1.Add")
print("2.sub")
print("3.multiply")
print("4.div")
choice=int(input("enter ur choice:"))
if(choice==1):
    print(num1+num2)
elif(choice==2):
    print(num1-num2)
elif(choice==3):
    print(num1*num2)
elif(choice==4):
    if(num2==0):
        print("invalid")
    else:
        print(num1/num2)
