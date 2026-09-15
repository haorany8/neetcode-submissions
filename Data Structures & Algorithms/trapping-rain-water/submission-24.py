class Solution:
    def trap(self, height: List[int]) -> int:
        def ispool(l, r):
            area_min = 0
            area_max = 0
            h_min = min(height[l], height[r])
            h_max = max(height[l], height[r])

            min_max = -1
            min_max_index = -1

            flag = True

            for i in range(l + 1, r):
                if height[i] >= h_max:
                    return False, 0, i
                elif height[i] >= h_min:
                    if height[i] > min_max:
                        min_max = height[i]
                        min_max_index = i
                        flag = False
                else:
                    area_min += h_min - height[i]
                    area_max += h_max - height[i]
            if flag:
                return True, area_min, None
            else:
                return False,0 , min_max_index

        n_ = len(height)
        max_ = 0
        l = 0
        r = n_ - 1
        area = 0
        while l < n_ - 1:
            flag, tmp, index = ispool(l ,r)
            if flag:
                area += tmp
                l = r
                r = n_ - 1
            else:
                r = index
                if l + 1 == r:
                    l += 1
                    r = n_ - 1
        
        return area
                