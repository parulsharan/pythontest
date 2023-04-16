#Enter Python code here and hit the Run button.
#// implementation
def even_odd_check(l1,l2):
    l3 =[]
    for index in range(1,len(l1),2):
       # print(l1[index])
        l3.append(l1[index])  
    for index in range(0,len(l2),2):
        l3.append(l2[index])

    return l3


#// test cases
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print(even_odd_check(l1, l2))