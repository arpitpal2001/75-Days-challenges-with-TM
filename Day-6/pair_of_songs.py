class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        r = {}
        for i in time:
            if i%60==0 and 0 in r:
                res+=r[0]
            elif 60-(i%60) in r:
                res+=r[60-(i%60)]
            if i%60 in r:
                r[i%60]+=1
            else:
                r[i%60]=1
        return res