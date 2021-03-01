"""
Given an array of intervals representing ‘N’ appointments, 
find out if a person can attend all the appointments.
"""
# Samples 
# Appointments[[6,7][2,4][8,12]] => [2,4][6,8][8,12]
# True
def can_attend_all_appointments(intervals):
    start, end = 0, 1
    intervals.sort(key = lambda x: x[start])
    # sort intervals in with start time
    # check if each interval is overlap: intervals[i+1][start] < intervals[i][end]
    # since appt can be right after the other so we cannot use ==
    for i in range(len(intervals) - 1):
        if intervals[i+1][start] < intervals[i][end]:
            return False
    return True
def return_conflict_intervals(intervals):
    res = []
    start, end = 0, 1
    intervals.sort(key = lambda x: x[start])
    for i in range(len(intervals) - 1):
        for j in range(i+1, len(intervals)):
            if intervals[j][start] < intervals[i][end]:
                res.append((intervals[i], intervals[j]))
    for i in range(len(res)):
        print("[" + str(res[i][0][start]) + "," + str(res[i][0][end]) + "]" + " and " + "[" + str(res[i][1][start]) + "," + str(res[i][1][end]) + "]" + " conflict.")

def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))
    return_conflict_intervals([[4,5], [2,3], [3,6], [5,7], [7,8]])

main()