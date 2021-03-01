"""
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, 
find the missing number.
"""
# Samples
# Input [4, 0, 3, 1]
# 2

def find_missing_number(nums):
    # Characteristic Problem: range 0 to 'n'. distinct number n out of n+1 number
    # [4,0,3,1] => missing 2 [0,1,3,4]
    # Do loop N to swap to its index, 
    # then loop back again to check if != index return that number
    i = 0
    while i  < len(nums):
        j = nums[i]
        if nums[i] != i and j < len(nums):
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    print(nums)
    for j in range(len(nums)):
        if nums[j] != j:
            return j
    return -1

print(find_missing_number([4,0,3,1]))