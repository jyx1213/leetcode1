def findAnagrams(self, s: str, p: str) -> List[int]:
    slength,plength,list1=len(s),len(p),[]
    p_cnt = [0] * 26
    s_cnt = [0] * 26
    if slength<plength:
        return list1
    for i in range(plength):
        p_cnt[ord(p[i])-ord("a")]+=1
        s_cnt[ord(s[i])-ord("a")]+=1
    if p_cnt==s_cnt:
        list1.append(0)
    for i in range(plength,slength):
        s_cnt[ord(s[i-plength])-ord("a")]-=1
        s_cnt[ord(s[i])-ord("a")]+=1
        if p_cnt==s_cnt:
            list1.append(i-m+1)