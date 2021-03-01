"""
# Given a string with lowercase letters only, 
# if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.
"""
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

class Solution():
    def length_of_longest_substring(self, str, k):
        # Infer algo/ data from characteristics problem
        # Generate samples, get pattern of samples see how algo look like
        # "abbfebbee" => 6 "bbfebb"
        # From every substep, come back to step 1 to see if we can optimize from it. 
        max_length, max_repeat_char, windowsStart = 0, 0, 0
        freq_char = {}
        # Loop through the string with windowsEnd
        for windowsEnd in range(len(str)):
        # if not in dict create one 
            left_char = str[windowsEnd]
            freq_char[left_char] = freq_char.get(left_char, 0) + 1
        # update max_repeat_char
            max_repeat_char = max(max_repeat_char, freq_char[left_char])
        # check if (length - max_repeat > k) if yes then subtract from dict and move windowsStart
            if (windowsEnd - windowsStart + 1 - max_repeat_char > k):
                right_char = str[windowsStart]
                freq_char[right_char] -= 1
                windowsStart += 1
        # update max_length
            max_length = max(max_length, windowsEnd - windowsStart + 1) 
        return max_length

str = "abccde"
print(Solution().length_of_longest_substring(str, 1))
# 5 'bccbb'