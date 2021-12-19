number=int(input("enter a number"))
print("the divisor of the given no are:")
for i in range (1,number//2+1):
    if(number%i==0):
        print(i,end=", ")
print(number)
