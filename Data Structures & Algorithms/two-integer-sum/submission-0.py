class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in history:
                return [history[needed], index]
            history[num] = index