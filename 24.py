l1 = ['xyx','abc','ok','bob','eve']
count = 0
for i in l1:
    if len(i)>=2 and i[0] == i[-1]:
        count += 1
print(count)