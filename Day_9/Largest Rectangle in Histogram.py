class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, p, ma = [], 0, 0
        n = len(heights)
        for i in range(n):
            while(stack and heights[stack[-1]] > heights[i]):
                p = stack.pop()
                if stack:
                    area = heights[p] * (i-stack[-1]-1)
                    ma = max(ma, area)
                else:
                    area = heights[p]*(i-0)
                    ma = max(ma, area)
            
            stack.append(i)
        
        while stack:
                 
                p = stack.pop()
                if stack:
                    area = heights[p]*(n-stack[-1]-1)
                    ma = max(ma, area)
                else:
                    area = heights[p]*(n-0)
                    ma = max(ma, area)
                    
        return ma