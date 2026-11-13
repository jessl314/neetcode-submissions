class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        input: is an array of integers nums, and a integer k that represents that we want to return
        the k most frequent elements within the array
        k most frequent elemenets: meaning like the top k elements with most frequency

        1st example: 1: 1x, 2: 2x, 3: 3x and k = 2

        so we return the top 2 most frequent elements in the array 
        which is 3 and then 2 as a new array

        the first idea is obviosuly to do a frequency map key:val -> number: frequency. and then in order to get most
        frequent maybe take the list of values and then we pop off the max but obviously that
        doesn't work because then we get confused about which original value it was
        wait never mind, we would just have to create an array with [count, num] elements
        and then sort which sorts the array by count and then pop

        - still need the frequency map -> O(n) thus we want to improve time (orignal is nlogn)
        - we need to somehow order our data by frequency. sort of like below but maybe not exact structure


        1 : [1]
        2: [2]
        3: [3]

        this kind of looks like how an array works actually!

        what if we have a frequency map and then another array consisting of empty lists (n empty lists)

        then we can essentially return the top k most frequent elements startign from n - 1th element

        like in example 1: buckets: [[1], [2], [3]]
        and then we would do a loop
        result = []

        for i in range(len(freq - 1), 0, -1):
            for j in freq[i]:
                we append to result
                if length of result reaches k
                return result
        
        this ends up being O(n) time despite the nested for loop since we in worst
        case still only end up going through n elements (like if all elements are freq 1)
        
        """
        
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        #1: make frequency map
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        #2: fill our buckets 
        # bucket: the numbers with index + 1 frequency

        for c in count:
            # we want to add to the frequency = index + 1 bucket
            # 7: 2, then bucket at index 1 appends 7 in -0index array
            # which makes sense since len(buckets) = 2
            buckets[count[c]].append(c)
    
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                result.append(j)
            if len(result) == k:
                return result
        
        # count = {1: 1}
        # buckets [[1]]

        


        
        
        

        