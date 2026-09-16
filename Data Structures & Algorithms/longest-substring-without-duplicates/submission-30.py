class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        s = list(s)
        n_ = len(s)
        if len(s) == 0:
            return 0

        max_length = len(set(s))

        for l in range(max_length, 0, -1):
            for i in range(n_):
                if l == len(set(s[i: i + l])):
                    return l
        
            
