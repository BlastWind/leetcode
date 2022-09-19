class Solution:
	def countSpecialNumbers(self, n: int) -> int:
		def isSpecial(n: int): 
			strr = str(n) 
			mp = {}
			for j in strr: 
				if j in mp: 
					return False 
				mp[j] = 1
			return True
		for i in range(1, n + 1): 
			if not isSpecial(i): 
				print(i)
a = Solution() 
a.countSpecialNumbers(1000)