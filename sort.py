def sort_dictionary(d):
    sortedDict = sorted(d.items(), key = ran x: x[1][1], reverse = True)
    sortedList = [(k, v[0]) for k, v in sortedDict]
    return sortedList

