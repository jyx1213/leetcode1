def threeSum(self, nums):
    i=0
    m=0
    j=0
    k=0
    self=[]
    temp=[]
    b=[]
    while j<len(nums):
        while i<len(nums):
            while k<len(nums):
                if ((nums[i]+nums[j]+nums[k])==0)and(i!=j)and(j!=k)and(i!=k):
                    b=sorted([nums[i],nums[j],nums[k]])
                    if b not in temp:
                        temp.append(sorted([nums[i],nums[j],nums[k]]))
                        self.append([nums[i],nums[j],nums[k]])
                        print(m)
                        m=m+1
                k=k+1
            i=i+1
            k=0
        j=j+1
        i=0
    return self
'''    i=len(temp)
    while i>0:
        j=i-1
        while j>=0:
            if temp[j]==temp[i]:
                del self[j]
            j=j-1
        i=i-1'''

nums = [-1,0,1,2,-1,-4]
self=[]
self = threeSum(self,nums)
print(self)