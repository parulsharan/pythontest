def list_turn_set(list1, list2):
    output = zip(list1, list2)
    output_set = set(output)
    return output_set

l1 =[2,3,4,5,6]
l2 =[4,6,8,10,12]
print(list_turn_set(l1, l2))    