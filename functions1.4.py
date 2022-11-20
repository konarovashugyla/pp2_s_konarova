def filter_prime(l):
    new = []
    def is_primee(x):
        for i in range(2, x):
            if x%i==0:
                return False
        return True
    for element in l:
        if is_primee(int(element))==True:
            new.append(int(element))
    print(new)
            
filter_prime(input().split())