class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #Add the new Interval
        for idx in range(len(intervals)):

            if intervals[idx][1] >= newInterval[0]:
                if intervals[idx][0] <= newInterval[1]:
                    intervals[idx][0] = min(intervals[idx][0], newInterval[0])
                    intervals[idx][1] = max(intervals[idx][1], newInterval[1])
                else:
                    intervals.insert(idx,newInterval)
                break
        else:
            intervals.append(newInterval)

        #Merge Intervals
        for idx in range(len(intervals)-1):

            while intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx][0] = min(intervals[idx][0], intervals[idx+1][0])
                intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                intervals.pop(idx+1)
                if idx >= len(intervals)-1:
                    break
            
            if idx >= len(intervals)-2:
                return intervals
        return intervals