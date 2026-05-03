class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        i = j = 0
        room = 0
        res = 0
        n = len(start)
        while i<n and j<n:
            if start[i]<end[j]:
                room+=1
                i+=1
                res = max(res,room)
            else:
                room-=1
                j+=1
            
        return res