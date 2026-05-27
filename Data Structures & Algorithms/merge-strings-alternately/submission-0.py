class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        s=""
        while i<l1 and i<l2:
            s=s+word1[i]+word2[i]
            i+=1
        s+=word1[i:]
        s+=word2[i:]

        return s

            