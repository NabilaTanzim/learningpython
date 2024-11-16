set = {"Aam", "Jaam", "Kathal"}
print(set)
print(type(set))
print(len(set))

for i in set:
    print(i)

set.add("Kola")
print(set)

set2 = {1, 2, 3}
set.update(set2)
print(set)

set.remove("Kola")
print(set)

set.discard("Lichu")
print(set)

set.pop()
print(set)

set.clear()
print(set)

set3 = {5, 6, 7}
set4 = {8, 9, 0}
set5 = set3.union(set4)
print(set5)

fruits = {"Aam", "Jaam", "Kathal"}
if "Jaam" in fruits:
    print("Yes Jaam is in")
else:
    print("No Jaam")



