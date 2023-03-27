d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
ascending = sorted(d)
descending = sorted(d,reverse=True)
asc = dict()
desc = dict()
for i in ascending:
    asc[i] = d[i]
    
for i in descending:
    desc[i] = d[i]
    
print(f"Ascending: {asc}")
print(f"Descending: {desc}")