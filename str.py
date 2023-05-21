# #  #string
# ram='medico'
# hema="medico"
# haritha='''medico'''  # in triple quotes we can write multiple lines 
# print(type(ram),type(hema),type(haritha))

#  #string methods
# ram='MEDICO'
# hema="medico"
# print(ram.lower())   #lower case convert the data into small letters
# print(hema.upper())  #upper case convert the data into capital letters

# ram="my college is a special place.it gives energy to me. it is a beautiful place"
# print(ram.count("it"))  
# print(len(ram))    #len is used for check the length of the line with spaces

# ram="my college is a special place"
# print(ram.endswith("place"))  
# print(ram.startswith("my"))

# ram="      these are the grapes            " 
# print(len(ram)) 
# print(len(ram.strip()))   #strip used to remove space on both sides
# print(len(ram.lstrip()))  #leftstrip used to remove left space
# print(len(ram.rstrip()))  #rightstrip used to remove right space

# names=["thanusha","varsha","anjali","sasi"]
# for i in names:                       # format is used when it has a constant string
#     print("hello.... {}".format(i))

# sasi="collection of characters is called string"
# a=sasi.split()     #split converts string to list
# print(a)  
# b=" ".join(a)      #join converts list to string 
# print(b)


# a="python"
# print(a.isalpha())

# a="python"
# print(a.isnumeric())

# a="122334556"
# print(a.isnumeric())

# a="sasi"
# print(a.isalnum())

# a="122334556"
# print(a.isalnum())

# jaya="there is a beautiful place"
# print(jaya.find("are"))    #find show the -1 in the place of error
# print(jaya.index("a"))     #index show the error

# jaya="there is a beautiful place"
# print(jaya.replace( "is","are"))

# chapter_name="methods of string"
# print(chapter_name.title())


# #paragraph data replace "is" with "are" and "there" with "that"
# para=''' there are two main systems of water disribution,the intermittent system,
# water is delivered in fixed hours.the safe water is likely to be rendered unsafe through improper storage
# there is a negative pressure. there is health hazard.
# '''
# t=para.split()
# n=[]
# for i in a:
#     if i=="there":
#         i="that" 
#         n.append(i)
#     elif i=="is":
#           i="are"
#           n.append(i)
#     else:
#         n.append(i)
#     t="  ".join(n)
# print(t)


# code to reverse the even places

d="iam learning python from python life"
print("iam"[::],"learning"[::-1],"python"[::],"from"[::-1],"python"[::],"life"[::-1])
        








