

class Solution:

    @staticmethod
    def longest_palindromic(self,s: str) -> str:
        res= ""
        reslen=0
        for i in range(len(s)):
            #odd 
            l=i 
            r=i
            while (l >=0 and r < len(s) and s[l] == s[r]):
                if (r - l +1) > rerslen:
                    res = s[l:r+1]
                    reslen = r -1 + 1
                    l -=1
                    r +=1
            #even 
            l=i 
            r=i+1
            while (l >=0 and r < len(s) and s[l] == s[r]):
                if (r - l +1) > rerslen:
                    res = s[l:r+1]
                    reslen = r -1 + 1
                    l -=1
                    r +=1
            return res

    pass