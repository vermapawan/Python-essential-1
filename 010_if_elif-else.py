n=int(input("Search any leap year:"))
if n<1582 :
    print("Not Within GREGORIAN CALENDER")
elif n%4>0 :
    print("common year")
elif n%100>0 :
    print("leap year")
elif n%400>0 :
    print("common year")
else:
    print("leap year")
        
