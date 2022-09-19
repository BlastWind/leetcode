from typing import List, Tuple


# class Solution:
# 	def smallestNumber(self, pattern: str) -> str:
# 		# greedy with many combinations and backtracking?
# 		# If a particular path doesn't work, reset
# 		# Try to be greedy
# 		# recur(rest of pattern)
# 		def recur(index: int, lastDigit: int, used: List[bool]) -> Tuple[bool, str]:
# 			if index == len(pattern):
# 				return (True, "")
# 			p = pattern[index]
# 			if p == "I":
# 				# if increasing, try to add the smallest greater unused val
# 				for i in range(lastDigit, 10):
# 					if not used[i]:
# 						used[i] = True
# 						(valid, result) = recur(index + 1, i , used)
# 						if valid:
# 							return (True, str(i) + result)
# 						used[i] = False
# 			elif p == "D":
# 				# if decreasing, try to add the largest lesser unused val
# 				for i in range(lastDigit, 0, -1):
# 					if not used[i]:
# 						used[i] = True
# 						(valid, result) = recur(index + 1, i, used)
# 						if valid:
# 							return (True, str(i) + result)
# 						used[i] = False
# 			return (False, "")

# 		# Driver
# 		for i in range(1, 10):
# 			used = [False] * 10
# 			used[i] = True
# 			(valid, result) = recur(0, i, used)
# 			if valid: return str(i) + result


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        dq = [1]  # [1,2,3,5,4,6]
        tmp = []  # []
        i = 2
        for p in pattern:
            if p == 'I':
                while tmp:
                    dq.append(tmp.pop())
                dq.append(i)
                i += 1
            else:
                tmp.append(dq.pop())
                dq.append(i)
                i += 1
        while tmp:
            dq.append(tmp.pop())
        return ''.join(map(str, dq))

    def mySmallestNumber(self, pattern: str) -> str:
        dq = []
        # if encountered 'D', remove previous element and append the greater, current element
        # if encoutnered two 'D', this will show the greatest element being inserted, and then
        # the removed element can be inserted in reverse (decreasing) order
        i = 0
        for k in map(len, pattern.split('I')):
            # k is how many D in a row do we encounter
            # k + 1 is how many numbers to insert in this segment
            segmentLen = k + 1
            dq.extend(range(i + segmentLen, i, -1))
            i += segmentLen
        return ''.join(map(str, dq))


a = Solution()
print(a.mySmallestNumber("IIIDIDDD"))
