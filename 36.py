stud = {'Cierra Vega': 23, 'Alden Cantrell': 23,
        'Kierra Gentry': 23, 'Pierre Cox': 23}

#checking all are 23 value in stud dictionary
count = list(stud.values()).count(23)
print(f"Check all are 23 in the dictionary: {count == len(stud)}")

#checking all are 10 value in stud dictionary
count = list(stud.values()).count(10)
print(f"Check all are 10 in the dictionary: {count == len(stud)}")
