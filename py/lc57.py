class Solution:
    def isoverlap (self,a,b):
        if a[1] < b[0] or b[1] < a[0]:
            return False
        return True

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            if self.isoverlap(ans[-1],intervals[i]):
                ans[-1][0] = min(intervals[i][0], ans[-1][0])
                ans[-1][1] = max(intervals[i][-1], ans[-1][-1])
            else:
                ans.append(intervals[i])
        return ans




t=Solution()
intervals =[[1,2],[4,5],[6,7],[8,10],[12,16]]
newInterval =[4,8]
ans=t.insert(intervals,newInterval)
print(ans)

'''思路和56题大致相似'''