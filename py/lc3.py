def longestConsecutive(nums):
    num_set=set(nums)
    max1=0
    for num in nums:
        if (num - 1) not in num_set:
            j=1
            while (num+1) in num_set:
                j=j+1
                num=num+1
            res = max(max1, j)
    return res

nums =[100,4,200,1,3,2]
a=longestConsecutive(nums)
print(a)