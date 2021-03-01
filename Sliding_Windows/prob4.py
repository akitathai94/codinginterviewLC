"""
Given a string, 
find the length of the longest substring in it with no more than K distinct characters.
"""
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

class Solution():
    def longest_substring_with_k_distinct(self, str, k):
        # Get data structure / algo from characteristic of problem: => 'length of longest substring'-> condition K distinct char
        # Get samples, 'leetcode' k = 3 => leet = 4 
        # Optimize for each substep from 1: 
        char_dict = {}
        res = -1
        length, windowsStart, = 0, 0 
        # loop through the string:
        for _,ch in enumerate(str):
        # check char if it exists in dict => add to dict
            char_dict[ch] = char_dict.get(ch, 0) + 1
        # increase length
            length += 1
        # keep sliding while len(dict) >= K:
            while len(char_dict) > k:
        # subtract from dict the value str[windowsStart] (if == 1 del dict and update distinct)
                if char_dict[str[windowsStart]] == 1:
                    del char_dict[str[windowsStart]]
                else:
                    char_dict[str[windowsStart]] -= 1
        # subtract length, slide windowsStart
                length -= 1
                windowsStart += 1
        # then update length after loop 
            res = max(res, length)
        return res

str = 'leetcode'
print(Solution().longest_substring_with_k_distinct(str, 3))
# 4 araa