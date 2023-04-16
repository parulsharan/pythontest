def list_operation(input_list):
    element = input_list.pop(4)
    input_list.insert(2,element)
    input_list.append(element)
    return input_list





sample_list = [34, 54, 67, 89, 11, 43, 94]
print(list_operation(sample_list))