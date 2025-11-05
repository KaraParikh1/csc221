def find(str, ch, start=0, end=0.5):
    if type(end) == float:
        end = len(str)
    else:
        pass
    index = start
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1

print(find("worddddd", "d"))