# brute force
class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        
        def isValid(hashmap, index, j):
            if j in hashmap:
                return False
            for k in hashmap.keys():
                if (j < k and hashmap[k] < index) or (j > k and hashmap[k] > index):
                    return False
            return True

        def util(index, nums1, nums2, hashmap):
            if index >= len(nums1):
                return 0
            
            result = 0
            for j in range(len(nums2)):
                if nums1[index] == nums2[j] and isValid(hashmap, index, j):
                    hashmap[j] = index
                    result = max(result, util(index+1, nums1, nums2, hashmap)+1)
                    del hashmap[j]

            return max(result, util(index+1, nums1, nums2, hashmap))
        
        hashmap = {}
        return util(0, nums1, nums2, hashmap)

# better approach

class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:

        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
