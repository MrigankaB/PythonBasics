"""
print("Hello World, ", end="")
print("Mriganka here")
"""
#print("C:\\narry") #to avoid new line(\n)
#print("how are\n you \t")  #\t, \p, \r etc



#variable = container, place value,
"""

var1="hello"
var2=4
var3=36.5

print(type(var1))
print(type(var2))
print(type(var3))

var4="Mriganka"
print(var1+ var4)

print(var2+var3)
print(type(var2+var3))

#Type Casting
print(int(var2)+int(var3))
"""



# print(10*"55\t")

# print(100*int(var2)+int(var3))

#print(10*str(int(var2)+int(var3))) #type Casting



"""
print("Enter a number: ")
num1 = input()
print("Entered numbered is ", num1)  #num is read/recorded as string

print("Enter a number: ")
num1 = input()
print("Entered numbered is ", int(num1)+20)
"""

#program1 - Sum of two numbers
"""
print("enter n1 ")
n1 = input()
print("Enter n2")
n2= input()
print("sum of the numbers are ",int(n1)+int(n2)) #int for String ---> int

"""





# Lecture 9
#String Slicing
"""

mystr= "Hey! How you doing"

print(len(mystr)) #length of string

#slicing from 0-5 from the string
print(mystr[0:5])

#advanced slicing
print(mystr[0:15:3]) #skips 1 letter

print(mystr[::]) #it takes 0 by default

print(mystr[::100])

print(mystr[::-1]) #Reverse the string

print(mystr[::-2])# Reverse the string and skips 1 character

"""


# Important Functions on String
"""

print(mystr.isalnum()) # Returns False ; Not alpha Because of spaces

print(mystr.isalpha()) # False ;Not alpha Because of spaces

print(mystr.endswith("doing")) #O: True

print(mystr.count("H")) # 2

print(mystr.capitalize()) #capitalize first letter

print(mystr.find("How")) # 5

print(mystr.lower()) # hey! how you doing

print(mystr.upper()) # HEY! HOW YOU DOING

print(mystr.replace("!",",")) # Hey, How you doing

"""





#Lecture 10
#List - mutable
"""
grocery=["Harpic", "Vim bar", "Surf Exel", "Bhindi", "Carrot", 16, 20]
print(grocery) # whole list ['Harpic', 'Vim bar', 'Surf Exel', 'Bhindi', 'Carrot', 16, 20]
print(grocery[3]) #Bhindi


numbers=[1,22,3,14,55,6,71,8,93]
print(numbers)  #[1,22,3,14,55,6,71,8,93]
print(numbers[5])  #6

numbers.sort()
print(numbers) #[1, 3, 6, 8, 14, 22, 55, 71, 93]

numbers.reverse()
print(numbers)  # [93, 71, 55, 22, 14, 8, 6, 3, 1]

print(numbers[0:3:2])  # includes every 2nd element or skips 1 element in between
                       # [93, 55]
                     
numbers.append(5)  # adds a new number at the end
print(numbers)     # [93, 71, 55, 22, 14, 8, 6, 3, 1, 5]

numbers.insert(2,101) # [93, 71, 101, 55, 22, 14, 8, 6, 3, 1, 5]
print(numbers)

numbers.remove(93) # [71, 101, 55, 22, 14, 8, 6, 3, 1 , 5]
print(numbers)

numbers.pop()
print(numbers) # [71, 101, 55, 22, 14, 8, 6, 3, 1, ]
"""



#tuple - immutable
"""
a=() # It's an example of empty tuple
x=(1,)  # Tuple with single value i.e. 1

tup1 = (1, 2, 3, 4, 5)

tup2 = ('harry', 5, 'Raj', 8.2, 91, 22)

print(tup2+ tup1) # ('harry', 5, 'Raj', 8.2, 91, 22, 1, 2, 3, 4, 5)
"""


#Swapping two numbers
"""
a=2
b=9
a,b = b,a
print(a)  # 9
print(b)  # 2
"""








