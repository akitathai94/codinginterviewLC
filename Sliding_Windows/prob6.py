"""
Given a string, find the length of the longest substring, which has no repeating characters.
"""
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

class Solution():
    def non_repeat_substring(self, str):
        # Data structure/ ALgo that match characteristic of the problem? 
        # "Length of longest substring" condition no repeating char ==> Sliding Windows
        # Generates samples, what algo look like ? samples pattern
        # ? "aabddefg" => 4 "defg", "bacade" => 4 "cade" => cannot skip windowsStart
        # For every substep, go to step 1 to see if it can be optimized?

        freq_str = {}
        windowsStart, res = 0, 0 
        # loop over str with windowsEnd to len(str)
        for windowsEnd,ch in enumerate(str):
        # else while pop windowsStart from freq_char, increase windowsStart, update length
        # update freq, add length with windowsEnd value
        # update res with max length
            if freq_str.get(ch):
                while freq_str.get(ch):
                    del_str = str[windowsStart]
                    del freq_str[del_str]
                    # length -= 1
                    windowsStart += 1
        # check if windowsEnd not in freq_char if no update freq, add length
            freq_str[ch] = 1
            # length += 1
            res = max(res, windowsEnd - windowsStart + 1)
        return res
    # Other method, using dict to keep track index of the last right char if windowsStart already over then keep windowsStart
    def non_repeat_substring1(self, str):
        char_index_map = {}
        windowsStart, max_length = 0, 0
        for windowsEnd in range(len(str)):
            right_char = str[windowsEnd]
            if right_char in char_index_map:
                windowsStart = max(windowsStart , char_index_map[right_char] + 1)
            char_index_map[right_char] = windowsEnd
            max_length = max(max_length, windowsEnd - windowsStart + 1)

        return max_length


str = "abccde"
print(Solution().non_repeat_substring(str))

print(Solution().non_repeat_substring1(str))
# 3 "abc"