# its a data type speacilly aplication programming language like java ,c++
# website, desktop app etc

# striig are sequence of characeter
# in pthon, string are a sequence of unicode character


# slicing =extarcting multiple charactr at ones
c="Hello binisha how are you"
print(c[0:4])
print(c[2:])
print(c[:4])

# last wala 2 ley yeti diff ma chaiyo
print(c[2:6:2])


# emty string positve index snga work gryaxa bney yo ka grdauba negative index snga xa bney mayta
print(c[0:6:-1])


# like this negative index
print(c[-5:-1:2])


# string reverse 
print(c[::-1])

# string are immutable datatype so its can be chage you cannot edit the string after it is created

# we can completely reassign but cannot chage the existing string
c="Hello "
# reaasign hello lai hatayera world leykhya
c="world"
print(c)


#  for deleting we have del keyword
# del(c)
# print(c)

# delete the first character of the string
c = c[1:]
print(c)

# string multiplication
print("*"*50)