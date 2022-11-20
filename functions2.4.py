def average_in_list(l):
    s= 0
    for d in l:
        s+= d['imdb']
    return s/len(l)
        
        