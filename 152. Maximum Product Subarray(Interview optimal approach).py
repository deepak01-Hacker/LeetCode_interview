class Solution:
    def maxProduct(self, a: List[int]) -> int:

        negative_freq = 0
        result = max(a)

        prefix = []
        pre_pod = 1
        has_zero = False
        for i in range(len(a)):
            negative_freq += 0 if a[i] >= 0 else 1

            pre_pod *= a[i]
            prefix.append(pre_pod)
            if pre_pod == 0:
                has_zero = True
                pre_pod=1

        if negative_freq%2 == 0 and not has_zero:
            return reduce(lambda x, y: x * y, a)
        
        suff_prod = 1
        for j in range(len(a)-1, 0, -1):

            suff_prod *= a[j]
            result = max(result, suff_prod, prefix[j-1])
            if suff_prod == 0:
                suff_prod=1
        return result


            
        
  
