
f= open("16text.txt")
print(f.tell())     #present position of the pointer
print(f.readline())
print(f.tell())
f.seek(0)   #reset the poiter to the given position
print(f.tell())
print(f.readline())
f.close()