class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l = 0
        r = len(height) - 1

        leftmax = height[l]
        rightmax = height[r]

        water = 0

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])

                water += leftmax - height[l]

            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                water += rightmax - height[r]
        return water
