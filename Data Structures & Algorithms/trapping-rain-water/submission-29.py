class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        Maxleft, Maxright = height[l], height[r]
        area = 0

        while l < r:
            if Maxleft < Maxright:
                l += 1
                Maxleft = max(Maxleft, height[l])
                area += Maxleft - height[l]
            else:
                r -= 1
                Maxright = max(Maxright, height[r])
                area += Maxright - height[r]

        return area