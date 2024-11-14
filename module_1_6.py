my_dict = {"Vasy": 1967, "Koly": 1992, "Afony": 2017}
print("Dict:", my_dict)

print("Value1:", my_dict["Vasy"])
print("Value2:", my_dict.get("Vasy"))
print("No existing value:", my_dict.get("Dormidont"))

my_dict.update({"Ruslan" : 2010, "Ludmila" : 2015})
print("Modified dictionare:", my_dict)

refund = my_dict.pop("Ludmila")
print("Existing value:", refund)
print("Modified dictionare:", my_dict)

print("##################################################")
my_set = {1, 1, "w", "w", "ogogo", "ogogo"}
print("Set:", my_set)

my_set.add("Koly")
my_set.add((1,2,3))
print("Modified set1:", my_set)

my_set.discard('w')
print("Modified set2:", my_set)