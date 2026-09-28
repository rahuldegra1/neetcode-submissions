class Solution(object):
    def subsets(self, nums):
        res = []
        
        def dfs(i, current_subset):
            if i >= len(nums):
                res.append(current_subset)
                return 
            
            # Decision to include nums[i]
            dfs(i + 1, current_subset + [nums[i]])
            
            # Decision NOT to include nums[i]
            dfs(i + 1, current_subset)
            
        dfs(0, [])
        return res
