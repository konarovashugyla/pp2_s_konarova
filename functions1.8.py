def spy_game(nums):
    if 0 in nums and 7 in nums :
        del nums[nums.index(0)]
        if 0 in nums:
            if nums.index(0)<nums.index(7):
                return True

    return False
'''
print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #-> False
'''
