thanu={}
print(type(thanu))

arjun={1:"veni","abi":23,2:9087}
print(arjun)
print(arjun[1])

arjun={1:"veni","abi":23,2:9087}
print(arjun.get("abi"))

arjun={1:"veni","abi":23,2:9087}
print(arjun.items())             #items gives both keys and values

arjun={1:"veni","abi":23,2:9087}
print(arjun.keys())           #it gives only keys as output

arjun={1:"veni","abi":23,2:9087}
print(arjun.values())

arjun={1:"veni","abi":23,2:9087}
print(arjun.pop("abi"))       #in argument we can give only keys

arjun={1:"veni","abi":23,2:9087}
arjun.update({23451:"kajol"}) #adding the data
print(arjun)
arjun.update({1:"thanusha"})  #update the already existed data
print(arjun)

arjun={1:"veni","abi":23,2:9087}
for i,j in arjun.items():
    print(i,j)




#nested dictonary
sri={
    23:"beautiful",
    "list":3746858,
    990:{"first":1,'second':2,'third':3}
}
print(sri.get(990).get("third"))

tuple
tree=(2.2,True,6,85,'dvd',44)
print(tree[-1])   #index possible

#built-in
tree=(2.2,34,6,85,508329,44,4.5643)
print(len(tree))
print(min(tree))
print(max(tree))
print(sum(tree))

#tuple concatenation
d=(2,5,7,8,9)
f=(9,67,33,12)
print(d+f)
print(tuple(zip(d,f)))

#tuple repetition
t=(2,4,6,8)
print(t*4)



