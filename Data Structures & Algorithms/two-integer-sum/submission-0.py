class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, n in enumerate(nums):
            sol = target - n
            if sol in values:
                return [values[sol], i]

            values[n] = i



