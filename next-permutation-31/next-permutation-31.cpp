#include <string>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <unordered_map>

using namespace std;
class Solution
{
public:
	void nextPermutation(vector<int> &nums)
	{
		int i = nums.size() - 1;
		for (int cur = nums[i]; i >= 0; cur = nums[i], i--)
		{
			if (nums[i] < cur)
				break;
		}
		// if all descending, the next permutation is the first permutation in an array of all sorted permutations
		if (i == -1 || nums.size() == 2)
		{
			reverse(nums.begin(), nums.end());
			return;
		}
		// else, find first pair whose right > left
		int pivot = i, smallest = nums[i + 1], smallestIndex = i + 1;
		for (i = pivot + 2; i < nums.size(); i++)
		{
			if (nums[pivot] < nums[i] && nums[i] <= smallest)
			{
				smallest = nums[i];
				smallestIndex = i;
			}
		}

		// swap first element in the pair (first, counting from left to right) with the smallest larger element in the sequence to the right
		swap(nums, pivot, smallestIndex);
		// then, reverse right sequence
		reverse(nums.begin() + pivot + 1, nums.end());
	}
	void swap(vector<int> &nums, int one, int two)
	{
		int temp = nums[one];
		nums[one] = nums[two];
		nums[two] = temp;
	}
};
int main(int argc, char *argv[])
{
	Solution a;
	vector<int> from{2, 3, 1, 3, 3};
	a.nextPermutation(from);
	for (auto row : from)
		cout << row << endl;

	return 0;
}
