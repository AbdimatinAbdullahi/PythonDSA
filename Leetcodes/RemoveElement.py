def RemoveElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = val
            i += 1
        else:
            continue
    return i

nums = [3, 2, 2, 3]
print(RemoveElement(nums, 3))