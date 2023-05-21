#sets
kavya={"a",1,2.3}  #based on input
print(type(kavya)) 

thanusha={"a",False,2.3,0,1.2,203,58}
print(thanusha)

#set methods

radha={2,2.3,4,5,79,9}
radha.add("krishna")
print(radha)

krishna={"yashoda","radha",2.3 ,45,90}
krishna.remove("radha")
print(krishna)

krishna={"yashoda","radha",2.3 ,45,90}
krishna.update({'rani'})
print(krishna)

krishna={"yashoda","radha",2.3 ,45,90}
krishna.pop()
print(krishna)

krishna={"yashoda","radha",2.3 ,45,90}
krishna.copy()
v=krishna
v.add("latha")
print(v)

krishna={"yashoda","radha",2.3 ,45,90}
krishna.clear()
print(krishna)


#set operations

t1={3,6,5,4,7,}
t2={1,2,3,4,5}     #all elements printed without common elements
print(t1.union(t2))

t1={3,6,5,4,7,} 
t2={1,2,3,4,5}      # only common elements are printed
print(t1.intersection(t2))

t1={3,6,5,4,7,}
t2={1,2,3,4,5}       #only uncommon elements
print(t1.difference(t2))

t1={3,6,5,4,7,}
t2={1,2,3,4,5}       
print(t1.isdisjoint(t2))

t1={1,2,3,4}
t2={3,4}
print(t1.issuperset(t2))

t1={1,2,3,4}
t2={3,4}
print(t2.issubset(t1))

t1={1,2,3,4}
t2={3,4}              #without common elements
print(t1.symmetric_difference(t2))






#frozen set
f=[1,34,68909,7486,45.98,9,354]
g=frozenset(f)
print(min(g))

f=[1,34,68909,7486,45.98,9,354]
g=frozenset(f)
print(max(g))

f=[1,34,68909,7486,45.98,9,354]
g=frozenset(f)
print(len(g))

f=[1,34,68909,7486,45.98,9,354]
g=frozenset(f)
print((g))