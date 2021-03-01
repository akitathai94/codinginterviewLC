"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.
"""
# Input: [2, 4, 1, 4, 4]
# Output: 4
def find_duplicate(nums):
    # range from 1 to 'n'  => cyclic sort 
    # j = nums[i] - 1 // index of value
    # generate samples to see the pattern
    # [2,4,3,5,3,3,1] => [1,2,3,4,5,3,3] => 3
    # loop through with len nums
    # if num at index is not the same swap:
    # if the same and equal => return
    i = 0 
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            # check if the same and equal
        elif nums[i] == nums[j] and i != j:
            return nums[i]
        else:
            i += 1 
    return -1
print(find_duplicate([2,4,3,5,3,3,1]))