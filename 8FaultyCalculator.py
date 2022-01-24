# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

def calculate():
    print("Welcome to MriCalculator")

    print("+ for addition")
    print("- for subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("^ for power")
    print("% for Modulo")

    print("Enter the operation you want to perform: ")
    op= input()

    #print("Enter 1st number: ")
    n1= int(input("Enter 1st number: "))

    #print("Enter 2nd number: ")
    n2= int(input("Enter 1st number: "))

    if op== "*" :
        if n1==45 and n2==3:
            print("45 * 3 = 555")
        else:
            print(f"{n1}*{n2}={n1*n2}")

    elif op=="+" :
        if n1==56 and n2==9:
            print("56 + 9 = 77")
        else:
            print(f"{n1}+{n2}={n1 + n2}")

    elif op=="/" :
        if n1 == 56 and n2 == 6:
            print("56/6 = 4")
        else:
            print(f"{n1}/{n2}={n1/n2}")

    elif op=="-":
        print(f"{n1}-{n2}={n1 - n2}")

    elif op=="^":
        print(f"{n1}^{n2}={n1 ** n2}")

    elif op=='%':
        print(f"{n1}%{n2}={n1 % n2}")

    else:
        print("Error! Try again")

    again()

def again():
    cal_again= input("Would you like to calculate again? Y/N : ")
    if cal_again== 'y' or 'Y':
        calculate()
    elif cal_again=='n' or 'N':
        print("Adios!!")
    else:
        again()   #or input()==""

calculate()

#Error in again() function
