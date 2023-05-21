
#list methods
jaya=[2,34,90,0,1,68,4,80]
jaya.append("python")    #append used for add one element
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.extend("python")    #extend using for adding  bulk  of data
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
j=jaya.copy()
jaya.append(234455)
print(j)
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.clear()
print(jaya)

jaya=[2,34,90, 6,6,6,6,60,1,68,4,80]
print(jaya.count(6))

jaya=[2,34,90,0,1,68,4,80]
jaya.insert( 4,"python")
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.pop(4)          #pop take index to remove element
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.remove(80)        #remove take element
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.reverse()        
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.sort()   # ascending 
print(jaya)

jaya=[2,34,90,0,1,68,4,80]
jaya.sort( reverse=True)  #descending
print(jaya)

y=[2,34,90,0,1,90,68,4,6,90,9,32]
for x in range(len(y)):   #identify the index
    if y[x]==90:
       print(x)

jaya=[2,34,90,0,1, 90,68,4,90,80]
for x in range(len(jaya)):
    if jaya[x]==90:     #replacing the element
       jaya[x]=22
print(jaya)

#list compherension
print([i+14 for i in [4,5,6,3,2,7,]])
print(["even" if i%2==0  else "odd"  for i in (2,4,6,8,10,12,14,16,18,20)])


print([32+i if i%2==0 else 22+i  for i in (0, 2,4,6,8,10,12,14,16,18,20)])