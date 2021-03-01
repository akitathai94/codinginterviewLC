"""
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.
"""
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
import math
class Solution():
    def smallest_arr_with_given_sum(self, S, arr):
        # Find characteristic of the problem: 'find length smallest contiguous subarray' condition sum >= 'given S', return 0 if not exists => sliding windows with S is condition of sliding
        # Generate samples, look at the pattern of samples, [2, 1, 5, 2, 3, ,2] S =4 => return 0
        windowsStart, curr_sum, min_size = 0, 0, math.inf
        # loop through array with windowsEnd ptr
        for windowsEnd in range(len(arr)):
            # add element in windowsEnd to curr_sum 
            curr_sum += arr[windowsEnd]
            # check while curr_sum >= S --> update size with min of min_size and (
        # windowsStart - windowsEnd + 1 -> subtract windowsStart element and slide windowsStart forward
            while curr_sum >= S:
                # curr_arr = [arr[i] for i in range(windowsStart, windowsEnd + 1)]
                # print(curr_arr)
                min_size = min(min_size, (windowsEnd - windowsStart + 1))
                curr_sum -= arr[windowsStart]
                windowsStart += 1
        # if not exist subarray return 0
        if min_size == math.inf:
            return 0
        # return min_size
        return min_size




# Test case
arr = [2, 1, 5, 2, 3, 2]
print(Solution().smallest_arr_with_given_sum(9, arr))