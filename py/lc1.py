
def twoSum(self, nums, target):
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if (nums[i]+nums[j])==target:
                self=[i,j]
                return self
            j=j+1
        i=i+1
    
nums =[3,2,4]
target = 6
self = []
self=twoSum(self, nums, target)
print(self)

