"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
"""
# Samples Input 
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

from __future__ import print_function
class Interval:
    def __init__(self, start ,end):
        self.start = start
        self.end = end
    
    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end =' ')

def insert(intervals, new_interval):
    # Data Structure/ Algo from characteristic problem
    # Generate samples, look at the pattern samples, how it look likes?
    # [1, 5] [7,10] [12, 14]  add [8, 13] => [1,5] [7,14]
    # From every substep, go back to step 1 if we can optimize from there?
    start = new_interval.start
    end = new_interval.end
    merged = []
    i = 0
    # First loop through the list to append those interval that intervals.end < start
    while i < len(intervals) and intervals[i].end < start:
        merged.append(Interval(intervals[i].start, intervals[i].end))
        i += 1
    # Second loop will try to merge overlap intervals until we cant
    while i < len(intervals) and intervals[i].start <= end:
        start = min(start, intervals[i].start)
        end = max(end, intervals[i].end)
        i += 1
    merged.append(Interval(start, end))
    # inside we have to update front and end interval with new interval
    # c.start = min(start, intervals[i].start)
    # c.end = max(end, intervals[i].end)
    # append the rest of the intevals to the list
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged
def main():
    print("Merged intervals: ", end='')
    for i in insert([Interval(2, 4), Interval(5, 7), Interval(8, 12)], Interval(3, 6)):
        i.print_interval()
        print()
main()
# This way we not using any class object of interval
def insert1(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1
    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
    return merged

print(insert1([[1, 3], [5, 7], [8, 12]], [4, 10]))