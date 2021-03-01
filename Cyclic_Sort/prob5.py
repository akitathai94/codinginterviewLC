"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.
"""
# Input [3,4,4,5,5]
# Output [4,5]

def find_all_duplicates(nums):
    # unsort array n number from 1 to 'n' => cyclic sort
    # Generate samples [3, 4, 4, 5, 5] => [5, 4, 3, 4, 5] => [5, 4]
    # if nums[i] != nums[j] swap
    # else if == and i != j append res
    # else i += 1
    i = 0
    res = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        elif nums[i] == nums[j] and i != j:
            res.append(nums[i])
            i += 1
        else:
            i += 1
    return res

print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))