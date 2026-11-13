class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k -> banana-per-hour rate so we can either eat k bananas from some pile or if less than
        k bananas in pile eat all of those

        my first thought was just take k or less bananas from each pile and loop until all zero, decrementing each 
        time -> quite inefficient as multiple passes -> it would make more sense to do division
        [1, 4, 3, 2] -> if k = 1 then 1 + 4 + 3 + 2 but then we have to consider fractions 
        so if k = 3 then when piles[i] 4 we have 4/3 but it takes two hours according the 2nd rule
        so ceiling of 4/3
        k: 1 ... max(piles)
        h: target number of hours 

        // per pile
        hour = ceiling(piles[i] / k)

        brute force: is try all k values using this formula
        O(n * m) where m is number of elements in piles and n is number of possible k values

        O(n * logm) binary search within k values
        
        """
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            mid_k = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / mid_k)
            if total_time <= h:
                min_k = mid_k
                r = mid_k - 1
            else:
                l = mid_k + 1
        return min_k
