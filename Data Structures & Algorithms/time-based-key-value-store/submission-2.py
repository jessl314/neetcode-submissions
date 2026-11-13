class TimeMap:
    # are the timestamps added in ascending order or can it be random
    # timestamp range? valid as in above 0? 

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key : [(value, timestamp)...] and we know this is in ascending order
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # we can linearly go through the list -> but even faster is binary search
        # O(n) -> O(logn)
        key_vals = self.store[key]
        if key not in self.store or not key_vals:
            return ""

        l, r = 0, len(key_vals) - 1
        get_val = ""
        while l <= r:
            mid = (l + r) // 2
            if key_vals[mid][1] > timestamp:
                r = mid - 1
            else:
                get_val = key_vals[mid][0]
                l = mid + 1


        return get_val


        
