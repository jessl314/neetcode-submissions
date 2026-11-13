class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums array -> assume valid input, aka only integers, pos, neg etc. 

        the tricky part here is that there are 3 numbers we need so
        I was thinking we should fix one number and then continue to search from there
        it would also make sense to sort the numbers so that we know after say searching for
        all triplets involving -1 in the first example that the following triplets likely don't that least number

        for num in nums

        doing a hashmap type situation since once we have found a second number the next step is to find the difference between 0 and the sum of the first two numbers
        for the third number -> this would require to fix two numbers actually -> but this would be memory inefficient as we have to frequency map
        and also logic inefficient because I would have to create a new map on all combos

        so instead we only fix the first number but then for the remaining i+1 to the end
        use two pointer

        sorted_nums = [-1, -1, 0, 1, 2, 4]
                        f      ^  ^

        last_seen = - 1
        (-1, -1, 2)

        -3, -2, 0 , 0, 1, 2
                ^      ^


        this is still O(n^2) which is the best we can do because we need to inspect every element as a fixed element
        then to find the triplet we do still visit the remaining elements to check this

        O(1) space because no new structure with n elemenets
        // sort here and results array
        for i, num in enumerate(nums):
            // all possible candidates > 0
            if num > 0:
                break
            // avoiding duplicates
            if i > 0 and num = nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    // move both pointers inward since for above we move one side based on >0 or < 0
                    result.append(triplet)
                    l += 1
                    r -= 1
                    // avoid duplicates again
                    while nums[i] == nums[i - 1] and l < r:
                        l += 1
        """
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    if num == nums[i - 1] and l < r:
                        l += 1
        return result

            

        