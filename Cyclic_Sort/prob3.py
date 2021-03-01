"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. 
Find all those missing numbers.
"""
# Inputs 
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7

def find_missing_number(nums):
    res = []
    i = 0
    # step 1: Cyclic Sort, range from 1 to 'n', duplicate will be at the wrong index add index to res list
    while i < len(nums):
        j = nums[i]
        if j <= len(nums) and j != nums[j - 1]:
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        else:
            i += 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i+1)
    return res

print(find_missing_number([2, 3, 2, 1]))
