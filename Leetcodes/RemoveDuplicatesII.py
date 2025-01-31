arr = [1, 1, 1, 2, 2, 2, 3, 3]
arr = [1, 2, 3, 4, 4, 5]

#  Remove duplicates inplace such that any unique number appears only twice

def RemoveDuplicates(nums):
    l , r = 0 , 0

    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            count += 1
            r = r + 1
        for j in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    
    return l


print(RemoveDuplicates(arr))