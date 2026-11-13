class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        the most simple solution is just check every element which is O(n) however
        we want O(logn) which to me suggests binary search
        here my first thought is with the first example to compare the leftmost element
        with the target which works because 1 < 3 so we look in right half. howeveer
        this would be looking in left half but that doesn't work because if our target 6, it 
        is > 3 so look in left half however 6 is in the right half due to rotatedness

        I think instead should consider how to determine the pivot index

        if we employ a similar search approach then we can take nums[num] and check with the rightmost element
        since 5 > 2 pivot is in the right half somewhere
        6, 1, 2
        1 < 2 that our pivot is within 6, 1 and then 6 > 1 so our pivot is at 1

        binary_search between 0 to pivot - 1 else pivot to the end
        finally -1

        another way without having to do two binary searchs

        is that we need to consider two things relationship between mid and target
        and also left and target

        for the first one -> mid_val is > left_val so this part sorted
        then we check if target is between these if not we know to move our left boundary
        to mid_index + 1

        [3, 4, 5, 6, 1, 2]

        mid_val <= left_val -> right half sorted
        if not in between then we know to check the right boundary being mid_index - 1

       still two passes

       what if instead of searching for this pivot we start with normal binary search

       l, r = 0, len(nums) - 1

       while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        
        // normal sorted array we have left value less than or equal to mid value
        // [6, 1, 2, 3, 4, 5]

        // left half mostly sorted
        if nums[l] <= nums[mid]:
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # normal sorted array we have left value less than or equal to mid value
            # [6, 1, 2, 3, 4, 5]

            # left half mostly sorted
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1