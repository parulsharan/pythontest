def set_intersection(set1,set2):
    output = set1.intersection(set2)
    print("output is: ",output)
    for item in output:
        set1.remove(item)
    return set1
set1 = {11,22,33,444,55,11,33} 
set2 = {22, 55, 44,23, 33}  
print(set_intersection(set1, set2)) 