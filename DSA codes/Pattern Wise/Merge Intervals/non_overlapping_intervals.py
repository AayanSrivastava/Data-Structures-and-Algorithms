def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    
    count = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            # overlap → remove this interval
            count += 1
        else:
            # no overlap → keep it
            prev_end = intervals[i][1]
    
    return count

# 2nd
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    
    prev_end = float('-inf')
    keep = 0
    
    for start, end in intervals:
        if start >= prev_end:
            keep += 1
            prev_end = end
    
    return len(intervals) - keep