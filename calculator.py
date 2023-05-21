 

# writing calculator program using python

a=int(input("enter the first value"))
b=int(input("enter the second value"))
print("1.addition, 2.substraction, 3.multiplication, 4.division")
i= int(input("select the opration"))
if(i==1):
    c=a+b
    print("addition value:",c)
elif(i==2):
    c=a-b
    print(" substraction value:",c)
elif(i==3):
    c=a*b
    print("multiplication value:",c)
elif(i==4):
    c=a/b
    print(" division value:",c)
             