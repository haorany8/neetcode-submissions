class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chardir = defaultdict(int)
        for c in t:
            chardir[c] += 1
        
        missing = len(t)

        l = 0

        res = None

        for r in range(len(s)):
            if s[r] in chardir:
                if chardir[s[r]] > 0:
                    missing -= 1

                chardir[s[r]] -= 1

            
            while missing == 0:
                if res == None or r - l < res[1] - res[0]:
                    res = [l, r]
                
                if s[l] in chardir:
                    chardir[s[l]] += 1
                    if chardir[s[l]] > 0:
                        missing += 1
                l += 1
        
        if res == None:
            return ""
        else:
            l, r = res
            return s[l: r + 1]