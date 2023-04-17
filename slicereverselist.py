def slice_reverse(input_list):
    chunks = 3
    length =len(input_list)
    chunks_size = int(length/chunks)

    start_index = 0
    end_index = chunks_size
    for i in range(chunks): 
        list_chucked = input_list[start_index:end_index]
        list_chucked.reverse()
        print(list_chucked)
        start_index = end_index
        end_index += chunks_size
        


    # list_1 = input_list[start_index : end_index] # 0 : 2
    # # print(list_1)
    # start_index = end_index
    # end_index = end_index + sub_list_length
    # list_2 = input_list[start_index : end_index] # 2 : 4

    # start_index = end_index
    # end_index = end_index + sub_list_length
    # list_3 = input_list[start_index : end_index] # 2 : 4

    # list_1.reverse()
    # list_2.reverse()
    # list_3.reverse()

    # print(list_1)
    # print(list_2)
    # print(list_3)

print(slice_reverse([2,4,5,6,5,4]))









    