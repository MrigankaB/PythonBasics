f= open("17text.txt","w")  #"w" is by default, Erases and writes from line 1
a= f.write("Will I am\n")
print(a)  # print no. of character we have appended
f.close()

k= open("17text.txt","a")
k.write("Meet you soon")    # Cannot read
k.close()

"""
g= open("17text.txt","r+") # "r+" can read write(append)"
g.write("Thank You\n")
print(g.read())
g.close()
"""