def found_set(set1, set2):

    if  set1.issubset(set2):
        print("set1 is subset.")
        set1.clear()
    else:
        print("set1 is superset of set2 ")    

            
     
set1 ={11,22}
set2 ={33,11,55,22,11,34}
print(found_set(set1,set2))
