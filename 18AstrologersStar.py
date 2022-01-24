"""
rows= int(input("Enter number of rows: "))
rev= int(input("Do you want a reverse triangle. Enter 1 if yes and 0 FOR No: "))
bol= bool(rev)
if rev== False:
    for i in range(1,rows+1 ):
        print("*"*i)

elif rev== True:
    for i in range(rows,0,-1):
        print("*"*i)
"""

print("How Many Row You Want To Print")
one= int(input())       #rows
print("Type 1 Or 0")
two = int(input())      #Reverse or not
new =bool(two)

if new == True:
    for i in range(1,one+1):
          for j in range(1,i+1):
              print("*", end="")    #*
          print()
                                    #**
                                    #***

elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end="")       #***
        print()
                                    #**
                                    #*