# list 

t=[22,6,20.3,"thanusha",2]
print(type(20.3))            #"type" is for knowing which data type is that

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[6])                #"forward indexing"(positive indexing)   

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[-6])               #"backward indexing"(negative indexing)

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(len(run))               # "len" is for knowing the length of the list

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[0:10:2])            #slicing ( start: stop: skip)

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[10:0:-3])           #index is in backward direction(but it is positive index)

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[-1:-10:-3])         # backward index slicing

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[::])                #it will  print whole list

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[:8])                #it will print 0 to 8 index values

run=[1,1.1,3,48,"ready",["van",67,89],49.6,67.4,True,False]
print(run[4:])                # it will print 4 to remaining  index values
