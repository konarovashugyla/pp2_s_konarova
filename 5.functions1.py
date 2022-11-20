from itertools import permutations
def find_perms(x):
    perms = [''.join(p) for p in permutations(x)]
    return (perms)