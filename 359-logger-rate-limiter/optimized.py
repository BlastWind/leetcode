class Logger:
    def __init__(self) -> None:
        self.newMessages = {}
        self.oldMessages = {}
        self.lastTimeStamp = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.lastTimeStamp + 20:
            self.newMessages = {}
            self.oldMessages = {}
            self.lastTimeStamp = timestamp
        elif timestamp >= self.lastTimeStamp + 10:
            self.oldMessages = self.newMessages
            self.newMessages = {}
            self.lastTimeStamp = timestamp
        if message in self.newMessages: 
            return False 
        
        if message in self.oldMessages: 
            if timestamp < self.oldMessages[message] + 10: 
                return False
        
        self.newMessages[message] = timestamp 
        return True
class bucketLogger:
    def __init__(self):
        self.buckets = [0] * 10
        self.sets = [set() for _ in range(10)]

    def shouldPrintMessageBucketSort(self, timestamp: int, message: str) -> bool:
        idx = timestamp % 10
        if timestamp != self.buckets[idx]:
            self.sets[idx].clear()
            self.buckets[idx] = timestamp
        for i in range(len(self.buckets)):
            if(timestamp - self.buckets[i] < 10):
                if message in self.sets[i]:
                    return False
        self.sets[idx].add(message)
        return True


obj = Logger()
obj.shouldPrintMessage(1, "foo")
obj.shouldPrintMessage(2, "bar")
obj.shouldPrintMessage(3, "foo")
obj.shouldPrintMessage(8, "bar")
obj.shouldPrintMessage(10, "foo")
obj.shouldPrintMessage(11, "foo")
