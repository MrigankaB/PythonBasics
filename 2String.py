# Lecture 9
#String Slicing

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



# Important Functions on String

print(mystr.isalnum()) # Returns False ; Not alpha Because of spaces

print(mystr.isalpha()) # False ;Not alpha Because of spaces

print(mystr.endswith("doing")) #O: True

print(mystr.count("H")) # 2

print(mystr.capitalize()) #capitalize first letter

print(mystr.find("How")) # 5

print(mystr.lower()) # hey! how you doing

print(mystr.upper()) # HEY! HOW YOU DOING

print(mystr.replace("!",",")) # Hey, How you doing

