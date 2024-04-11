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

# better approach 


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for i in num:
            while(stack and stack[-1] > i and k > 0):
                stack.pop()
                k -= 1
            stack.append(i)

        while(stack and k > 0):
            stack.pop()
            k -= 1

        while(stack and stack[0] == "0" and stack.count('0') <= len(stack)):
            stack.pop(0)
        
        if stack == []:
            return "0"

        return "".join(stack)

