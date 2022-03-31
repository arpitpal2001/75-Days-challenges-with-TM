class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target+1)]
        
        for i in candidates:
            for j in range(1, target+1):
                if j<i:
                    continue
                if j==i:
                    dp[j].append([i])
                else:
                    for k in dp[j-i]:
                        dp[j].append(k+[i])
        return dp[target]