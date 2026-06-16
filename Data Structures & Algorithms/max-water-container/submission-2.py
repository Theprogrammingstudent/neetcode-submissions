class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxHeight = 0

        for i in heights:
            container = (r - l) * min(heights[l], heights[r])
            maxHeight = max(maxHeight, container)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxHeight
