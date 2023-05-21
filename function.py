# def first_function():
#     print("this is my first function")
# first_function()    

# def thanu():            #function definition
#     print("this is devi")  
# thanu()     #function calling

# def thanusha(a):   # here "a" is parameter
#     print(a)
# thanusha(100)     #100 is argunment

# def my_sum(a,b):   #multiple parameters
#     print(a,b)
#     my_sum(10,20)    

# def raju(*a):     #arbitary argunment
#     print(a)      #a* is to assign argunment to parameter 
# raju(12,23,14)    

# def raju(**a):     # keyword argunments
#     print(a)      
# raju(name="thanusha",age=19)   # it stores the data in dictionary formate

# #function within a function(nested function)

# def outer_fun():
#     print("outer_fun")
#     def inner_fun():
#         print("inner fun")
#     inner_fun()    
# outer_fun()



# loreal=10 #global variable
# def a():
#     meera=12 #local variable
#     print(meera,loreal)
# a()  

# def add(a,b):  # module is file name
#     print(a+b)
# def  sub(a,b):
#     print(a-b)  
# def  mul(a,b):
#     print(a*b)    
# def  div(a,b):
#     print(a/b)




# #advance function

# t = lambda a ,b ,c : a + b + c
# print(t(3,4,5)) 

# f=lambda a:a*3
# print(f("python"))

# l1=[12,4,56,7]
# l2=[]
# for i in l1:
#     t=lambda a:a+1
#     l2.append(t(i))
# print(l2) 

   
# #function

# ages=[5,7,8,18,49,24,64,34]
# def myFunc(x):
#     if x>=18:
#        return True
#     else:
#       return False
# adults = filter(myFunc, ages)
# print(list(adults)) 

#   # map

# numbers={2,4,6,8,10}
# def calculateAddition(f):
#     return f+f
# result = map(calculateAddition,numbers)
# print(list(result))

# #reduce

# from functools import reduce
# d=reduce(lambda a,b :a*b,[34,56,8,9])
# print(d)

# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
# x = simpleGeneratorFun()
# print(x.__next__()) 
# print(x.__next__()) 
# print(x.__next__())    

# #writing CALCULATOR program by using functions
# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiple(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a=int(input("enetr the value"))
# b=int(input("enter the value"))
# thanu=input("enter the option")
# if (thanu=="+"):
#   print(add(a,b))
# elif (thanu =="-"):
#     print(sub(a,b))
# elif (thanu =="*"):
#    print(multiple(a,b))
# elif (thanu =="/"):
#    print(div(a,b))
# else:
#     print("entered wrong option")   













# writing  ATM program using functions
print("welcome to python bank")
print("insert your card")
print(int(input("enter the pin")))
amount= 50000
print("1.credit,2.debit,3.balance")
thanu=int(input("choose option"))
def credit():
    a=int(input("enter the amount"))
    b=a+amount
    print(b)
def debit():
    c=int(input("enter the amount"))
    d=c+amount
    print(d)
def balance():
    print(amount)
if thanu==1:
    credit()
elif thanu==2:
    debit()
else:
    balance()        




