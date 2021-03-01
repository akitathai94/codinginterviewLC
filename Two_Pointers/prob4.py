"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""
# Sample Outputs
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero. 

class Solution():
    def search_triplets(self ,arr):
        # Infer algo/ data from characteristics problem? Find unique triplets that sum is zero.  => two pointers
        # Generate samples, get pattern of samples see how algo look like? 
        # [-3, -5, -7, 0, 1, 4, 5, 2, 3] => [[-3, 0, 3], [-5, 0, 5], [-7, 5, 2], [-5, 1, 4]]
        # [-7, -5, -3, 0, 1, 2, 3, 4, 5]
        # From every substep, come back to step 1 to see if we can optimize from it.?
        sorted_arr = sorted(arr)
        # no neg num so does not exist triplets that sum is zero
        if sorted_arr[0] >= 0:
            return [-1, -1, -1]
        neg_ptr = 0 
        res = [] 
        while sorted_arr[neg_ptr] < 0:
            if neg_ptr > 0 and sorted_arr[neg_ptr] == sorted_arr[neg_ptr - 1]:
                pass
            else:
                self.findSum(res, neg_ptr, sorted_arr)
            neg_ptr += 1
        # First sort the array so we can have neg pos seperated
        # negative num will be sum of the other two. we first pick neg 
        # then find that sum by solving another small two pointers
        return res
    def findSum(self, res, neg_index, arr):
        left, right = neg_index + 1, len(arr) - 1
        target_sum = - arr[neg_index]
        while left < right:
            if (arr[left] + arr[right] == target_sum) and (arr[left - 1] != arr[left]):
                res.append([arr[neg_index], arr[left], arr[right]])
            if arr[left] + arr[right] > target_sum:
                right -= 1
            else:
                left += 1
    
            



arr = [-3, 0, 1, 2, -1, 1, -2] # [-3, -2, -1, 0, 1, 1, 2]
print(Solution().search_triplets(arr))
# [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]