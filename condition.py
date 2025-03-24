#if-else statement 
#correct email binisha@gmail.com and password=binisha123
# email=input("Enter your email")
# password=input("Enter your password")
# if email=="binisha@gmail.com" and password=="binisha123":
#     print("Welcome")
# else:
#     print("Wrong email and password")


#if email correct and password failed give another chance
# email=input("Enter your email")
# password=input("Enter your password")
# if email=="binisha@gmail.com" and password=="binisha123":
#    print("Welcome")
# elif email=="binisha@gmail.com" and password!="binisha123":
#    print("Password incorrect")
#    password=input("Again enter your password")
#    if password =="binisha123":
#       print("welcome")
#    else:
#       print("wrong password")
# else:
#    print("Wrong credential")

# to check email format @ 
email=input("Enter your email")
 
if "@" in email:
    password=input("enter your password")
    if email=="binisha@gmail.com" and password=="binisha123":
        print("Welcome")
    elif email=="binisha@gmail.com" and password!="binisha123":
        print("invalid password")
        password=input("Enter password again")
        if password=="binisha123":
            print("welcome")
        else:
            print("incorrect again")
    else:
        print("login failed")
else:
    print("invalid gmail format")

