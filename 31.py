students = {'Aex':{'class':'V', 'rolld_id':2},'Puja':{'class':'V','roll_id':3}}
count = 1
for i,j in students.items():
    print(count,i)
    for x,y in j.items():
        count+=1
        print(f"{count} {x}:{y}")
    count+=1