"""
Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.
"""
# Sample 
# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
from collections import deque
class Solution():
    def find_subarrays(self, arr, target):
        # Infer algo/ data from characteristics problem? 
        # two pointers for left and right moving, and using sliding windows to keep tracking of products (subarray)
        # Generate samples, get pattern of samples see how algo look like?
        # [2, 5, 1 , 4, 6, 9] target = 12 => [2][5][2,5][1][5,1][2,5,1][4][1,4][6][9]
        # From every substep, come back to step 1 to see if we can optimize from it.

        # create two pointers left, right:
        left = 0
        res = []
        product = 1
        # start loop right pointer:
        for right in range(len(arr)):
        # calc product, check if current windows(left- right) 
        # is not over target and left still within arr index:
            product *= arr[right]
            while(product >= target and left < len(arr)):
                product /= arr[left]
                left += 1
        # otherwise / by left element and slide left ptr forward
        # initialize queue
            windows_queue = deque()
        # loop from right to left ptr and add to left queue
            for i in range(right, left - 1, -1):
                windows_queue.appendleft(arr[i])
                res.append(list(windows_queue))
        # then add add element to res list 
        # return res 
        return res


arr = [2, 5, 1 , 4, 6, 9]
print(Solution().find_subarrays(arr, 12))
