class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chardir = defaultdict(int)
        n = len(t)
        res = defaultdict(list)
        for c in t:
            chardir[c] += 1

        l = 0
        res = None

        missing = len(t)

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

        if res is None:
            return ""
        i, j = res
        return s[i:j+1]
        