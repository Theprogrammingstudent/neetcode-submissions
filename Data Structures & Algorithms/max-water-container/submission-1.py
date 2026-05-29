class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We use two pointers to solve this
        # Declare a result
        # Declare two pointers
        # Calculate the area of where the pointers are at
        # ( r-l ) * min(height[l], height[r])
        # Calc res by finding the max of res and area
        # Next move the pointers forward
        # choose the smaller one to move left or right

        res = 0
        l, r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res    