class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j - i) * min(height[j], height[i])
            max_area = area if area > max_area else max_area
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return max_area


input1 = [1,8,6,2,5,4,8,3,7]
input2 = [1,1]
print(Solution().maxArea(input1))
print(Solution().maxArea(input2))
