#finding compound intrest
p=int(input("enter the principal amount"))
r= float(input("enter the rate"))
n=int(input("enter the no of times intrest is compounded"))
t=int(input("enter the time period"))
a=p*((1+r/n)**n*t)
print("total amount :", a)
ci=a-p
print("compound interest:",ci)

