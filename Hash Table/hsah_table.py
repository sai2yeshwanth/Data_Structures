dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print(dict)
dict_1 = dict.copy()
print(dict_1)
del dict_1["Class"]
print(dict_1)
dict_1.clear()
print(dict_1)
