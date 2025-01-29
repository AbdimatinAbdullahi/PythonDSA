def RemoveDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
    

nums = [1, 2, 2, 4, 4, 5, 6, 7]
print(RemoveDuplicates(nums))