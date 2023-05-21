#writing ATM program using python
print("welcome to python bank")
print("insert the card")
print(input("enter the pin"))
amount=30000
print("1.credit, 2.debit, 3.balance enquiry, 4.exit")
t=int(input("select option"))
if (t==1):
    a=int(input("enter the amount"))
    b=amount+a
    print(" after credit the amount:",b)
elif(t==2):
    print(" withdrawl amount:" ,3000)
elif(t==3):
    print("balance amount:")
else:
    print("exit")        

 