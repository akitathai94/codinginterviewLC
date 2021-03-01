"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
"""
# Sample input
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
from __future__ import print_function
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end=' ')

def merge(intervals):
    res = []
    # Data structure/ Algo = Merge Interval
    # Generate samples: [[1,4], [2,5], [7,9]]
    # In every substep, go back to step 1 to see if we can optimize it. 
    # sort array with interval.start so interval in right order. 
    intervals.sort(key = lambda x: x.start)
    # if only one interval => print interval
    if len(intervals) < 2:
        return intervals
    # get curr_interval = intervals[0]
    curr_interval = intervals[0]
    for i in range(1, len(intervals)):
        if curr_interval.end >= intervals[i].start:
            curr_interval.end = max(curr_interval.end, intervals[i].end)
        else:
            res.append(Interval(curr_interval.start, curr_interval.end))
            curr_interval = intervals[i]
    res.append(Interval(curr_interval.start,curr_interval.end))
    # a, b interval => a overlap b completely, a overlap b and b end after a, 
    # if curr.end >= interval.start => curr.end = interval.end
    # else append to res list and update curr as next interval
    # append last interval in curr to res after break while loop
    return res

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
        print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
        print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
        print()

main()
