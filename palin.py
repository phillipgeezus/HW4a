def palindrome(input_list):
    list_length = len(input_list)
    for i in range(list_length//2):
        if input_list[i] != input_list[list_length - i - 1]:
            return False
    return True
#def palindrome(list):
    #if len(list) <= 1:
        #return True
    #if list[0] == list[-1]:
	#return palindrome(list[1:-1])
    #else:
	#return False
