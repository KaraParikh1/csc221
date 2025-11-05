def find(str, ch, start=0):
    index = start
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

#add parameter in parameter list


#at beginning of function, use len() of string to add value to end parameter