from typing import List


def generate_subset_sums(nums: List[int]):
	sums = []
	def recur(index, acc):
		if index >= len(nums):
			sums.append(acc)
			return
		recur(index+1, acc)
		recur(index+1, acc+nums[index])
	recur(0, 0)
	return sums

print(generate_subset_sums([1, 2, 4]))