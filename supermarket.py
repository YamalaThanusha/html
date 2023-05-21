from datetime import datetime
name=input("enter your name")
#Lists of items
lists='''
wheat flour   30/kg
rice          50/kg
maggi         20/each
salt          10/kg
oil           120/lit
sugar         30/kg
soaps         20/each
ragi flour    35/kg
dal           40/kg
chocolate     20/each
tea powder    50/kg
coffee powder 45/kg
'''

#rates for item
items={"wheat flour":30,
"rice":50,
"oil":120,
"sugar":30,
"maggi":20,
"salt":10,
"soaps":20,
"ragi flour":35,
"dal":40,
"chocolate":20,
"tea powder":50,
"coffee powder":45}
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

option=int(input("enter 1 for lists:"))
if option==1:
    print(lists)
for i in range(len(items)):
    a=int(input("do you want  to buy enter 1 or 2 for exit:"))
    if a==2:
        break
    if a==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("your entered item is not in list:")
    else:
        print("your entered wrong number") 
    b=input("can i bill the items press yes or no:")
    if b=="yes":
       print("ok")
       if finalamount !=0:
        print(30*"=","dollar tree",30*"=")
        print(30*" ","rajamundhry")
        print("name:",name,30*" ","Date:",datetime.now())
        print(80*"-")
        print("sno",10*" ",  "items",2*" " ,  "quantity",5*" ",   "price",10*" ")
        for i in range(len(pricelist)):
            print(i,10*" ",2*" ",ilist[i],5*" ",qlist[i], 10*" ",plist[i])
            print(80*"-")
            print(50*" ","TotalAmount:",'Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(80*"-")
            print(50*" ","FinalAmount:",'Rs',finalamount)
            print(80*"-")
            print(50*" ","Thanks For Visiting")
            print(80*"-")
            print(35*"=","Visit Again",35*"=")
            
