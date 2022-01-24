num1=input("Enter 1st number: ")
num2=input("Enter 2nd number: ")

try:
    print("Sum of the numbers is ", int(num1)+int(num2))

except Exception as e:
    print(e)


print("Important line is printed even if error occurs")


"""
Advantages of using try and catch :

* Without a try block if an exception occurs the program will surely crash.

* If we have some part of code that is not much important but can cause an 
  exception, then we must write it down in the try block so it does not cause 
  the whole program to crash.
  
"""
a=1
b=12
print(sum((a,b)))
