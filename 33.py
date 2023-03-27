d = dict()
key = ['x','y','z']
t1 = list(range(11,20))
t2 = list(range(21,30))
t3 = list(range(31,40))
val = [t1,t2,t3]
for i,j in zip(key,val):
    d[i] = j
    
count = 1
print("i. First")
for i in d.items():
    print(f"{count}. {i[0]} has value {i[1]}")
    count+=1
#     print(f"{i} has value {j}")

count = 1
print("\nii. Second")
for i in d.keys():
    print(f"{count}. {d[i][4]}")
    count+=1