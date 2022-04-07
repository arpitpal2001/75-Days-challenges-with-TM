class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        l1 = len(nums)
        if l1%2 != 0:
            return nums[l1//2]
        return ((nums[(l1//2)-1] + nums[l1//2])/2 )