class Logger:

    def __init__(self):
        self.logToTime = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logToTime or timestamp >= self.logToTime[message] + 10:
            self.logToTime[message] = timestamp
            return True
        return False
        # Your Logger object will be instantiated and called as such:
        # obj = Logger()
        # param_1 = obj.shouldPrintMessage(timestamp,message)
