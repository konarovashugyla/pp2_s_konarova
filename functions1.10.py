def unique(l):
    new_list= []
    for element in l:
        if element not in new_list:
            new_list.append(element)
    return new_list
