"""
Given two lists of intervals, 
find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
"""
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

def merge(intervals_a, intervals_b):
    # From characteristic problem => Data/ Algo overlap problem:
    # Generate samples to see how the pattern look like? 
    # From every substep, come back to step 1 to see if we can optimize 
    # then for each interval check if we can find overlap 
    # apply intersect between both and append to intersect_ array 
    intersect_ = []
    a, b, start, end = 0, 0, 0, 1
    while a < len(intervals_a) and b < len(intervals_b):
        # check if a_overlap_b or b_overlap_a
        # a overlap b means: a[start] <= b[start] and a[end] >= b[end]
        a_overlap_b = intervals_a[a][start] >= intervals_b[b][start] and intervals_a[a][start] <= intervals_b[b][end]
        b_overlap_a = intervals_b[b][start] >= intervals_a[a][start] and intervals_b[b][start] <= intervals_a[a][end]
        # either one condition meet apply algorithm to update overlap intervals between two:
        if a_overlap_b or b_overlap_a:
            intersect_.append([max(intervals_a[a][start], intervals_b[b][start]), min(intervals_a[a][end], intervals_b[b][end])])
        # check with interval end smaller than go to next interval
        if intervals_a[a][end] < intervals_b[b][end]:
            a += 1
        else:
            b += 1
    return intersect_

def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()