#Lecture 11
#Dictionary
"""
d1 = {}
print(type(d1))

d2 = {"Mriganka":"Roti",
      "Partha":"Chicken",
      "Ron":"Fish",
      "Mike":"Ice-Cream",
      "Rikky":{"A":"Burger", "B":"Lolipop", "C":"Paneer"}}
d2["Graham"]="Rolls"
d2["Vanissa"]="Kabab"
d2["Officer"]="Bread"

print(d2)

print(d2["Partha"])
print(d2["Vanissa"])

del d2["Officer"]
print(d2)

d3 = d2.copy()  # don't use d3=d2 as  any action on d3 will affect d2
del d3["Vanissa"]
print(d3)

d2.update({"Pheobe":"Coffee"}) # same as d2["Phoebe"]="Coffee"
print(d3)

print(d2.keys()) #dict_keys(['Mriganka', 'Partha', 'Ron', 'Mike', 'Rikky', 'Graham', 'Vanissa', 'Pheobe'])

print(d2.items()) # dict_items([('Mriganka', 'Roti'), ('Partha', 'Chicken'), ('Ron', 'Fish'), 
                  # ('Mike', 'Ice-Cream'), ('Rikky', {'A': 'Burger', 'B': 'Lolipop', 'C': 'Paneer'}), 
                  #('Graham', 'Rolls'), ('Vanissa', 'Kabab'), ('Pheobe', 'Coffee')])
            
"""





# Dictionary
"""  

D= {"Surrounding":"Ambience",
      "Dested thing":"Anathema",
      "Speed up":"Expedite",
      "Fear":"Dispel",
      "Gloomy":"Dismal",
      "Mistake":"Discrepancy",
      "Tired":"Effete",
      "Agriculture":"Husbandry",
      "Damage":"Impair",
      "Violate":"Infringe"
    }

print("Choose your word, you want to know meaning of :")
print(D.keys())

s=input()
n= D[s]
print("Meaning of ",s, "is", n )
"""











#Lecture 12
#set
"""
s= set()
print(type(s))

set_1= set([1,2,3,4])
print(set_1)
print(type(set_1))
"""


"""
list=(1,2,3,4,5,6)
set_from_list = set(list)
print(set_from_list)
print(type(set_from_list))
"""


"""
s=set()
s.add(1) #{1}
print(s)
s.add(1) #{1}; only retains unique values (different than list)
print(s)
s.add(2) #{1,2}
print(s)

s1= s.union({5,8,1}) #{1, 2, 5, 8}
print(s1)

s2= s1.intersection({5,6,7,8}) #{8,5}
print(s2)

s3= s1.difference(s2) #{1,2}
print(s3)

s4=s2.isdisjoint(s3)
print(s4)

print(max(s2))

s1.remove(1)
print(s1)
"""








#Lecture 13
#TfElse_ElseIf
"""
# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# Quiz
print("What is your age?")
age = int(input())
if age<18:
    print("You cannot drive")

elif age==18:
    print("We will think about you")

else:
    print("You can drive")
"""







#Lecture-14
#Faulty Calculator
"""
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
            #print(int(n1) * int(n2))

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
    if cal_again== "y" or "Y":
        calculate()
    elif cal_again=="n" or "N":
        print("Adios!!")
    else:
        again()   #or input()==""

calculate()
"""










#Lecture 15
#for loop


"""
list1= ["Apple", "Banana", "Coconut", "Dragon Fruit", "Egg Plant",
        "Fig", "Grapes", "Hazelnut", "I", "Jack Fruit", "kiwi",
        "Lemon", "Mango", "N", "Onion", "Plam", "Quin", "Radish",
        "strawberry", "Tomato", "U", "V", "Watermelon", "X", "Yam",
        "Zucchini"]

list2=list1.copy()
list2.insert(14,"Nectarine")
list2.remove("N")
list2.insert(20,"Ugly Fruit")
list2.remove("U")
list2.insert(21,"Victoria Palm")
list2.remove("V")
#print(list2)

for item in list2:
    print(item)
    






list1= [["Apple",0], ["Banana",1], ["Coconut",2], ["Dragon Fruit",3], ["Egg Plant",4]]

dict1 = dict(list1)
print(dict1)

for item, indexN in list1:               # Using List
        print(item, " index no. is ", indexN)

for item, indexN in dict1.items():           # Using Dictionary
        print(item," index no. is ", indexN)







#Check if the item is a number and print if it is greater than 5
items= [2,5,"Cats",23,21,"dogs", 1, 5, 91,"mouse", 32]

for item in items:
        if str(item).isnumeric() and item>=6 :
                print(item)

"""












# lecture 16
#While Loop
"""
i=0
while(i<45):
    print(i)
    i=i+1
    
    


while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
"""








#Lecture 17
#Guessing number game
