from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        maximums = {}

        for i, h in enumerate(height):
            maximums[i] = h * max(i + 1, len(height) - i)

        for i, h1 in enumerate(height):
            if i == len(height) - 1:
                print(maximums)
                return ans

            if maximums[i] > ans:
                for j in range(i + 1, len(height)):
                    if maximums[j] > ans:
                        h2 = height[j]
                        test_area = (j - i) * min(height[j], h1)
                        ans = max(ans, test_area)


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = Solution().maxArea(array)
print(ans)
