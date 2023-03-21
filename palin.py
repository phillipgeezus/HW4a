def palindrome(list):
    if len(list) <= 1:
        return True

    if list[0] == list[-1]:
	return palindrome(list[1:-1])
    else:
	return False
		
