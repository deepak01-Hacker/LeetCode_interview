class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = {}
        def maxSumCofficient(index, satisf, time):
            if index >= len(satisf):
                return 0
            if (index, time) in dp:
                return dp[(index, time)]

            dp[(index, time)] = max((time * satisf[index]) + maxSumCofficient(index+1, satisf, time+1), maxSumCofficient(index+1, satisf, time))
            return dp[(index, time)]
        return maxSumCofficient(0, satisfaction, 1)
