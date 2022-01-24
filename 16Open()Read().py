f= open("16text.txt","rt") #rt is default
# content=f.read()
# print(" ## ",content)   # Curser is at end. So next it will print blank

# content=f.read(20)    # read first 20 characters
# print("1 ",content)
# content=f.read(20)    # read next 20 character
# print("2 ",content)

# for line in f:
#    print(line, end="")

# print(f.readline())   # read 1 line

print(f.readlines())    # print as list

f.close()      # To free resources, So other process can read too
