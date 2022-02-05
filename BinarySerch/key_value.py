# to identify the value, we need both key and timestamp
# timestamp is strictly increasing = already sorted 
class TimeMap:

    def __init__(self):
        # key = string, value = list of [value, timestamp]
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # the key exists in store dictionary
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l, r = 0, len(values)-1
        
        while l <= r:
            m = (l+r)//2
            
            if values[m][1] <= timestamp:
                # update res, because values[m][1] is colser so far
                res = values[m][0]
                l = m+1
            else: 
                r = m-1
                
        # if store does not have the key, res will not be updated and will be empty string
        return res
                
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)