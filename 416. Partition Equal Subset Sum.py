
################# brute force ###################
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sum_arr = sum(nums)
        if sum_arr%2 != 0:
            return False
        
        dp = {}
        def util(nums, i, k):
            if k == 0:
                return True
            if i >= len(nums) or k < 0:
                return False
            if (i,k) in dp:
                return dp[(i,k)]
            
            dp[(i,k)] = util(nums, i+1, k) or util(nums, i+1, k-nums[i])
            return dp[(i,k)]
        return util(nums, 0, sum_arr/2)


################# brute force ###################

