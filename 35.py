stud = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9,65),
        'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

ans = dict()
for i,j in stud.items():
    if j[0] >= 6 and j[1] >= 70:
        ans[i] = j

print(ans)