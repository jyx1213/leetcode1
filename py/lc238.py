class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i] 
        return res

    
t=Solution()
nums = [-1,1,0,-3,3]
answer=t.productExceptSelf(nums)
print(answer)