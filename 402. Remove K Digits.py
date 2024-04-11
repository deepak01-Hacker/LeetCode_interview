class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        def util(num, k):
            if num == "":
                return 0
            if k == 0:
                return int(num)
            res = int(num)
            for i in range(len(num)):
               res = min(res, util(num[:i] + num[i+1:], k-1))
            return res
        return str(util(num, k))
