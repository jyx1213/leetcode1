class Solution:
    def judge(self, a, b):
        if a[1] < b[0] or b[1] < a[0]:
            return False
        return True

    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = [intervals[0]]
        for idx in range(1,len(intervals)):
            if self.judge(ans[-1], intervals[idx]):
                ans[-1][0] = min(intervals[idx][0], ans[-1][0])
                ans[-1][1] = max(intervals[idx][-1], ans[-1][-1])
            else:
                ans.append(intervals[idx])
        return ans
    
'''解题思路通过比较当下两个集合是否有交集如果有交集就取并集如果没有就将集合添加在尾部'''