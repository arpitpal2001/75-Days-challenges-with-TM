class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n<2):
            return 0
        st = prices[0]
        mp=[]
        p = 0
        for i in range(0,n):
            if (prices[i]-st>p):
                p = prices[i]-st
            if (prices[i]<st):
                st = prices[i]
            mp.append(p)
        
        p = 0
        ed = prices[-1]
        for i in range(n-2,-1,-1):
            if (ed - prices[i] + mp[i] > p):
                p = ed - prices[i] + mp[i]
            if (prices[i]>ed):
                ed = prices[i]
        return p