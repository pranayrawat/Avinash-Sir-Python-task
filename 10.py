def concat(*args):
    dict1 = dict()
    for i in args:
        dict1.update(i)
    print(dict1)
    
dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
concat(dic1,dic2,dic3)
# dic1.update(dic2)
# print(dic1)