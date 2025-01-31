arr = [1, 2, 3, 4, 5, 6, 7]
# [7, 6, 5, 4, 3, 2, 1]
# Given an array and value k , Rotate an Array such that the Array will move k steps to the right



def rotate_array(nums, k):
    k = k % len(nums)
    print(k)

    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l , r = l + 1, r - 1

    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    l, r = k , len(nums) - 1
    print(k + 1)
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    
    return nums

print(rotate_array(arr, 3))

