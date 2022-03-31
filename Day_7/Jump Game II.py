class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        j = 0
        f = 0
        for i in range(len(nums)):
            f = max(f, nums[i]+i)
            if i!=len(nums)-1 and i==end:
                j+=1
                end = f
        return j