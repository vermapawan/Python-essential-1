h1=int(input("Give me the start time(hour): "))
m1=int(input("give me the start time (minute): "))
d=int(input("Give me the duration in (minutes: "))
d=(h1*60)+m1+d
print("The finish time is=",end="")
print(d//60,d%60,sep=":")
    
