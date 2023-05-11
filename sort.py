def sort_dictionary(input_dict):
    sorted_dict = sorted(input_dict.items(), key=lambda x: x[1][1])
    result = [(name, phone_num) for name, (phone_num, _) in sorted_dict]   
    return result
  
