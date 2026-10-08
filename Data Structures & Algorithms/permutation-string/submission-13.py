class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chardir_1 = defaultdict(int)
        n = len(s1)

        for c in s1:
            chardir_1[c] += 1

        l  = 0

        for r in range(len(s2)):

            if s2[r] in chardir_1:
                while chardir_1[s2[r]] == 0:
                    chardir_1[s2[l]] += 1
                    l += 1
                chardir_1[s2[r]] -= 1

            while s2[r] not in chardir_1 and l != r:
                if s2[l] in chardir_1:
                    chardir_1[s2[l]] += 1
                l += 1

            if not any(chardir_1.values()):
                return True

        return False