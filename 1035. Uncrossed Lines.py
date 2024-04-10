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
