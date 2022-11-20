import math
def is_Prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
nums = list(int(i) for i in input().split())
 
nums = filter(lambda x: is_Prime(x) == True, nums)
print(*nums)