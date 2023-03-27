def check(str1):
    values = dict1.values()
    if str1 in values:
        print(f"'{str1}' value is in dictionary")
    else:
        print("Not present")
        
global dict1
dict1 = {1:"A",2:"B",3:"C",4:"D"}
check("A")