class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dup1={}
        dup2={}
        for i in range(len(s)):
            dup1[s[i]]=dup1.get(s[i],0)+1
        for i in range(len(t)):
            dup2[t[i]]=dup2.get(t[i],0)+1
        if dup1==dup2:
            return True
        return False        
       