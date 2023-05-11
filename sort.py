def sort_dictionary(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda x: x[1][1], reverse=True)
    sorted_list = [(name, phone, age) for name, (phone, age) in sorted_tuples]
    for name, phone, age in sorted_list:
      print(name, phone, age)
    return sorted_list
