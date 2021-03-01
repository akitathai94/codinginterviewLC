"""
Problem Statement
Given a sorted array, 
create a new array containing squares of all the numbers of the input array in the sorted order.
"""
# Sample Output
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

class Solution():
    def make_squares(self, arr):
        # Infer algo/ data from characteristics problem? create new array that squares of inputs in sorted order
        # Generate samples, get pattern of samples see how algo look like?
        # [-2, -1, 0, 2, 3] => [0, 1, 4, 4, 9]
        # From every substep, come back to step 1 to see if we can optimize from it.?
        # Create two pointer from both ends 
        # iterate through array with two pointer square and compare, 
        # higher will be put in the mostright ptr of the new arr
        res = [0 for i in range(len(arr))]
        res_ptr = len(arr) - 1
        left, right = 0, len(arr) - 1
        while left < right:
            square_left = arr[left] * arr[left]
            square_right = arr[right] * arr[right]
            if square_left >= square_right:
                res[res_ptr] = square_left
                left += 1
            else:
                res[res_ptr] = square_right
                right -= 1
            res_ptr -= 1
        return res


arr = [-3, -1, 0, 1, 2]
print(Solution().make_squares(arr))
# [0, 1, 4, 4, 9]