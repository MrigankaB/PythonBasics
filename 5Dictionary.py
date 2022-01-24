#Dictionary - mutable
"""
d1 = {}
print(type(d1))

d2 = {"Mriganka": "Roti",
      "Partha": "Chicken",
      "Ron": "Fish",
      "Mike": "Ice-Cream",
      "Rikky": {"A": "Burger", "B": "Lolipop", "C": "Paneer"}}
d2["Graham"] = "Rolls"
d2["Vanissa"] = "Kabab"
d2["Officer"] = "Bread"

print(d2)

print(d2["Partha"])
print(d2["Vanissa"])

del d2["Officer"]
print(d2)

d3 = d2.copy()  # don't use d3=d2 as  any action on d3 will affect d2
del d3["Vanissa"]
print(d3)

d2.update({"Pheobe": "Coffee"})  # same as d2["Phoebe"]="Coffee"
print(d3)

print(d2.keys())  # dict_keys(['Mriganka', 'Partha', 'Ron', 'Mike', 'Rikky', 'Graham', 'Vanissa', 'Pheobe'])

print(d2.items())  # dict_items([('Mriganka', 'Roti'), ('Partha', 'Chicken'), ('Ron', 'Fish'),
# ('Mike', 'Ice-Cream'), ('Rikky', {'A': 'Burger', 'B': 'Lolipop', 'C': 'Paneer'}),
# ('Graham', 'Rolls'), ('Vanissa', 'Kabab'), ('Pheobe', 'Coffee')])

"""



#Dictionary which takes user input

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