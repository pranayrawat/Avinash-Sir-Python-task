d1 = {'A': 1, 'B': 3, 'D': 2,'E':10}
d2 = {'A': 1, 'C': 2,'E':10}

for i in d1.items():
    if i in d2.items():
        print(f"{i[0]}:{i[1]} is present in both d1 and d2")
