class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        j = 0
        f = 0
        for i in range(len(nums)):
            if i>f:
                f = j
                end += 1
            j = max(j, nums[i]+i)
        return end