# Lecture 10
# List - mutable

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

