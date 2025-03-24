# example of variable(string,int,float,boolean)
name="Aman"
age=20
discout=20.4
is_std=True

print(name,age,discout,is_std)
print(f"your name is {name} and your age is {age}");  #this is called fstring

# now for boolean
if is_std:
    print("yes you are student")
else:
    print("no you arent")

# now type()function to check their type like int,str
print(type(name))
print(type(is_std));  #remember one thing we can convert any type of expect character




# variable are container for future use it is a fundamental concept in programming
#no variable decalrae can directly used in python 
#its called dynamic typing (no need to decalrae data type)
# static typing - decalrae varriable type 
#no virable is binded to specific  like yeutai varibale multiple data type store garxa its called dynamic binding



#special syntax
a=5;b=6;c=7
print(a)
print(b)
print(c)

a,b,c=4,5,6
print(a)
print(b)
print(c)