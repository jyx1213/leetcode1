def lengthOfLongestSubstring(self, s: str) -> int:
    length = len(s)
    i=0
    flag=0
    tempstr=s
    tempmax=0
    if s=="":
        return 0
    while i < length:
        if  s.count(s[i])>1:
            flag=1
            tempstr=tempstr[:i]+tempstr[i+1:]
            sec=tempstr.find(s[i],i)
            tempmax=max(sec-i+1,tempmax)
            tempstr=s
        i+=1
    return tempmax
self=[]
s = "abcabcbb"
a=lengthOfLongestSubstring(self, s)
print(a)