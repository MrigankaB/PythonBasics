"""
#While Loop
i=0
while(i<45):
    print(i)
    i=i+1
"""

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue