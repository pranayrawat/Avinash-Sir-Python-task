from datetime import date
t1 = (2014,7,2)
t2 = (2014,7,11)
first_date = date(t1[0],t1[1],t1[2])
second_date = date(t2[0],t2[1],t2[2])
print(f"{(second_date-first_date).days} days")