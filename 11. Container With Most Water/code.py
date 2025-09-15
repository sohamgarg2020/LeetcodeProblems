class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1
        while right > left:
            if min(height[left], height[right])* (right-left) > area:
                area = min(height[left], height[right])* (right-left)
                print(right-left)
            else:
                if height[left] > height[right]:
                    right-= 1
                elif height[right] > height[left]:
                    left += 1
                else:
                    left += 1
        return area
