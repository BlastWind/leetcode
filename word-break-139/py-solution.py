import collections
import queue
from typing import List, Set


class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		dp = [False] * (len(s)+1)  # dp[i] represents if s[i:] word breaks
		dp[len(s)] = True  # Base case

		for i in range(len(s) - 1, -1, -1):
			for word in wordDict:
				if i + len(word) <= len(s) and s[i: i + len(word)] == word:
					dp[i] = dp[i+len(word)]
				if dp[i]:
					break
		return dp[0]

	def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
		dp = [False] * (len(s) + 1)  # dp[i] represents if s[0:i] word breaks
		dp[0] = True  # Always have match done character
		for i in range(0, len(s)):
			if not dp[i]:
				break
			for word in wordDict:
				if i + len(word) <= len(s) and not dp[i + len(word)] and s[i: i + len(word)] == word:
					dp[i + len(word)] = True
		return dp[len(dp) - 1]

	def bfs(self, s: str, wordDict: List[str]) -> bool:
		q = collections.deque()
		q.appendleft(s)
		se = set()
		while len(q) > 0:
			str = q.pop()
			for word in wordDict:
				wordLen = len(word)
				if wordLen <= len(str) and str[:wordLen] == word:
					if str[wordLen:] == "":
						return True
					elif str[wordLen:] not in se:
						se.add(str[wordLen:])
						q.appendleft(str[wordLen:])
		return False

	def dfsManual(self, s: str, wordDict: List[str]) -> bool:
		stack = collections.deque()
		stack.append(s)
		se = set()
		while len(stack) > 0:
			str = stack.popleft()
			print(f"popped: {str}")
			for word in wordDict:
				wordLen = len(word)
				if wordLen <= len(str) and str[:wordLen] == word:
					if str[wordLen:] == "":
						return True
					elif str[wordLen:] not in se:
						se.add(str[wordLen:])
						stack.append(str[wordLen:])
						break
		return False

	def dfsHelper(self, s: str, wordDict: List[str], memo: Set[str]) -> bool: 
		for word in wordDict:
			wordLen = len(word)
			if wordLen <= len(s) and s[:wordLen] == word:
				if s[wordLen:] == "":
					return True
				elif s[wordLen:] not in memo:
					memo.add(s[wordLen:])
					if self.dfsHelper(s[wordLen:], wordDict, memo): return True
		return False 
	def dfsDriver(self, s: str, wordDict: List[str]) -> bool:
		return self.dfsHelper(s, wordDict, set())

a = Solution()
print(a.dfsDriver("abcd", ["a", "abc", "b", "cd"]))
