"""
# Given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) 
# such that they add up to the given target. 
"""
# Samples
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

class Solution():
    def pair_with_targetsum(self, arr, sum):
        # Infer algo/ data from characteristics problem? find a pair in the array
        # Generate samples, get pattern of samples see how algo look like? 
        # [1, 6, 7, 8, 10], sum = 15 => [2, 3]
        # From every substep, come back to step 1 to see if we can optimize from it.?

        # Using two ptr, front and back.
        f, b = 0, len(arr) - 1
        # loop until it overlap, calculate sum of two indices 
        while f != b:
        # if found sum return two ptrs
            pair_sum = arr[f] + arr[b]
            if pair_sum == sum:
                return [f, b]
        # if sum > target => shift end ptr
            if pair_sum > sum:
                b -= 1
        # if sum < target ==> shift front ptr
            if pair_sum < sum:
                f += 1
        # return [-1, -1]
        return [-1, -1]

arr = [2,5,9,11]
print(Solution().pair_with_targetsum(arr, 11))
# [1, 3]