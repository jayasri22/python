a = int(input("Enter a value: "))  
  
if a > 1:  
   for i in range(2,a):  
       if (a % i) == 0:  
           print(a,"no")  
           print(i,"times",a//i,"is",a)  
           break  
   else:  
       print(a,"yes")  
         
else:  
   print(a," no")  
Output:
