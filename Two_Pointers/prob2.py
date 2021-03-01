"""
# Problem Statement 
# #Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; 
# after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
"""
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
class Solution():
    def remove_duplicates(self, arr):
        # Infer algo/ data from characteristics problem?  Get set of items that not duplicates => two pointers
        # Generate samples, get pattern of samples see how algo look like?
        # [1,2,2,4,4,7,9,10] ==> [1,2,4,7,9,10]
        # From every substep, come back to step 1 to see if we can optimize from it.?
        next_ptr, non_repeat_ptr = 1, 0
        # Loop through the arr:
        while next_ptr <= len(arr) - 1:
        # check if next is not the same as prev, then increase non_repeat
            if arr[next_ptr] != arr[next_ptr - 1]:
                non_repeat_ptr += 1
        # if non-repeat prev is not the same as next_ptr, then update next-non-repeat to be next-ptr 
                if arr[non_repeat_ptr - 1] != arr[next_ptr]:
                    arr[non_repeat_ptr] = arr[next_ptr]
        # move non-repeat ptr
        # move next ptr
            next_ptr += 1
        return non_repeat_ptr + 1

arr = [2, 3, 3, 3, 6, 9, 9]

print(Solution().remove_duplicates(arr))
# 4 [2,3,6,9]