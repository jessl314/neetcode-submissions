class Solution:
    def trap(self, height: List[int]) -> int:
        """
        and the idea for a area to contain water, the height is determined by the shorter wall
        width of a singular wall is always 1?
        and we want max area of water 

        and then can one boundary be at the first and last elements -> no

        I will also consider the water column by column then sum as I go this works 
        because as long as we know the boundary is somewhere 

        [0,2,0,3,1,0,1,3,2,1]
           ^               ^
         the max left wall height is 0 right wall height 1 so no possible water here

         left_max = 0
         right_max = 1


         to calculate the water I can trap at any given index block it is 
         minimum(left_max_h, right_max_h) - height[curr]

        """
        if not height:
            return 0
        water = 0
        l, r = 0, len(height) - 1
        l_max_h, r_max_h = height[l], height[r]
        # amount of water = max_h - height[curr]

        while l < r:
            if l_max_h < r_max_h:
                l += 1
                l_max_h = max(l_max_h, height[l])
                water += (l_max_h - height[l])
                
                
            else:
                r -= 1
                r_max_h = max(r_max_h, height[r])
                water += (r_max_h - height[r])
              
        return water

        