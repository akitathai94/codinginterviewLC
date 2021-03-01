"""
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
Write a function to return the count of such triplets.
"""
# Sample:
# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

class Solution():
    def triplet_with_smaller_sum(self, arr, target):
        # Infer algo/ data from characteristics problem? 
        # count of triplets that sum less than target value => two pointers with one tracking first triplet
        # Generate samples, get pattern of samples see how algo look like?
        # [-1, 4, 2, 1, 3] => sort => [-1, 1, 2, 3, 4] target 5  => [-1, 1, 4], [-1, 1, 3], [-1, 1, 2] => count = 3
        # From every substep, come back to step 1 to see if we can optimize from it.
        count = 0
        arr.sort()
        # Loop first element of triplet to last 2
        for i in range(len(arr) -2):
            count = self.find_smaller_sum(i+1, arr, target, count)
        # get the next index from first as left and last index in right
        # calc sum of triplet if less than target count += 1 and right -= 1 
        # until it reachs left < right
        # then increase left and reset right 
        # return count
        return count
    def find_smaller_sum(self, left, arr, target, count):
        curr_tuplet = arr[left -1]
        while left <= len(arr) - 2:
            right = len(arr) - 1
            while (left < right):
                calc_target = arr[left] + arr[right] + curr_tuplet
                if calc_target < target:
                    print([curr_tuplet, arr[left], arr[right]])
                    count += 1
                right -= 1
            left += 1
        return count
    def triplet_with_smaller_sum1(self, arr, target):
        arr.sort()
        count = 0
        for i in range(len(arr) -2):
            count += self.find_smaller_sum1(i, arr, target - arr[i])
        return count  
    def find_smaller_sum1(self, first, arr, target):
        count = 0
        left, right= arr[first], len(arr) - 1
        while left <right:
            if arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

arr = [-1, 4, 2, 1, 3] # [-1, 1, 2, 3, 4]
print(Solution().triplet_with_smaller_sum(arr, 5))
print(Solution().triplet_with_smaller_sum1(arr, 5))

# 4 [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


