def occurence_element(input_list):
    count_dict =dict()
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] =1
    return count_dict        


list =[11, 33 ,44, 11, 45, 33, 44, 11]
print(occurence_element(list))