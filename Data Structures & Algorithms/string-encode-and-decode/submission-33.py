class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "false"
        
        string_ = ""
        for word in strs:
            for char_ in word:
                string_ = string_ + str(ord(char_))
                string_ = string_ + ","
            string_ = string_ + "/"
        return string_

    def decode(self, s: str) -> List[str]:
        output = []
        sum_ = ""
        word = ""
        if s == "false":
            return []
        
        for char_ in s:
            if char_ != "," and char_ != "/":
                word = word + char_
            elif char_ == ",":
                sum_ = sum_ + chr(int(word))
                word = ""
            elif char_ == "/":
                output.append(sum_)
                sum_ = ""

        return output