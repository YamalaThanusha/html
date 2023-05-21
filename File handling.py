#file handling
# file handling methods

file=open("demo.txt",mode="r")
content=file.read()     # to read the lines
print(content)
file.close()

file=open("demo.txt",mode="r")
content=file.readline()    # to read one line
print(content)
file.close()

file=open("demo.txt",mode="r")
content=file.readlines()     #to read all lines in file
print(content)
file.close()

file=open("demo.txt",mode="w")
content=file.write("another line of code 2")     
print(content)
file.close()

file=open("demo.txt",mode="w")
content=file.write("iam so happy")     #w will loss the data 
file.close()

file=open("demo.txt",mode="a")
content=file.write(  " this is the data")  # a doesnot loss the data   
file.close()

file=open("demo.txt",mode="r+")
content=file.read()
file.write("   another data")
print(content)  
file.seek(0)   # seek to change the file pointer position
file.close()

file=open("demo.txt",mode="w+")
file.write("iam learning python")
file.seek(0)
print(file.read())   
file.close()

thanu=open("demo.txt","r")
thanu.read()
print(thanu.tell())  # it tells the file pointer current  position
thanu.close

thanu=open("demo.txt","r")
print(thanu.tell())
thanu.read(2)
print(thanu.tell())
thanu.seek(0)
print(thanu.tell())
thanu.close()

file=open ("demo.txt",mode="r+")
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(2,"advanced")
print(file.tell())
file.close()
file=open("demo.txt",mode="w")
print(f)
for i in f:
    file.writelines([i])

#Error Handling

a=2
b=2
try:
    print(a+b)
except:
    print("error vachindi")
else:
    print("error raleadhu")
finally:
    print("always")

try:
    print(2/0)
except Exception as e:
    print("error",e)        

try:
    print(a)
except ValueError:
    print(" value error")
except TypeError:
    print(" type error")
except NameError:
    print(" name error")  
          








try:
    print(a)
except:
    print("name error")
    try:
        print(1/0)
    except:
        print("name error")        


#name error
print(a)    #when we doesnot define a variable name error occurs

#type error
print(1+"r") #we can't add the str and int



























