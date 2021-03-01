"""
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.
"""
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9 Explanation: Subarray with maximum sum is [5, 1, 3].

class Solution():
    def max_sub_arr_size_K(self, arr, k):
        # Look at characteristic of problem, combine them to find data structure / algo
        # Generate samples, what are the pattern of samples, what algo look like?
        # For every sub-step of algo, go back step 1 to see how can we optimize this step
        windowsStart, curr_max, curr_sum = 0, 0, 0
        # loop through the array with windowsEnd
        for windowsEnd in range(len(arr)):
            # add windowsEnd element to curr_sum
            curr_sum += arr[windowsEnd]
            # if windowsEnd - windowsStart >= k - 1
            if windowsEnd - windowsStart >= k - 1:
                # update curr_max
                curr_max =  max(curr_max, curr_sum)
                # subtract windowsStart, update windowsStart
                curr_sum -= arr[windowsStart]
                windowsStart += 1
        # return curr_max
        return curr_max

arr = [2, 3, 4, 1, 5]
print(Solution().max_sub_arr_size_K(arr, 2))

