x=float(input("Enter your income: "))
if x<85528:
    c=(0.18*x)-556.02
    if c<0:
        print("There is no money return")
    else:
        print("The tax is: ",c)
else:
    print("The tax is: ",14839.02+((x-85528)*0.32))
    
    
