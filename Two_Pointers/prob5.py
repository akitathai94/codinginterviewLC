"""
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.
"""
# Sample output:
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
import math
class Solution():
    def triplet_sum_close_to_target(self, arr, target_sum):
        # Infer algo/ data from characteristics problem? find triplet in the array with sum closest to the target => two pointers
        # Generate samples, get pattern of samples see how algo look like? 
        # [-1, 0, 3, 4 ,-2], target = 1  => 0 because [-1, -2, 3]
        # From every substep, come back to step 1 to see if we can optimize from it.?
        # sort array, pick one to the left and only update res if target_diff is smallest
        arr.sort()
        res = [0, math.inf]
        for i in range(len(arr) -2):
            # call find_min_Sum()
            res = self.find_min_Sum(i + 1, res, arr, target_sum)
        return res[0]

    def find_min_Sum(self, left, res, arr, target_sum):
        curr_small = arr[left - 1]
        right = len(arr) - 1
        final_sum = 0
        while left < right:
            final_sum = arr[left] + arr[right] + curr_small
            if final_sum == target_sum:
                return [final_sum, abs(target_sum - final_sum)]
            elif final_sum > target_sum:
                right -= 1
            else:
                left += 1
        if abs(res[1]) > abs(target_sum - final_sum):
            res = [final_sum, abs(target_sum - final_sum)]
        return res

arr = [-2, 0, 1, 2] # [0, 1, 1, 1]
print(Solution().triplet_sum_close_to_target(arr, 2))
