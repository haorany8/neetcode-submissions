class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        
        for word in strs:
            n_ = len(word)
            
            res.append(str(n_))
            res.append("#")
            res.append(word)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            l_ = int(s[i:j])
            i = j + 1
            j = i + l_
            output.append(s[i:j])
            i = j
    
        return output