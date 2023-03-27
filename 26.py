global dict1
dict1 = {'a':1,'b':2,'c':3,'d':4}

def add(k,v):
    dict1[k] = v
    print(dict1)
add("x",10)