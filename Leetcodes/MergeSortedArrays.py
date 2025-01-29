def Merge(nums1, m, nums2, n):
    i = m - 1 # valid pointers in nums2
    j = n - 1 # Valid pointers in nums2
    k = m + n - 1 # Size of new nums1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

nums1 =[1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

print(Merge(nums1, 3, nums2, 3))
