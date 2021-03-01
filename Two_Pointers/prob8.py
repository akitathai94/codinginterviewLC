"""
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.
"""
# Samples
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]
class Solution():
    def dutch_flag_sort(self, arr):
        # Infer algo/ data from characteristics problem? 
        # two pointers high and low, after low is 0 before high is 2 and between is 1
        # Generate samples, get pattern of samples see how algo look like?
        # [1, 0, 2, 2, 0, 1, 1] => [0, 0, 1, 1, 1, 2, 2] lo = 2, hi = 4, i = 5
        # From every substep, come back to step 1 to see if we can optimize from it.

        # assign low at 0 high at len(arr) - 1
        lo, hi = 0, len(arr) - 1
        i = 0
        # iterate through high
        while i <= hi:
        # if arr[i] == 0 swap with arr[low] increase low
            if arr[i] == 0:
                arr[i], arr[lo] = arr[lo], arr[i]
                lo += 1
        # elif arr[i] == 1 increase i 
            elif arr[i] == 1:
                i += 1
            else:
                arr[i], arr[hi] = arr[hi], arr[i]
                hi -= 1
        # else arr[i] == 2 swap with arr[high] decrease high
        return arr

arr = [1, 2, 2, 0, 0, 2]
print(Solution().dutch_flag_sort(arr))
# [0, 0, 1, 1, 2]
