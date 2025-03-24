# time completety of nested loop is n2 based on the  loop
# *
# **
# ***
# ****
# *****

rows=int(input("Enter the numbet of rows"))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*", end=" ")


