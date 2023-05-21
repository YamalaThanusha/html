# # oops (class)


# class thanusha():
#     print("sita is a beautiful girl")
# jaya=thanusha() #object creation

# class thanusha():
#     def display():
#         print("this is thanusha")
#     display()
# jaya=thanusha()        

# class thanusha():
#     def display(self):
#         print("this is thanusha")
# jaya=thanusha()    
# jaya.display()

# class thanu():
#     t=12345
#     def fun(self):
#         print("this is function",self.t)
# obj=thanu()
# obj.fun() 
# print(obj.t )        


# class thanusha():
#     thanu=1
#     def thanusha_fun(self):
#         print("hello",self.thanu)
# thanusha_obj=thanusha()
# thanusha_obj.thanusha_fun()






# class thanu():
#     def thanu(self):
#         print("boi")
# t=thanu()
# t1=thanu()
# t.thanu()
# t1.thanu()    

# class thanu():
#     def j(self):
#         print("jaya")
# t=thanu()
# t.j()        

# a=12
# b=6
# c=22
# def D():
#     print(a)
# D()
# def j():
#     print(b)
# j()        

# class thanu():
#     def __init__(self,a,b,c):
#         self.d=a
#         self.j=b
#         self.t=c
#     def output(self):
#         print(self.d)
# a=thanu(12,6,22)
# a.output()        

# class phone():
#     def __init__(self,phone_name,phone_ram,phone_version,phone_price):
#         self.a=phone_name
#         self.b=phone_ram
#         self.c=phone_version
#         self.d=phone_price
#     def phone_details(self):
#         print("phone name:",self.a)
#         print("phone ram:",self.b)
#         print("phone version:",self.c)
#         print("phone price:",self.d)
# pn=input("enter the phone name:")   
# pr=input("enter the phone ram:")    
# pv=input("enter the phone version:")    
# pp=input("enter the phone price:")         
# phone_obj=phone(pn,pr,pv,pp)
# phone_obj.phone_details()


       
# inheritance
class parent:
    def output(self):
        print("this is parent class")
class child(parent):
    def outputchild(self):
        print("this is the child class")
i=child()
i.output()
i.outputchild()                





class Father:
    def output(self):
        print("this is father class")
class Mother:
    def outputM(self):
        print("this is mother class")
class child(Father,Mother):
    def outputchild(self):
        print("this is child class")
jaya=child()
jaya.output()
jaya.outputM()
jaya.outputchild()













class GrandFather:
    def output(self):
        print("this is grand father class")
class Father(GrandFather):
    def outputf(self):
        print("this is father class")
class child(Father):
    def outputchild(self):
        print("this is child class")
jaya=child()
jaya.output()
jaya.outputf()
jaya.outputchild()

class Father:
    def output(self):
        print("this is father class")
class child1(Father):
    def outputf(self):
        print("this is child1 class")
class child2(Father):
    def outputchild(self):
        print("this is child2 class")
jaya=child1()
thanu=child2()
jaya.output()
jaya.outputf()
thanu.output()
thanu.outputchild()







def test(a,b):
    print(a+b)
test(1,1)
test("k","k")
test([1,3],[3,4])    

class Methodoverlod:
    def something(self,a=None,b=None,c=None):
        print(a,b,c)
obj=Methodoverlod()
obj.something(2,4,6)
obj.something(2,4)
obj.something(2)
obj.something()

class Methodoverri:
    def display(self):
        print("this is parent class")
class child(Methodoverri):
    def display(self):
        print("this is child class")
        super().display()
class child2(child):
    def display(self):
        print("this is child 2 class")
        super().display()
obj=child2()
obj.display()                        
















 #encapsulation
class GFather:
    def __init__(self,a):
        self._y=a
class Father(GFather):
    def display1(self):
        print(self._y)
class child(Father):
    def display2(self):
        print("child",self._y)
obj=child(12)
obj.display1()
obj.display2()                        

class GFather:
    def __init__(self,a):
        self.__y=a
        print(a)
class Father(GFather):
    def display1(self):
        try:
            print(self.__y)
        except:
            print("private variable cannot be accessed")
class child(Father):
    def display2(self):
        try:
            print(self.__y)
        except Exception as e:
            print("private variable cannot be accessed",e)
obj=child(12)
obj.display1()
obj.display2()                                    

    
                    











































































