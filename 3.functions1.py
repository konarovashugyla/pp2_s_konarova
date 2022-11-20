def above_55(l):
    movies= []
    for d in l:
        if d['imdb']>5.5 :
            movies.append(d['name'])
    return movies
   