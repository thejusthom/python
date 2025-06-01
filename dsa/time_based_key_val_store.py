class TimeMap(object):

    def __init__(self):
        self.timeMap = {}
                

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value,timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        val = self.timeMap.get(key,[])
        l,r = 0,len(val)-1
        while l <= r:
            m = (l+r)//2
            if timestamp >= val[m][1]:
                res = val[m][0]
                l = m+1
            else:
                r = m-1
        return res
    
timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 1))  
print(timeMap.get("foo", 3))         
print(timeMap.set("foo", "bar2", 4))
print(timeMap.get("foo", 4))         
print(timeMap.get("foo", 5)) 