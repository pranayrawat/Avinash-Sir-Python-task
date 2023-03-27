dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict2 = dict1.copy()
for i in dict1.keys():
    if dict1[i] is None:
        dict2.pop(i)
print(dict2)