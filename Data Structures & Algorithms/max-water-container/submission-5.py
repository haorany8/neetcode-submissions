class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ = 0
        n_ = len(heights)
        l, r = 0, len(heights) - 1
        
        i1 = i2 = -1

        for i, value in enumerate(heights):
            if i1 == -1 or value >= heights[i1]:
                i1 = i
                i2 = i1
            elif i2 == -1 or value >= heights[i2]:
                i2 = i
        
        if i1 < i2:
            l = i1
            r = i2
        else:
            l = i2
            r = i1

        max_ = min(heights[i1], heights[i2]) * (r - l)

        for j in range(r, n_):
            for i in range(l+1):
                h = min(heights[j], heights[i])
                w = j - i
                if h * w > max_:
                    max_ = h * w

        return max_
                
