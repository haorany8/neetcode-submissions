class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s)
        j = len(s)-1
        i = 0
        gap = ord("a") - ord("A")

        Alp_list = list(range(ord("A"), ord("Z") + 1)) + list(range(ord("a"), ord("z") + 1)) + list(range(ord("0"), ord("9") + 1))

        C_list = list(range(ord("A"), ord("Z") + 1)) + list(range(ord("a"), ord("z") + 1))
        L_list = list(range(ord("a"), ord("z") + 1))
        num_list = list(range(ord("0"), ord("9") + 1))

        while i <= j:
            ord_i = ord(s_list[i])
            ord_j = ord(s_list[j])

            if ord_i not in Alp_list:
                i += 1
            if ord_j not in Alp_list:
                j -= 1

            if ord_i in Alp_list and ord_j in Alp_list:

                if ord_i in C_list and ord_j in C_list:
                    if ord_i == ord_j or ord_i + gap == ord_j or ord_i - gap == ord_j:
                        i += 1
                        j -= 1
                    else:
                        return False
                elif (ord_i in num_list and ord_j in num_list):
                    if ord_i == ord_j:
                        i += 1
                        j -=1
                    else:
                        return False
                else:
                    return False

        return True

