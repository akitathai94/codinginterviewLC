"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""
# Input Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

class Solution():
    def find_avg_of_sub_arr(self, arr, k):
        #1 Characteristic of the problem, can I combine these characteristic to math a known data structure/ algo
        #2 Generate samples? Pattern samples? What the algo look like?
        #3 Look at every substep of algo, look at step 1 and see how can I optimize this 
        # Time complexity: O(N)
        windowsStart, curr_sum = 0, 0
        res = []
        # Loop through the arr with windowsEnd ptr:
        for windowsEnd in range(len(arr)):
            # add element at windowsEnd to the sum
            curr_sum += arr[windowsEnd]
            # if size of subarray >= k - 1  then calculate avg, subtract element from the head, move head forward
            if (windowsEnd - windowsStart) >= k - 1:
                res.append(curr_sum / k)
                curr_sum -= arr[windowsStart]
                windowsStart += 1
        # return sub - array
        return res



arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(Solution().find_avg_of_sub_arr(arr, 5))
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]
