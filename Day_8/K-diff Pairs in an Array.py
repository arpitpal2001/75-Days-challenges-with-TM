class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        r = 0
        if k==0:
            for i in c.values():
                r+=i>1
        else:
            for j in c:
                r+=k+j in c
        return r