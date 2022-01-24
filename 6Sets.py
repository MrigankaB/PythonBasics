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