"""
Sort objects in-place on their creation O(n) and without any extra space. 
"""
# [3, 1, 5, 4, 2] => [1, 2, 3, 4, 5]

def cyclic_sort(nums):
    # if value is not at == index, swap value to that index value
    for i in range(len(nums)):
        j = nums[i] - 1
        if nums[i] != i+1:
            nums[j], nums[i] = nums[i], nums[j]
    return nums

print(cyclic_sort([3,1,5,4,2]))