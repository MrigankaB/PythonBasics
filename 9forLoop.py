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
    
"""



"""
list1= [["Apple",0], ["Banana",1], ["Coconut",2], ["Dragon Fruit",3], ["Egg Plant",4]]

dict1 = dict(list1)
print(dict1)

for item, indexN in list1:               # Using List
        print(item, " index no. is ", indexN)

for item, indexN in dict1.items():           # Using Dictionary
        print(item," index no. is ", indexN)
"""



#Check if the item is a number and print if it is greater than 5
items= [2,5,"Cats",23,21,"dogs", 1, 5, 91,"mouse", 32]

for item in items:
        if str(item).isnumeric() and item>=6 :
                print(item)




