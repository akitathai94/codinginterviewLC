# First sort by start time 
# if len < 2 return by 1 room
# if there is overlap check array queue increase room by 1 and append both end time to queue 
# if there next overlap check start time if <= end time in queue 
# then update end time with new end, otherwise increase another room.
# [[4,5][2,3][2,4][3,5]]
# [2,3][2,4][3,5][4,5]

from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end
def min_meeting_rooms(meetings):
    # if len(meetings) < 2:
    #     return 1
    # min_room = 1
    # # create heap for time_slot
    # time_slot = []
    # # sort array by start time
    # meetings.sort(key = lambda x: x.start)
    # # compare pair of room time 
    # for i in range(len(meetings) - 1):
    #     if (meetings[i].start <= meetings[i+1].start and meetings[i+1].start < meetings[i].end):
    #         if not time_slot:
    #             min_room += 1
    #             heappush(time_slot, meetings[i].end)
    #             heappush(time_slot, meetings[i+1].end)
    #         else:
    #             min_endtime = min(meetings[i].end, meetings[i+1].end)
    #             if min_endtime <= time_slot[0] and len(meetings) >= 2:
    #                 heappop(time_slot)
    #                 heappop(time_slot)
    #             heappush(time_slot, meetings[i].end)
    #             heappush(time_slot, meetings[i].end)
    meetings.sort(key = lambda x: x.start)
    min_room = 0
    time_slot = []
    for meeting in meetings:
        while len(time_slot) > 0 and meeting.start >= time_slot[0].end:
            heappop(time_slot)
        heappush(time_slot, meeting)
        min_room = max(min_room, len(time_slot))
    return min_room

    # conflict room condition: a over b : a.start <= b.start and b.start < a.end
def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    #[1,4][2,4][8,12]
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    #[2,4][6,7][8,12]
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    #[1,4][2,3][3,6]
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    # [2,3][2,4][3,5][4,5]
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5), Meeting(4,6)])))


main()