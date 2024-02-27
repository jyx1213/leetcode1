class Solution:
    def threeSumClosest(self,nums: list[int], target: int) -> int:
        nums.sort()
        res,k,num_difference,mindifference=0,0,100000,100000
        for k in range(len(nums)-2):
            i,j= k+1,len(nums)-1
            while i<j:
                res=nums[k]+nums[i]+nums[j]
                num_difference=target-res
                if (abs(mindifference)>abs(num_difference)):
                    mindifference=num_difference
                if target>res:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif target<res:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    return target
        return target-mindifference

t= Solution()
nums =[-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]
target = -14
print(t.threeSumClosest(nums,target))