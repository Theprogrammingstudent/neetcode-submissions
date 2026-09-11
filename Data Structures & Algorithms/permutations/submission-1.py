class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                #constraint
                if num in path:
                    continue
                #include nums
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res
