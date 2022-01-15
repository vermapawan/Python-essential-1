I=float("Enter any naturaL number: "))
a=0
b=1
if(I%1==0 and I>0):
    while(I/=1):
        a+=1
        b=b*10
        print("The total numbert of digit is : ",a)
else:print("this is not a natural.")        
