class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        given: integer array heights, height[i] is the height of the i-th bar
        amount of water = area of rectangle where width is right bar index - left bar index
        height is the minimum of these two bars heights
        a = l * w
        return: max amount of water a container can store -> max area
        naive: find the tallest bar and then compare the areas with it and every other bar for the max
        or even do a nested for loop which is n^2

        my plan:
        what if we in order to do better than O(n^2) iterate through array using two pointer approach (in-place)
        we would have two pointers p1 and p2 at opposite ends. now since the min of heights is the container water height
        we know that we should "move on" from that bar in the hopes of finding a higher bar

        """
        result = 0
        p1,p2 = 0, len(heights) - 1

        while p1 < p2:
            height = min(heights[p1], heights[p2])
            area = (p2 - p1) * height
            result = max(result, area)
            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return result
        