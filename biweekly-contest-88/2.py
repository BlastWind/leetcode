class LUPrefix:

    def __init__(self, n: int):
        # dummy: Make array of length 10000
        self.vid = [False] * n
        self.lastLongest = 1
    def upload(self, video: int) -> None:
        self.vid[video] = True
    def longest(self) -> int:
        # print(self.vid, self.lastLongest, len(self.vid))
        for i in range(self.lastLongest, len(self.vid)):
            b = self.vid[i]
            if not b: 
                self.lastLongest = max(1 if i == 1 else i, self.lastLongest)
                return i - 1
            if i == len(self.vid) - 1: 
                self.lastLongest = len(self.vid) - 2
                return len(self.vid) - 1
        return -3

server = LUPrefix(4)
server.upload(3)            
print(server.longest())
                              
server.upload(1)              
print(server.longest()              )
server.upload(2)              
print(server.longest()              )