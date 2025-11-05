def find(str, ch, start=0, end=0):
    end = len(str)
    index = start
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1



#at beginning of function, use len() of string to add value to end parameter