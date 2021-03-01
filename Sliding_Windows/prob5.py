'''
 Given an array of characters where each character represents a fruit tree, 
 you are given two baskets, and your goal is to put maximum number of fruits in each basket. 
 The only restriction is that each basket can have only one type of fruit.
 You can start with any tree, but you can’t skip a tree once you have started. 
 You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
'''
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3 
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

class Solution():
    def fruits_into_baskets(self, fruits):
        # Algo/ Data from Problem Characteristic:
        #  ( max number of fruit => max length), 
        # (cannot skip a tree => contigous subarray)
        # distinct= only 2 types  ==> SLIDING WINDOWS with distinct of 2 return max length
        # Generate samples, how pattern samples, algo look like
        # [A, B, A, B, B, C, D] => 5 [A, B, A, B, B]
        # For every sub-step, go back to step 1 to see if we can optimize O(N)
        windowsStart, length, res = 0, 0, -1
        freq_fruits = {}
        # for loop through array fruits
        for _, right_fruit in enumerate(fruits):
        # update dict_fruit 
            freq_fruits[right_fruit] = freq_fruits.get(right_fruit, 0) + 1
        # add length
            length += 1
        # while loop check if distinct > 2
            while len(freq_fruits) > 2:
        # subtract dict_fruit from fruits[windowsStart] ( if == 1 del that key)
                left_fruit = fruits[windowsStart]
                if freq_fruits[left_fruit] == 1:
                    del freq_fruits[left_fruit] 
                else:
                    freq_fruits[left_fruit] -= 1
        # subtract length
                length -= 1
        # update res with max length and res
            res = max(res, length)
        return res

# Test case
fruits = ['A', 'B', 'C', 'B', 'B', 'C']
print(Solution().fruits_into_baskets(fruits))
# 3 [C, A, C]