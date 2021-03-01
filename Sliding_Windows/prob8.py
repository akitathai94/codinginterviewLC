"""
Problem Statement
# Given an array containing 0s and 1s, 
# if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.
"""
# Sample 
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

class Solution():
    def length_of_longest_substring(self, arr, k):
        # Infer algo/ data from characteristics problem  longest substring => Sliding Windows
        # Generate samples, get pattern of samples see how algo look like
        # [1, 0, 0, 1, 1], k = 2 => 5 
        # From every substep, come back to step 1 to see if we can optimize from it. 
        windowsStart, max_length, max_repeat_one = 0, 0, 0
        freq_char = {}
        # Loop through str with windowsEnd
        for windowsEnd in range(len(arr)):
        # update dict with windowsEnd element
            right_char = arr[windowsEnd]
            freq_char[right_char] = freq_char.get(right_char, 0) + 1
        # max_repeat_one = max(max_repeat_one, dict[1])
            max_repeat_one = max(max_repeat_one, freq_char.get(right_char))
        # if (length - repeat_one > k):
            if (windowsEnd - windowsStart + 1 - max_repeat_one > k):
                left_char = arr[windowsStart]
                freq_char[left_char] -= 1
                windowsStart += 1
        #   subtract dict from windowsStart and increase windowsStart
        # max_length = max(max_length, length)
            max_length = max(max_length, windowsEnd - windowsStart + 1)
        return max_length

arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
print(Solution().length_of_longest_substring(arr, 3))

